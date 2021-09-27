import matplotlib.pyplot as plt
import pydicom
from matplotlib.widgets import Cursor
from matplotlib.widgets import Button


class Vessel:
  inside_marker=[]
  outside_marker=[]
  marker_count=0


def onclick(event,vessel,fig,ax):
    #when marker_count is reset to 0, the inside if statement runs first and then the outside
    if vessel.marker_count==1:
        x = int(event.xdata)
        y = int(event.ydata)
        vessel.outside_marker=[x,y]
        print("outside ="+ str(x) + "," + str(y)) 
        ax.plot(x,y,'c+')
        ax.axvline(x=int(event.xdata))
        ax.axhline(y=int(event.ydata))
        #plt.axvline(x=0.22058956)
        #plt.axvline(x=0.22058956)
        #plt.axvline(x=0.22058956)
        fig.canvas.draw() #redraw the figure
        vessel.marker_count=2
    
    if vessel.marker_count==0:
        x = int(event.xdata)
        y = int(event.ydata)
        vessel.inside_marker=[x,y]
        print("inside ="+ str(x) + "," + str(y)) 
        ax.plot(x,y,'r+')
        ax.axvline(x=int(event.xdata))
        ax.axhline(y=int(event.ydata))
        fig.canvas.draw() #redraw the figure
        vessel.marker_count=1

    



def next(self, event):
    yi=9
    #vessel.marker_count=0

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
        #plt.draw()



vessel = Vessel()

filename = "IM-0001-0256.dcm"
dataset = pydicom.dcmread(filename)
img_full = dataset.pixel_array
frame1=img_full[0,:,:]
marker_count=0
fig, ax = plt.subplots()
ax.imshow(frame1,cmap='gray')
fig.suptitle('Set Vessel Markers',fontsize=16)
ax.set_title('Inside=Red Outside=Blue',fontsize=12)


# Defining the cursor
cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True,
                color = 'r', linewidth = 1)
# Function for storing and showing the clicked values
#fig.canvas.mpl_connect('key_press_event', lambda event: on_press(event, flo))    
fig.canvas.mpl_connect('button_press_event', lambda event: onclick(event,vessel,fig,ax))


callback = Index()
axprev = plt.axes([0.81, 0.01, 0.1, 0.05])
axnext = plt.axes([0.7, 0.01, 0.1, 0.05])
axreset = plt.axes([0.9, 0.01, 0.1, 0.05])

breset = Button(axreset, 'Reset')
breset.on_clicked(callback.reset)

bnext = Button(axprev, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axnext, 'Previous')
bprev.on_clicked(callback.prev)

#bnext=Button(ax, 'Next')
#bnext.on_clicked(next)

plt.show()
plt.close()

