import sys
import numpy as np
import matplotlib.pyplot as plt

###  Synthesizing data to be plotted ###
x = np.arange(5)     # Same as x = np.array(range(5))
# y = x**2             # Basically item-wise calculation for numpy arrays

### Plotting Start ###
## Page Setup ##
fig = plt.figure()            # Define "figure" instance
fig.set_size_inches(8,6)    # Physical page size in inches, (lx,ly)
suptit = "Axes Setup: GridSpec"
fig.suptitle(suptit,fontsize=15)   # Title for the page

##-- Plotting for axis1 --##
import matplotlib.gridspec as gridspec
gs0 = gridspec.GridSpec(11,11)
gs0.update(left=0.1,right=0.95,bottom=0.1,top=0.88)

ax1 = plt.subplot(gs0[0:11,0:3])  # gs0[y0(top):y1(bottom),x0(left):x1(right)]
ax1.plot(x,x)
ax1.set_title("Panel#1",fontsize=12)

ax2 = plt.subplot(gs0[0:6,4:11])  # gs0[y0(top):y1(bottom),x0(left):x1(right)]
ax2.plot(x,x**0.5)
ax2.set_title("Panel#2",fontsize=12)

ax3 = plt.subplot(gs0[7:11,4:7])  # gs0[y0(top):y1(bottom),x0(left):x1(right)]
ax3.plot(x,x**1.5)
ax3.set_title("Panel#3",fontsize=12)

ax4 = plt.subplot(gs0[7:11,8:11])  # gs0[y0(top):y1(bottom),x0(left):x1(right)]
ax4.plot(x,x**2)
ax4.set_title("Panel#4",fontsize=12)

##-- Seeing or Saving Pic --##
#plt.show()   #- If want to see on screen -#
outdir = "../../data/"
outfnm = outdir+"02_axes_setup.subplot3.png"     # File format is decided by the file name, eg. png here
fig.savefig(outfnm,dpi=80,facecolor='0.9')   # dpi: pixels per inch
#fig.savefig(outfnm,dpi=80,bbox_inches='tight')   # dpi: pixels per inch

sys.exit()