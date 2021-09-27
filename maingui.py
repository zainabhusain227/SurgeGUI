import matplotlib.pyplot as plt
import pydicom
#from matplotlib.widgets import Cursor
#from matplotlib.widgets import Button

from guiclasses import *
from panel1 import panel1
from tester import tester
#from selectview import selectview

#import napari   

#filename = "MATCH_anterior_left.dcm"
filename = "IM_0001.dcm"
print("Reading " + filename)
vessel=Vessel()
vessel.dataset = pydicom.dcmread(filename)
image_data=vessel.dataset.pixel_array
vessel.segment_arr=np.zeros(image_data.shape)
#plt.imshow(my_image_data[0],cmap='gray')
#plt.show()
# create a Viewer and add an image here
#viewer_1 = napari.view_image(my_image_data)
#viewer_2 = napari.view_image(my_image_data)
# custom code to add data here
#viewer.add_points(my_points_data)

# start the event loop and show the viewer
#napari.run()

panel1(vessel)
tester(vessel)
panel1(vessel)
#tester2(vessel)
#export3d(vessel)

