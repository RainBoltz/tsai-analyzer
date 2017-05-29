# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import IncrementalPCA
from gensim.models import word2vec
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager
    
def main():
    m = word2vec.Word2Vec.load(sys.argv[1])
    X = []
    words = []
    colors = []
    with open(sys.argv[2],'r') as f:
        for line in f:
            t = line.strip('\n').split(',')
            w = t[0]
            c = t[1]
            try:
                X.append(m[w])
                words.append(w)
                colors.append(c)
            except:
                continue
    
    samples = np.array(X)
    ipca = IncrementalPCA(n_components=3)
    ipca.fit(samples)        
    
    data = ipca.transform(X)
    xs = [i[0] for i in data]
    ys = [i[1] for i in data]
    zs = [i[2] for i in data]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs, ys, zs)
    
    chf = font_manager.FontProperties(fname='msjh.ttf', size='10')
    for i, txt in enumerate(words):
        ax.text(xs[i],ys[i],zs[i], txt, color=colors[i], fontproperties=chf)
    
    plt.show()
    
if __name__=='__main__':
    main()
