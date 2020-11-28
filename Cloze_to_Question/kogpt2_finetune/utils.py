import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.getcwd()))))

from Cloze_to_Question.kogpt2.utils import get_tokenizer
from gluonnlp.data import SentencepieceTokenizer
import gluonnlp

def get_tokenizer_vocab():
    path = get_tokenizer()
    sp_tokenizer = SentencepieceTokenizer(path)

    kogpt2_vocab = gluonnlp.vocab.BERTVocab.from_sentencepiece(path,
                                                               mask_token = None,
                                                               sep_token = None,
                                                               cls_token = None,
                                                               unknown_token = '<unk>',
                                                               padding_token = '<pad>',
                                                               bos_token = '<s>',
                                                               eos_token = '</s>')

    return sp_tokenizer, kogpt2_vocab

kogpt2_config = {
    "initializer_range": 0.02,
    "layer_norm_epsilon": 1e-05,
    "n_ctx": 1024,
    "n_embd": 768,
    "n_head": 12,
    "n_layer": 12,
    "n_positions": 1024,
    "vocab_size": 50000
    }

pytorch_kogpt2 = {
    'url':
    'https://kobert.blob.core.windows.net/models/kogpt2/pytorch/pytorch_kogpt2_676e9bcfa7.params',
    'fname': 'pytorch_kogpt2_676e9bcfa7.params',
    'chksum': '676e9bcfa7'
    }