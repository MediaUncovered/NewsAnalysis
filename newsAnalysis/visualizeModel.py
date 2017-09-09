from sklearn.manifold import TSNE
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import pdb

def visualizeModel():

    path = 'models/w2v_10000'
    word2vec = Word2Vec.load(path)

    vectors = word2vec[word2vec.wv.vocab]
    vectors = vectors[:1000,:]

    tsne = TSNE(n_components=2)
    X_tsne = tsne.fit_transform(vectors)

    plt.scatter(X_tsne[:,0], X_tsne[:,1])
    plt.show()




    pdb.set_trace()


if __name__=='__main__':
    visualizeModel()
