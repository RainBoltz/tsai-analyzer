# Tsai Analyzer

Only for Linux currently.
Chinese Wiki Analyzer, developed it just for a fun, so these are still dirty codes. 

### Python Requirements
  - numpy (with MKL)
  - gensim
  - scikit-learn
  - matplotlib
### other Requirements
  - opencc (system version, not python)

# Preprocess
1. download zh-wiki dumps from [here](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2). (all file named *-pages-articles.xml.bz2 is available)
2. dump out the wiki archive using [wiki2text.py](wiki2text.py)
3. segment the Chinese sentences into words by using [text2word.py](text2word.py) (you can add the words that MUST be segmented in the code)
4. transform simplified Chinese to traditional Chinese, lower the alphabets, then do word2vec. use [word2vec.py](word2vec.py)
5. Now you get a Trained zhWiki Word2Vec model!

# Usage
1. in the text file [anal](anal) (sorry for the imappropriate but that stands for ***anal***yze), you can add the words you want to find out in a 3-dimension space at each line, and the color for the word ( *format: [WORD],[COLOR]* ), then run [drawTsai.py](drawTsai.py)

2. if you want to find out the top-10 closest relation words for a word, you can run [drawGlobal.py](drawGlobal.py), and remember to add the words in [anal](anal)

License
----

MIT


