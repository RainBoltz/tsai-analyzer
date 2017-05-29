# -*- coding: utf-8 -*-

import logging
import argparse
from gensim.corpora import WikiCorpus

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    parser = argparse.ArgumentParser(description='Segmenter for dumped wiki text.')
    parser.add_argument('-i', action='store', dest='input_path',help='input file path (wiki-pages-articles.xml.bz2)', required=True)
    parser.add_argument('-o', action='store', dest='output_path',help='output file path', required=True)

    args = parser.parse_args()

    logging.info('reading wiki corpus: '+args.input_path+' ...')
    wiki_corpus = WikiCorpus(args.input_path, dictionary={})

    texts_num = 0
    
    logging.info('start parsing articles ...')  
    with open(args.output_path,'w',encoding='utf-8') as output:
        for text in wiki_corpus.get_texts():
            output.write(b' '.join(text).decode('utf-8') + '\n')
            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("%d articles parsed." % texts_num)
if __name__ == "__main__":
    main()
