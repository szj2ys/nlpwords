# *_*coding:utf-8 *_*
from os.path import join
from stopwds.paths import dirs


def stopwords(what='baidu', user_stopwds=None):
    '''
    return:: an iterator
    '''
    def read(file):
        with open(file, encoding='utf-8') as f:
            for item in f.readlines():
                yield item.strip()

    if what == 'baidu':
        return read(file=join(dirs.STOPWORDS, 'cn', 'baidu_stopwords.txt'))
    elif what == 'cn':
        return read(file=join(dirs.STOPWORDS, 'cn', 'cn_stopwords.txt'))
    elif what == 'hit':
        return read(file=join(dirs.STOPWORDS, 'cn', 'hit_stopwords.txt'))
    elif what == 'scu':
        return read(file=join(dirs.STOPWORDS, 'cn', 'scu_stopwords.txt'))
    else:
        return read(file=what)




