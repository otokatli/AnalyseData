#import ctypes
#import struct
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10
mpl.rcParams['font.family'] = 'serif'

# matlab plot colors
mlColor = ([0, 0.4470, 0.7410], [0.8500, 0.3250, 0.0980], [ 0.9290, 0.6940, 0.1250], [0.4940, 0.1840, 0.5560], [0.4660, 0.6740, 0.1880], [0.3010, 0.7450, 0.9330], [0.6350, 0.0780, 0.1840])

# data file
fName = "data.hdata"

# custom data type
#myDT = np.dtype([("t", np.double), ("refDiceRot", np.double, (9,)), ("actDicePos", np.double, (3,)), ("actDiceRot", np.double, (9,)), ("devRot", np.double, (9,)), ("devPos", np.double, (3,)), ("devVel", np.double, (3,))])

with open(fName, "rb") as f:
	expData = np.fromfile(f, dtype=np.double)

# data
numData = int(len(expData)/37)
time               = np.array([expData[i*37] for i in range(0, numData)])
refDiceOrientation = np.array([np.asmatrix(expData[i*37+1:i*37+10]) for i in range(0, numData)])
actDicePos         = np.array([expData[i*37+10:i*37+13] for i in range(0, numData)])
actDiceOrientation = np.array([np.asmatrix(expData[i*37+13:i*37+22]) for i in range(0, numData)])
devOrientation     = np.array([np.asmatrix(expData[i*37+22:i*37+31]) for i in range(0, numData)])
devPos             = np.array([expData[i*37+31:i*37+34] for i in range(0, numData)])
devVel             = np.array([expData[i*37+34:i*37+37] for i in range(0, numData)])

# Device Position
with PdfPages("devicePosition.pdf") as pdf:
	fig1 = plt.figure(1)
	ax1 = fig1.gca(projection='3d')
	ax1.plot(devPos[:,0], devPos[:,1], devPos[:,2], color=mlColor[0])
	ax1.set_xlabel("x-axis")
	ax1.set_ylabel("y-axis")
	ax1.set_zlabel("z-axis")
	ax1.set_title("Position of the Device")
	pdf.savefig()

# Actual device position
with PdfPages("dicePosition.pdf") as pdf:
	fig2 = plt.figure(2)
	ax2 = fig2.gca(projection='3d')
	ax2.plot(actDicePos[:,0], actDicePos[:,1], actDicePos[:,2], color=mlColor[1])
	ax2.set_xlabel("x-axis")
	ax2.set_ylabel("y-axis")
	ax2.set_zlabel("z-axis")
	ax2.set_title("Position of the Dice")
	pdf.savefig()

# Show plots
plt.show()