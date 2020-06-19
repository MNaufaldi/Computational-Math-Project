import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.widgets import TextBox


def f(x):
    return x**(3) - 0.165*(x**(2)) + 3.993*(10**(-4))

def fd(x):
    return 3*x**(2) - (2*0.165)*x

def newRaph(xInitial,iteration):
    i = 0
    error = 100
    while i != iteration:
        xInitial2 = xInitial - (f(xInitial)/fd(xInitial))
        error = abs((xInitial2 - xInitial)/xInitial2)*100
        xInitial = xInitial2
        i+=1
    print("Iteration =",i)
    print("Error =",error,"%")
    print("X Middle =",xInitial)
    print("\n")
    return xInitial

# Initial values (default)
plot_limitLowerX = -0.02
plot_limitUpperX = 0.12
initial_function = "x**(3) - 0.165*(x**(2)) + 3.993*(10**(-4))"
xInitial = 0.05
x = np.arange(plot_limitLowerX,plot_limitUpperX,0.005)
y = f(x)
initial_iteration = 1


# Create plot and setting up the axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)
xMiddle = newRaph(xInitial,initial_iteration)
l, = plt.plot(x,y,color="blue")
plt.title("Newton - Rhapson")
# Plot design
ax.set_xlim((plot_limitLowerX,plot_limitUpperX))
ax.set_xticks(np.arange(plot_limitLowerX,plot_limitUpperX,0.02))
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')


xMiddleLine = ax.axvline(xInitial,color="orange")
# Text boxes
# Function
axbox = plt.axes([0.125, 0.05, 0.8, 0.0400]) #left bottom width height
text_box = TextBox(axbox, 'Function', initial=initial_function)
# X Lower
axbox2 = plt.axes([0.180,0.13,0.2,0.0400])
xMiddleBox = TextBox(axbox2, 'Initial X guess', initial=str(xInitial))
# Slider
# Iteration count
axbox4 = plt.axes([0.125,0.21,0.3,0.0400])
iterSlider = Slider(axbox4, 'Iteration', 0 , 10 , valinit=initial_iteration-1 , valstep=1 )

# Update iteration
def updateIteration(val):
    # Get values from the slider
    iteration = iterSlider.val
    # Remove existing xMiddle
    ax.lines[-1].remove()
    # Get updated xMiddle
    xMiddle = newRaph(float(xMiddleBox.text),iteration)
    # Set the xMiddle
    xMiddleLine = ax.axvline((xMiddle),color="Orange")
    plt.draw()
def updateXMiddle(text):
    # Setup the x's
    xMiddle = float(text)
    iterSlider.set_val(0)

    # Remove existing xUpper xLower and xMiddle
    ax.lines[-1].remove()
    # New x's
    xMiddleLine = ax.axvline(xMiddle,color="Orange")


iterSlider.on_changed(updateIteration)
xMiddleBox.on_submit(updateXMiddle)
plt.show()