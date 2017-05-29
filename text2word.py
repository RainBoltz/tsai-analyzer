# -*- coding: utf-8 -*-

import jieba
import logging
import argparse

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    parser = argparse.ArgumentParser(description='Segmenter for dumped wiki text.')
    parser.add_argument('-i', action='store', dest='input_path',help='input file path', required=True)
    parser.add_argument('-o', action='store', dest='output_path',help='output file path', required=True)
    parser.add_argument('--cores', type=int, help='core number for parallel processing', default=4)

    args = parser.parse_args()

    logging.info('loading stop words...')
    stopwordset = set()
    with open('jieba/stop_words.txt','r',encoding='utf-8') as sw:
        for line in sw:
            stopwordset.add(line.strip('\n'))

    output = open(args.output_path,'w')

    logging.info('start jieba chinese segmenter...')
    jieba.set_dictionary('jieba/dict.txt.big')
    jieba.load_userdict("jieba/dict.txt.user")

    #---------------------------
    jieba.add_word('蔡英文')
    jieba.add_word('小英')
    jieba.add_word('兩岸')
    jieba.add_word('两岸')
    jieba.add_word('兩岸關係')
    jieba.add_word('两岸关係')
    jieba.add_word('台獨')
    jieba.add_word('台独')
    jieba.add_word('臺獨')
    jieba.add_word('台灣獨立')
    jieba.add_word('臺灣獨立')
    jieba.add_word('台湾独立')
    jieba.add_word('民進黨')
    jieba.add_word('民进党')
    jieba.add_word('國民黨')
    jieba.add_word('国民党')
    jieba.add_word('共產黨')
    jieba.add_word('共产党')
    jieba.add_word('鄭又平')
    jieba.add_word('郑又平')
    jieba.add_word('一帶一路')
    jieba.add_word('一带一路')
    jieba.add_word('新南向')
    jieba.add_word('新南向政策')
    jieba.add_word('一中各表')
    jieba.add_word('一中原則')
    jieba.add_word('一中原则')
    jieba.add_word('台北大學')
    jieba.add_word('臺北大學')
    jieba.add_word('台北大学')
    jieba.add_word('九二共識')
    jieba.add_word('九二共识')
    jieba.add_word('國台辦')
    jieba.add_word('国台办')
    jieba.add_word('海基會')
    jieba.add_word('海基会')
    jieba.add_word('海協會')
    jieba.add_word('海协会')
    jieba.add_word('川普')
    jieba.add_word('川習會')
    jieba.add_word('川习会')
    jieba.add_word('特朗普')
    jieba.add_word('小英政府')
    jieba.add_word('英政府')
    jieba.add_word('一例一休')
    jieba.add_word('司法改革')
    jieba.add_word('年金改革')
    jieba.add_word('兩岸掮客')
    jieba.add_word('两岸掮客')
    #---------------------------

    jieba.enable_parallel(args.cores)
    texts_num = 0
    with open(args.input_path, 'r') as content :
        for line in content:
            words = jieba.cut(line, cut_all=False)
            for word in words:
                if word not in stopwordset:
                    output.write(word.lower() +' ')
            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("%d sentences segmented." % texts_num)
    output.close()
    
if __name__ == '__main__':
    main()
