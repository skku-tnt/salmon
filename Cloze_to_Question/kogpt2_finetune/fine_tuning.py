import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.getcwd()))))

from torch.utils.data import Dataset
from Cloze_to_Question.kogpt2.utils import download, tokenizer, get_tokenizer
from gluonnlp.data import SentencepieceTokenizer
import gluonnlp
import pandas as pd
import torch
from torch.utils.data import DataLoader
from Cloze_to_Question.kogpt2.model.torch_gpt2 import GPT2Config, GPT2LMHeadModel
import re
import argparse
from utils import get_tokenizer_vocab, kogpt2_config, pytorch_kogpt2

parser = argparse.ArgumentParser()
parser.add_argument('--epoch', type = int, default = 3,
                    help = 'epoch를 통해서 학습 범위를 조절합니다.')
parser.add_argument('--save_path', type = str, default = '../save_model/',
                    help = '학습된 결과 모델을 저장하는 경로입니다.')
parser.add_argument('--load_path', type = str, default = '../save_model/KoGPT2_checkpoint_11985.tar',
                    help = '기존에 학습된 모델을 불러오는 경로입니다.')
parser.add_argument('--data_path', type = str, default = '../data/KorQuAD/korquad_gpt2.txt',
                    help = '학습 데이터(txt형식)을 불러오는 경로입니다.')
parser.add_argument('--batch_size', type = int, default = 16,
                    help = 'batch_size를 지정합니다.')
args = parser.parse_args()


class Read_Dataset(Dataset):

    def __init__(self, file_path, tokenizer, vocab):
        self.data = []
        self.df = pd.read_csv(file_path, encoding = 'utf-8')
        self.tokenizer = tokenizer
        self.vocab = vocab

        for idx, sent in enumerate(self.df['tar_sent']):
            tokenized_sent = tokenizer(sent)
            tokenized_ques = tokenizer(self.df['question'][idx])
            index_of_words = [vocab[vocab.bos_token]] + vocab[tokenized_sent] + [vocab[';']]\
                             + vocab[tokenized_ques] + [vocab[vocab.eos_token]]
            self.data.append(index_of_words)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]


def fine_tuning(epoch, save_path, load_path, file_path, batch_size):
    if torch.cuda.is_available():
        ctx = 'cuda'
    else:
        ctx = 'cpu'

    cachedir = '~/kogpt2/'
    device = torch.device(ctx)

    sp_tokenizer, kogpt2_vocab = get_tokenizer_vocab()

    model_info = pytorch_kogpt2
    model_path = download(model_info['url'],
                          model_info['fname'],
                          model_info['chksum'],
                          cachedir = cachedir)
    kogpt2model = GPT2LMHeadModel(config = GPT2Config.from_dict(kogpt2_config))
    kogpt2model.load_state_dict(torch.load(model_path))
    kogpt2model.to(device)

    try:
        checkpoint = torch.load(load_path, map_location = device)
        kogpt2model = GPT2LMHeadModel(config = GPT2Config.from_dict(kogpt2_config))
        kogpt2model.load_state_dict(checkpoint['model_state_dict'])
        kogpt2model.eval()

    except:
        count = 0

    else:
        count = int(re.findall("\d+", load_path)[1])

    print("loaded model check with train_number \n train_number(count) : {}".format(count))
    # count == 0 : 새로 불러온 모델
    # count != 0 : batch 단위 학습이 몇번 진행됐는지 count 횟수를 통해 파악

    kogpt2model.train()
    model = kogpt2model

    dataset = Read_Dataset(file_path, sp_tokenizer, kogpt2_vocab)
    data_loader = DataLoader(dataset, batch_size = batch_size, shuffle = True, pin_memory = True)

    learning_rate = 3e-5
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

    print('KoGPT-2 Fine Tuning Start')
    avg_loss = (0.0, 0.0)

    for epoch in range(epoch):
        for data in data_loader:
            optimizer.zero_grad()
            data = torch.stack(data)
            data = data.transpose(1, 0)
            data = data.to(ctx)
            model = model.to(ctx)

            outputs = model(data, labels = data)
            loss, logits = outputs[:2]
            loss = loss.to(ctx)
            avg_loss = (avg_loss[0] * 0.99 + loss, avg_loss[1] * 0.99 + 1.0)
            optimizer.step()

            if count % 10 == 0:
                print('epoch : {} / train number : {} / loss : {:.5f} / avg_loss : {:.5f}'.format(epoch, count, loss, avg_loss[0] / avg_loss[1]))
            count += 1

            if (count > 0 and count % 10000 == 0) or (len(data) < batch_size):
                try:
                    torch.save({
                        'epoch' : epoch,
                        'train_no' : count,
                        'model_state_dict' : model.state_dict(),
                        'optimizer_state_dict' : optimizer.state_dict(),
                        'loss' : loss
                    }, save_path + 'KoGPT2_checkpoint_' + str(count) + '.tar')
                except:
                    pass

if __name__ == "__main__":
    fine_tuning(args.epoch, args.save_path, args.load_path, args.data_path, args.batch_size)


