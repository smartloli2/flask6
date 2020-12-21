from nltk import sent_tokenize
from typing import List, Dict
import json
import os


def get_sentences_from_file(filename: str = "./game_of_thrones.txt", lang: str = "english") -> List[str]:
    with open(filename, "r", encoding="unicode_escape") as book:
        text = book.read()
        sentences = sent_tokenize(text, lang)
        return sentences


def find_words(sentences: List[str], words: List[str], examples: int = 5) -> dict:
    ret = []
    for sentence in sentences:
        if examples <= 0:
            break
        if any(word in sentence for word in words):
            ret.append(sentence)
            examples -= 1
    return {'words': ret}


def find_words_by_request(req: dict) -> dict:
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    got = os.path.join(THIS_FOLDER, 'game_of_thrones.txt')
    new_sentences = get_sentences_from_file(got)
    return find_words(new_sentences, req['words'], req['examples'])
