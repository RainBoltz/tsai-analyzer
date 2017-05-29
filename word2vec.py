# -*- coding: utf-8 -*-

from gensim.models import word2vec
import os
import logging
import argparse

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    parser = argparse.ArgumentParser(description='Segmenter for dumped wiki text.')
    parser.add_argument('-i', action='store', dest='input_path',help='input file path', required=True)
    parser.add_argument('-o', action='store', dest='output_tag',help='output file tag (name= tag_dim_win.w2v)', required=True)
    parser.add_argument('--window', type=int, help='word2vec model window size', default=4)
    parser.add_argument('--size', type=int, help='word2vec model output dimension', default=200)
    parser.add_argument('--cores', type=int, help='core number for multiprocessing', default=4)

    args = parser.parse_args()
    
    logging.info('transforming Simplified Chinese -> Traditional Chinese...')
    os.system('opencc -i '+args.input_path+' -o '+args.input_path+'-zh -c s2twp.json')    

    logging.info('start training Word2Vec Model....')
    sentences = word2vec.Text8Corpus(args.input_path)
    model = word2vec.Word2Vec(sentences, size=args.size, window=args.window, workers=args.cores)

    model.save(args.output_tag+'_dim'+str(args.size)+'_win'+str(args.window)+'.w2vmodel')


if __name__ == "__main__":
    main()
