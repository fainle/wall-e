#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sample.model.corpus import Corpus
import requests
from bs4 import BeautifulSoup
from sample.model import db_session
from sample.model.corpus import Corpus

# print(soup)
i = 1
corpus = Corpus.query.order_by(Corpus.id.desc()).first()
if corpus:
    times = corpus.times + 1
else:
    times = 1

for num in range(3920):
    res = requests.get('http://notsocleverbot.jimrule.com/scripts/ajax.php?action=display&page=%s' % num)
    soup = BeautifulSoup(res.content, 'html5lib')

    for tag in soup.find_all('span'):
        _class = tag.get('class')

        if not _class:
            continue

        if _class[0] == 'cleverbot' or _class[0] == 'user':

            if _class[0] == 'cleverbot':
                type = 1
            else:
                type = 2

            if i % 2 != 0:
                corpus = Corpus()
                if tag.get_text():
                    corpus.q = tag.get_text().split(":")[1]

                corpus.type = type
                corpus.times = times
                db_session.add(corpus)
                db_session.commit()
            else:
                corpus = Corpus.query.order_by(Corpus.id.desc()).first()
                if tag.get_text():
                    corpus.a = tag.get_text().split(":")[1]
                db_session.commit()

            i += 1
        if _class[0] == 'time':
            i = 1
            times += 1


