from matplotlib import widgets
import matplotlib.pyplot as plt
import pydicom
#from matplotlib.widgets import Cursor
from matplotlib.widgets import Button,Slider,CheckButtons,RadioButtons

import numpy as np 
from guiclasses import *
#import sys


#def next(self, event):
#vessel.marker_count=0


#vessel = Vessel()
#vessel.view=0
#filename = "MATCH_anterior_left.dcm"
#dataset = pydicom.dcmread(filename)
#img_full = dataset.pixel_array

def panel1(vessel):
    #figure out how to plot it with the colored plots
    img_full = vessel.dataset.pixel_array + vessel.segment_arr

    frame1=img_full[0,:,:]
    frame2=img_full[:,0,:]
    frame3=img_full[:,:,0]
    dim1=img_full.shape[0]-1
    dim2=img_full.shape[1]-1
    dim3=img_full.shape[2]-1

    #put this inside the checkbutton loop if statements
    dim=dim1
    fig, (ax, ax2,ax3) = plt.subplots(1,3)
    #fig.tight_layout(pad=0.1, w_pad=0.2, h_pad=0.5)
    fig.subplots_adjust(top=0.9, bottom=0.3, left=0.02, right=0.98, hspace=0.0, wspace=0.07)
    ax.axis('off')
    ax2.axis('off')
    ax3.axis('off')
    myobj=ax.imshow(frame1,cmap='gray')
    myobj2=ax2.imshow(frame2,cmap='gray')
    myobj3=ax3.imshow(frame3,cmap='gray')
    fig.suptitle('Choose Frame',fontsize=16)
    #ax.set_title('Select a View',fontsize=12)




    '''
    # Make checkbuttons with all plotted lines with correct visibility
    rax = plt.axes([0.05, 0.4, 0.1, 0.15])
    labels = ["dim1","dim2","dim3"]
    visibility = (True, False, False)
    check = RadioButtons(rax, labels,visibility)


    def func(label):
        if check.value_selected=="dim1":
            print("its 1")
            vessel.view=0
        elif check.value_selected=="dim2":
            print("its 2")
            vessel.view=1
        elif check.value_selected=="dim3":
            print("its 3")
            vessel.view=2
            #call update
    check.on_clicked(func)'''
    #button controlled slider changes
    def prev(event):
        vessel.sliderval[0]= vessel.sliderval[0] - 1
        update(vessel.sliderval[0])
        samp.set_val(vessel.sliderval[0])

    def next(event):
        vessel.sliderval[0]= vessel.sliderval[0] + 1
        update(vessel.sliderval[0])
        samp.set_val(vessel.sliderval[0])

    def prev2(event):
        vessel.sliderval[1]= vessel.sliderval[1] - 1
        update2(vessel.sliderval[1])
        samp2.set_val(vessel.sliderval[1])

    def next2(event):
        vessel.sliderval[1]= vessel.sliderval[1] + 1
        update2(vessel.sliderval[1])
        samp2.set_val(vessel.sliderval[1])

    def prev3(event):
        vessel.sliderval[2]= vessel.sliderval[2] - 1
        update3(vessel.sliderval[2])
        samp3.set_val(vessel.sliderval[2])

    def next3(event):
        vessel.sliderval[2]= vessel.sliderval[2] + 1
        update3(vessel.sliderval[2])
        samp3.set_val(vessel.sliderval[2])

    # .axes(offset from left, verctical placement, horizontal thickness, vertical thickness)
    axamp  = plt.axes([0.1, 0.25, 0.65, 0.03])
    axamp2  = plt.axes([0.1, 0.15, 0.65, 0.03])
    axamp3  = plt.axes([0.1, 0.05, 0.65, 0.03])
    samp = Slider(axamp, 'Slice', 1, dim, valinit=0,valstep=1,color="purple")
    samp2 = Slider(axamp2, 'Slice', 1, dim, valinit=0,valstep=1,color="red")
    samp3 = Slider(axamp3, 'Slice', 1, dim, valinit=0,valstep=1,color="blue")

    #slider 1 buttons
    axprev = plt.axes([0.80, 0.25, 0.05, 0.03])
    axnext = plt.axes([0.86, 0.25, 0.05, 0.03])

    bprev= Button(axprev, 'Prev')
    bprev.on_clicked(prev)
    bnext= Button(axnext, 'Next')
    bnext.on_clicked(next)

    #slider 2 buttons
    axprev2 = plt.axes([0.80, 0.15, 0.05, 0.03])
    axnext2 = plt.axes([0.86, 0.15, 0.05, 0.03])

    bprev2= Button(axprev2, 'Prev')
    bprev2.on_clicked(prev2)
    bnext2= Button(axnext2, 'Next')
    bnext2.on_clicked(next2)

    #slider 3 buttons
    axprev3 = plt.axes([0.80, 0.05, 0.05, 0.03])
    axnext3 = plt.axes([0.86, 0.05, 0.05, 0.03])

    bprev3= Button(axprev3, 'Prev')
    bprev3.on_clicked(prev3)
    bnext3= Button(axnext3, 'Next')
    bnext3.on_clicked(next3)

    def update(val):
        print(val)
        vessel.sliderval[0]=val
        vessel.view=1
        vessel.slice=val
        frame1=img_full[val,:,:]
        myobj.set_data(frame1)

        #fig.canvas.draw_idle()

    def update2(val):
        print(val)
        vessel.sliderval[1]=val
        vessel.view=2
        vessel.slice=val
        frame2=img_full[:,val,:]
        myobj2.set_data(frame2)
        print(vessel.contourlist)
        for contour in vessel.contourlist:
            ax2.plot(contour[:, 1], contour[:, 0], linewidth=2, label='Standard')
        #fig.canvas.draw_idle()

    def update3(val):
        print(val)
        vessel.sliderval[2]=val
        vessel.view=3
        vessel.slice=val
        frame3=img_full[:,:,val]
        myobj3.set_data(frame3)
        #fig.canvas.draw_idle()

    samp.on_changed(update)
    samp2.on_changed(update2)
    samp3.on_changed(update3)
    plt.show()
    plt.close()
    print("***")
    print(vessel.view)
    print(vessel.slice)
