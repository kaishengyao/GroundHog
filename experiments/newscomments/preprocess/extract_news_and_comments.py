__author__ = 'kaisheny'

import json
import sys
import glob
import errno
import argparse
import os
import nltk
from nltk import word_tokenize

parser = argparse.ArgumentParser(
    description="""
This takes a directory name with json files inside and create a text file of the content to be retrieved
""", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-d", "--directory", default='.',
                    help="the directory with json file")
parser.add_argument("-c", "--content", default='Body',
                    help="the content to be read")
parser.add_argument("-o", "--output", default='content.txt',
                    help="the file name to save content")
parser.add_argument("-m", "--comment", default='comment.txt',
                    help="the file name to save comments")
parser.add_argument("-l", "--length", default='10000',
                    help="the maximum length")

class loadJson(object):
    def __init__(self):
        self.fn = ''
        self.content = []
        self.comments = []
        self.what_to_read = ['Body', ['CommentList', 0, 'Content']]
        self.file_ext = 'json'
        self.maxlen= 10000

    def setWhatToRead(self, what_to_read):
        self.what_to_read = what_to_read

    def setMaxLen(self, maxlen):
        self.maxlen = maxlen

    def tokenize(self, raw):
        tokens = word_tokenize(raw)
        text = nltk.Text(tokens)
        newstr = ''
        for t in text:
            newstr += t + ' '
        return newstr

    def loadEach(self, fn, maxlen=10000):
        with open(fn) as data_file:
            data = json.load(data_file)
            news = None
            cmt = None
            for cn in self.what_to_read:
                if not isinstance(cn, list):
                    info = data[cn]
                    if info != None:
                        news = info.lower()
                else:
                    info = data
                    succ = True
                    for idx in cn:
                        if isinstance(info, list) and len(info) == 0:
                            succ = False
                            break
                        info = info[idx]
                        if info == None:
                            succ = False
                            break
                    if succ == True: # there are comments
                        cmt = info
            # everything lower case
            if news != None and cmt != None:
                news = news.strip()
                cmt = cmt.strip()

                if len(news) > 0 and len(cmt) > 0:
                    cntn = news.lower()
                    cntn = self.tokenize(cntn)
                    ln = cntn.split()
                    if len(ln) > maxlen:
                        nln = ln[0:maxlen]
                    else:
                        nln = ln
                    self.content.append(' '.join(nln))

                    cmtn = cmt.lower()
                    cmtn = self.tokenize(cmtn)
                    ln = cmtn.split()
                    if len(ln) > maxlen:
                        nln = ln[0:maxlen]
                    else:
                        nln = ln
                    self.comments.append(' '.join(nln))

    def loadDir(self, dirname, maxlen=10000):
        path = dirname + '/*' + self.file_ext
        files = glob.glob(path)

        maxlen = int(maxlen)

        for fname in files:
            try:
                self.loadEach(fname, maxlen)
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise

    def saveCotent(self, fn1, fn2):

        dirname, filename = os.path.split(fn1)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        id = 0
        f = open(fn1, 'w')
        try:
            for c in self.content:
                s = c + '\n'
                f.write(s.encode("UTF-8"))
                id += 1
        finally:
            f.close()

        id = 0
        f = open(fn2, 'w')
        try:
            for c in self.comments:
                s = c + '\n'
                f.write(s.encode("UTF-8"))
                id += 1
        finally:
            f.close()


def main(dirfrm, news_save_to, comments_to_save, maxlen):
    reader = loadJson()

    reader.loadDir(dirfrm, maxlen)

    reader.saveCotent(news_save_to, comments_to_save)

'''
example:
1) 10000 words at most, i.e., use all words in an article
python extract_news_and_comments.py -d D:/data/Articles/2015/03-23 -o d:/data/newscomments/2015/03-23/news.txt -m d:/data/newscomments/2015/03-23/comments.txt

2) 50 words at most
python extract_news_and_comments.py -d D:/data/Articles/2015/03-23 -o d:/data/newscomments/45wrds/2015/03-23/news.txt -m d:/data/newscomments/45wrds/2015/03-23/comments.txt -l 45
'''
if __name__ == "__main__":
    args = parser.parse_args()
    main(args.directory, args.output, args.comment, args.length)

