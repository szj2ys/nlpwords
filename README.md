
<p align="center">
    <img width="200" src="https://github.com/szj2ys/stopwds/raw/master/stopwds/datasets/resources/logo.png"/>
</p>

<h3 align="center">
    <p>Frequent used words in NLP</p>
</h3>


<p align="center">
    <a href="https://python.org/pypi/stopwds">
        <img src="https://badge.fury.io/py/stopwds.svg" alt="Version"/>
    </a>
    <a href="https://python.org/pypi/stopwds">
        <img src="https://img.shields.io/pypi/l/stopwds.svg?color=orange" alt="License"/>
    </a>
    <a href="https://python.org/pypi/stopwds">
        <img src="https://img.shields.io/pypi/dm/stopwds?color=blue" alt="pypi downloads"/>
    </a>
    <a href="https://python.org/pypi/stopwds">
        <img src="https://img.shields.io/github/last-commit/szj2ys/stopwds?color=blue" alt="GitHub last commit"/>
    </a>
    <a href="https://github.com/szj2ys/stopwds">
        <img src="https://img.shields.io/github/stars/szj2ys/stopwds?style=social" alt="Stars"/>
    </a>
</p>

# Installation
```shell
pip install stopwds
```
you may want to checkout the version
```shell
stopwds version
```


# Usage

## stopwords
```python
from stopwds import stopwords

'''
baidu: 百度停用词表
hit: 哈工大停用词表
scu: 四川大学机器智能实验室停用词表
cn: 中文停用词表
'''
for stopword in stopwords('baidu'):
    print(stopword)
```

## Acknowlegements
*   stopwords
