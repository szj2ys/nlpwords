# *_*coding:utf-8 *_*
'''
Descri：
'''
from stopwds import stopwords
import jieba

text = ('医美产业崛起的同时，我国医美行业也形成了一条清晰且完整的产业链，上游医美产品生产企业占据了产业链核心环节。')
cut_sent = [word for word in jieba.cut(text) if word and word not in stopwords(user_stopwds='user_stopwords.txt')]
print(cut_sent)
# stopwords = stopwords()
# for stopword in stopwords:
#     print(stopword)
