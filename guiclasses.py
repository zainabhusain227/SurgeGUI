#import matplotlib.pyplot as plt
#import pydicom
#from matplotlib.widgets import Cursor
#from matplotlib.widgets import Button
import numpy as np

class Vessel:
  inside_marker=[]
  outside_marker=[]
  marker_count=0
  dataset=[]
  pov=[]
  slice=0
  sliderval=np.zeros(3,dtype=int)
  segment_arr=[]
  contourlist=[]

'''
class Index:
    ind = 0

    def reset(self, event):
        self.ind += 1
        vessel.marker_count=0

    def next(self, event):
        self.ind += 1
        #i = self.ind % len(freqs)
        #ydata = np.sin(2*np.pi*freqs[i]*t)
        #l.set_ydata(ydata)
        #plt.draw()

    def prev(self, event):
        self.ind -= 1
        #i = self.ind % len(freqs)
        #ydata = np.sin(2*np.pi*freqs[i]*t)
        #l.set_ydata(ydata)
        #plt.draw()'''


