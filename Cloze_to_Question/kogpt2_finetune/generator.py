import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.getcwd()))))

import argparse
import torch
from utils import get_tokenizer_vocab, kogpt2_config
from Cloze_to_Question.kogpt2.model.torch_gpt2 import GPT2Config, GPT2LMHeadModel


parser = argparse.ArgumentParser()
parser.add_argument('--sentence', type = str, default = '드라마 킹덤의 주연은 <mask>이다.',
                    help = '질문으로 바꾸고 싶은 masked 문장을 입력합니다.')
parser.add_argument('--saved_model', type = str, default = '../save_model/KoGPT2_checkpoint_11985.tar',
                    help = '학습된 모델을 불러오는 경로입니다.')
args = parser.parse_args()

def generator(sentence, saved_model):
    if torch.cuda.is_available():
        ctx = 'cuda'
    else:
        ctx = 'cpu'
    device = torch.device(ctx)

    sp_tokenizer, kogpt2_vocab = get_tokenizer_vocab()
    checkpoint = torch.load(saved_model, map_location = device)
    model = GPT2LMHeadModel(config = GPT2Config.from_dict(kogpt2_config))
    model.load_state_dict(checkpoint['model_state_dict'])

    model.to(device)
    model.eval()

    sentence += ';'
    tokenized_sent = sp_tokenizer(sentence)
    integer_sent = [kogpt2_vocab[kogpt2_vocab.bos_token]] + kogpt2_vocab[tokenized_sent]

    while 1:
        input_ids = torch.tensor(integer_sent).unsqueeze(0)
        input_ids.to(ctx)
        model.to(ctx)

        pred = model(input_ids)[0]
        gen = kogpt2_vocab.to_tokens(torch.argmax(pred, axis = -1).squeeze().tolist())[-1]
        if gen == '</s>':
            break
        else:
            sentence += str(gen)
            integer_gen = kogpt2_vocab(gen)
            integer_sent += [integer_gen]

    sentence = sentence.replace('▁', ' ')
    return sentence.split(';')[1]

if __name__ == '__main__':
    question = generator(args.sentence, args.saved_model)
    print(question)