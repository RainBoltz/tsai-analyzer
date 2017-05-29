# -*- coding: UTF-8 -*-

import json
import requests
import time
import logging
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from sys import argv

def main():
    crawler = PttCrawler()
    crawler.crawl(start=int(argv[1]), end=int(argv[2]))

class PttCrawler(object):

    root = "https://www.ptt.cc/bbs/"
    main = "https://www.ptt.cc"
    gossip_data = {
        "from":"bbs/Gossiping/index.html",
        "yes": "yes"
    }

    def __init__(self):
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

        self.session = requests.session()
        requests.packages.urllib3.disable_warnings()
        self.session.post("https://www.ptt.cc/ask/over18",
                           verify=False,
                           data=self.gossip_data)

    def articles(self, page):

        res  = self.session.get(page,verify=False)
        soup = BeautifulSoup(res.text, "lxml")

        for article in soup.select(".r-ent"):
            try:
                yield self.main + article.select(".title")[0].select("a")[0].get("href")
            except:
                pass # (本文已被刪除)

    def pages(self, board=None, index_range=None, output_dir="result/"):

        target_page = self.root + board + "/index"

        if range is None:
            yield target_page + ".html"
        else:
            for index in index_range:
                yield target_page + str(index) + ".html"

    def parse_article(self, url):

        raw  = self.session.get(url, verify=False)
        soup = BeautifulSoup(raw.text, "lxml")

        try:
            article = {}

            article["Author"] = soup.select(".article-meta-value")[0].contents[0].split(" ")[0]
            article["Title"]  = soup.select(".article-meta-value")[2].contents[0]

            content = ""
            for tag in soup.select("#main-content")[0]:
                if type(tag) is NavigableString and tag !='\n':
                    content += tag
                    break
            article["Content"] = content

            upvote = 0
            downvote = 0
            novote = 0
            response_list = []

            for response_struct in soup.select(".push"):

                if "warning-box" not in response_struct['class']:

                    response_dic = {}
                    response_dic["Content"] = response_struct.select(".push-content")[0].contents[0][1:]
                    response_dic["Vote"]  = response_struct.select(".push-tag")[0].contents[0][0]
                    response_dic["User"]  = response_struct.select(".push-userid")[0].contents[0]
                    response_list.append(response_dic)

                    if response_dic["Vote"] == u"推":
                        upvote += 1
                    elif response_dic["Vote"] == u"噓":
                        downvote += 1
                    else:
                        novote += 1

            article["Responses"] = response_list
            article["UpVote"] = upvote
            article["DownVote"] = downvote
            article["NoVote"] = novote

        except Exception as e:
            print(e)
            print(u"error when analyzing %s !" % url)

        return article

    def output(self, filename, data):

        with open("ptt/"+filename+".json", 'wb') as op:
            op.write(json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8'))

    def crawl(self, board="Gossiping", start=1, end=2, sleep_time=0.01):

        crawl_range = range(start, end+1)


        for page in self.pages(board, crawl_range):
            res = []
            for article in self.articles(page):
                res.append(self.parse_article(article))
                #time.sleep(sleep_time)
            self.output(board + str(start), res)

            logging.info(u"crawled %s - page#%d ." %(board,start))
            start += 1


if __name__ == '__main__':
    main()
