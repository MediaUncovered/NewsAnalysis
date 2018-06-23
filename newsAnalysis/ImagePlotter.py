import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

class ImagePlotter:

    def __init__(self, show=False):
        self.show = show

    def createFigure(self):
        self.fig, self.ax = plt.subplots()

    def horizontalBarPlot(self, data, labels, title, x_label, path='fig.png'):
        self.createFigure()
        y_pos = np.arange(len(data))
        self.ax.barh(y_pos, data, align='center')
        self.ax.set_title(title)
        self.ax.set_xlabel(x_label)
        self.ax.set_yticks(y_pos)
        self.ax.set_yticklabels(labels)
        self.save(path)
        self.showFigure()


    def save(self, path):
        try:
            plt.savefig(path)
        except:
            print('Error ImagePlotter: Figure cannot be saved')

    def showFigure(self):
        if self.show:
            plt.show()


