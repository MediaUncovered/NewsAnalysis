from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pygal


def createWordCloud(wordList):
    wordcloud = WordCloud(max_font_size=100)
    wordcloud.fit_words(wordList)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


def createHorzBarPlot(X1,X2,labels,name):
    chart = pygal.HorizontalBar()
    chart.add(X1[0], X1[1])
    chart.add(X2[0], X2[1])
    chart.x_labels = labels
    chart.render_to_file('plots/'+name+'.svg')


def annotatedScatterPlot(xVec,yVec,keywords,title,xlabel,ylabel):
    fig,ax = plt.subplots()
    ax.scatter(xVec, yVec)
    for ind,word in enumerate(keywords):
        ax.annotate(word, (xVec[ind], yVec[ind]))
    plt.title(title)
    plt.set_xlabel(xlabel)
    plt.set_ylabel(ylabel)
    plt.show()
