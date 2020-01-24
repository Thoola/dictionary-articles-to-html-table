import os 
import json
from json2html import *
import corpus_parse as cp
scriptdir = os.path.dirname(os.path.abspath(__file__))


class TextProcessing:
    def __init__(self):
        self.WORDS = dict()
        self.TEXT = str()
        self.jdata = []
        self.processing = str()

    def input(self, file_txt: str):
        sp_file = os.path.join(scriptdir, file_txt)
        self.TEXT = open(sp_file, 'r')
        self.processing = self.TEXT.read()
        self.TEXT.close()

    def containerWords(self):
        mass = self.processing.split('&')
        for part in mass:
            i = part.find('—')
            self.WORDS[str(part[0:i])] = str(part[i:])

    def containerTexts(self):
        for ke, va in sorted(self.WORDS.items()):
            self.jdata.append({'alph': ke[0], 'title': ke[0:ke.index(' ')],
                               'def': ke, 'content': va,
                               'context': cp.get_leeds(ke[0:ke.index(' ')])+'\n'+cp.get_nkrya(ke[0:ke.index(' ')])})
        
    def output(self):
        with open('data.json', 'w', 4, 'utf-8') as fp:
            json.dump(self.jdata, fp, skipkeys=False, ensure_ascii=False)


def genhtml(ind):
    with open(ind, 'r') as jcash:
        jj = jcash.read()
        data = json2html.convert(json=jj)
    with open('predata.html', 'w', 4, 'utf-8') as temp:
        temp.write(data)


# tp = TextProcessing()
# tp.input('TEXT')
# tp.containerWords()
# tp.containerTexts()
# tp.output()
genhtml('jdata.json')