import matplotlib.pyplot as plt
import pydicom
from matplotlib.backend_bases import MouseButton
from matplotlib.widgets import Cursor
from matplotlib.widgets import Button,Slider

import numpy as np 
import sys


from skimage.draw import ellipse
from skimage.filters import gaussian, sobel
from skimage.segmentation import watershed
from skimage import measure
from guiclasses import *

def tester(vessel):

    def onclick(event,vessel,fig,ax):
        if event.button is MouseButton.RIGHT:
            print("right!")
            #when marker_count is reset to 0, the inside if statement runs first and then the outside
                # Only clicks inside this axis are valid.
            if event.inaxes != ax:
                return

            if vessel.marker_count==0: #and vessel.clear_screen==0:
                x = int(event.xdata)
                y = int(event.ydata)
                vessel.inside_marker=[x,y]
                print("inside ="+ str(x) + "," + str(y)) 
                vessel.iplot=ax.plot(x,y,'r+')
                fig.canvas.draw() #redraw the figure
                vessel.marker_count=1

            elif vessel.marker_count==1: #and vessel.clear_screen==0:
                x = int(event.xdata)
                y = int(event.ydata)
                vessel.outside_marker=[x,y]
                print("outside ="+ str(x) + "," + str(y)) 
                vessel.oplot=ax.plot(x,y,'c+')
                fig.canvas.draw() #redraw the figure
                vessel.marker_count=2

            '''elif vessel.marker_count==2: #and vessel.clear_screen==1:
                vessel.iplot[0].remove()
                vessel.oplot[0].remove()
                fig.canvas.draw()
                #vessel.clear_screen=0
                vessel.marker_count=0'''


    def on_press(event,vessel,fig,cursor):
        sys.stdout.flush()
        if event.key == 'space':
            print("dwe")
        if event.key == 'r':
            print("reset")
            if vessel.marker_count==2: #and vessel.clear_screen==1:
                vessel.iplot[0].remove()
                vessel.oplot[0].remove()
                print("removed")
                #fig.canvas.draw()
                #vessel.clear_screen=0
                vessel.marker_count=0






    def next(self, event):
        yi=9
        #vessel.marker_count=0

    class Index:
        ind = 0

        def reset(self, event):
            self.ind += 1
            vessel.clear_screen=1

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



    #vessel = Vessel()

    #filename = "MATCH_anterior_left.dcm"
    #dataset = pydicom.dcmread(filename)
    img_full = vessel.dataset.pixel_array
    if vessel.view==1:
        frame1=img_full[vessel.slice,:,:]
    elif vessel.view==2:
        frame1=img_full[:,vessel.slice,:]
    elif vessel.view==3:
        frame1=img_full[:,:,vessel.slice]
    #frame1=img_full[152,:,:]
    marker_count=0
    fig, ax = plt.subplots()
    ax.imshow(frame1,cmap='gray')
    fig.suptitle('Set Vessel Markers',fontsize=16)
    ax.set_title('First_Right_Click=Inside Second_Right_Click=Outside R=Reset',fontsize=12)


    # Defining the cursor
    cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True,
                    color = 'r', linewidth = 1)
    # Function for storing and showing the clicked values
    fig.canvas.mpl_connect('key_press_event', lambda event: on_press(event, vessel,fig,cursor))    
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

    #####################################
    # Create the image
    #####################################
    '''RS=5
    pad = 10 * RS
    img = np.zeros((28*RS + pad, 28*RS + pad), dtype=np.double)

    # fill ellipse
    rr, cc = ellipse(10*RS + int(pad/2), 14*RS  + int(pad/2), 6*RS, 10*RS, img.shape)
    img[rr, cc] = 1.0

    # fill ellipse
    rr, cc = ellipse(20*RS + int(pad/2), 14*RS + int(pad/2), 4.1*RS, 12*RS, img.shape)
    img[rr, cc] = 1.0'''


    img=frame1
    markers = np.zeros_like(img)
    #markers[14*RS,14*RS] = 2
    #swaped x and y coordinstes??
    markers[vessel.inside_marker[1],vessel.inside_marker[0]] =2
    markers[vessel.outside_marker[1],vessel.outside_marker[0]] =1
    #markers[1,1] = 1
    #print(markers)
    img = gaussian(img, 0.2)#*RS)
    # img = img + np.random.normal(scale=0.1, size=img.shape)

    #####################################
    # Get the image gradient
    #####################################
    img_g = gaussian(img, 1.0)# * RS)
    grad = sobel(img_g)
    grad_g = gaussian(grad, 1.0 )#* RS)

    improved_grad = grad - grad_g


    #####################################
    # Try just sharpening the image???
    #####################################
    amount = 1.0
    img_g_unsharp = amount*(img_g - gaussian(img_g, 0.2)) #* RS))

    grad_unsharp= sobel(img_g_unsharp)

    #####################################
    # Segment the image
    #####################################
    ground_truth = watershed(img, markers)
    grad_w = watershed(grad, markers)
    improved_grad_w = watershed(improved_grad, markers)

    improved_grad_w_unsharp = watershed(grad_unsharp, markers)


    fig, ax = plt.subplots()

    contours1 = measure.find_contours(grad_w, 1.5)
    vessel.contourlist= contours1
    print("***")
    print(vessel.contourlist)
    print("****")
    contours2 = measure.find_contours(improved_grad_w, 1.5)
    #print(contours2.shape)
    #print(contours2[0])
    #add watershed contour pixels to full matrix

    '''for contour in contours2:

        xcord=int(contour[0, 0])
        ycord=int(contour[1, 0])
        print(xcord)
        #figure out how to display it in color
        vessel.segment_arr[xcord,0,ycord]= 255'''
    contours3 = measure.find_contours(improved_grad_w_unsharp, 1.5)

    ax.imshow(img,cmap='gray')
    for contour in contours1:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2, label='Standard')
    for contour in contours2:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2, label='SURGE')
    for contour in contours3:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2, linestyle='--', label='Image sharpened')
    ax.legend()
    plt.show()