import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.widgets import TextBox


def f(x):
    return x**(3) - 0.165*(x**(2)) + 3.993*(10**(-4))


def bissection(xLower,xUpper,iteration):
    i = 0 #Accumulator
    xRootNew = 0
    xRoot = 0
    error = 100

    while i != iteration:
        xRootNew = (xLower+xUpper)/2
        #If f(xl)f(xm) < 0 root is on the left, then xu = xm
        if(f(xLower)*f(xRootNew) < 0):
            xUpper = xRootNew
        #If f(xl)f(xm) > 0 root is on the right, then xl = xm
        elif(f(xLower)*f(xRootNew) > 0):
            xLower = xRootNew
        #If f(xl)f(xm) = 0 root is xm

        #Error
        error = abs((xRootNew - xRoot)/xRootNew)*100
        xRoot = xRootNew
        i+=1
    print("Iteration =",i)
    print("X Upper =",xUpper)
    print("X Lower =",xLower)
    print("X Middle =",(xLower+xUpper)/2)
    print("Error =",error,"%")
    print("\n")
    return xUpper,xLower


# Initial values (default)
initial_function = "x**(3) - 0.165*(x**(2)) + 3.993*(10**(-4))"
initial_xUpper = 0.11
initial_xLower = 0
x = np.arange(initial_xLower-0.02,initial_xUpper+0.02,0.005)
y = f(x)
initial_iteration = 1

# Create plot and setting up the axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)
xUpper,xLower = bissection(initial_xLower,initial_xUpper,initial_iteration)
#function_x,function_y = generate_xy((initial_xLower-0.02),(initial_xUpper+0.02))
l, = plt.plot(x,y,color="blue")
plt.title("Bissection")
# Plot design
ax.set_xlim(((initial_xLower-0.02),(initial_xUpper+0.02)))
ax.set_xticks(np.arange((initial_xLower-0.02),(initial_xUpper+0.02),0.02))
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

# xUpper xLower and xMiddle
xUpperLine = ax.axvline(xUpper,color="Yellow")
xLowerLine = ax.axvline(xLower,color="Red")
xMiddleLine = ax.axvline((xLower+xUpper)/2,color="Orange")
# Text boxes
# Function
axbox = plt.axes([0.125, 0.05, 0.8, 0.0400]) #left bottom width height
text_box = TextBox(axbox, 'Function', initial=initial_function)
# X Lower
axbox2 = plt.axes([0.180,0.13,0.2,0.0400])
xLowerBox = TextBox(axbox2, 'Initial X Lower', initial=str(xLower))
# X Upper
axbox3 = plt.axes([0.600,0.13,0.2,0.0400])
xUpperBox = TextBox(axbox3, 'Initial X Upper', initial=str(xUpper))

# Slider
# Iteration count
axbox4 = plt.axes([0.125,0.21,0.3,0.0400])
iterSlider = Slider(axbox4, 'Iteration', 0 , 10 , valinit=initial_iteration-1 , valstep=1 )

# Update function
def updateFunction(text):
    ydata = eval(text)
    l.set_ydata(ydata)
    ax.set_ylim(np.min(ydata)-0.02, np.max(ydata)+0.02)
    plt.draw()

# Update iteration
def updateIteration(val):
    # Get values from the slider
    iteration = iterSlider.val
    # Remove existing xUpper xLower and xMiddle
    ax.lines[-1].remove()
    ax.lines[-1].remove()
    ax.lines[-1].remove()
    # Get updated xUpper xLower xMiddle
    xUpper,xLower = bissection(float(xLowerBox.text),float(xUpperBox.text),iteration)
    # Set the xUpper xLower xMiddle
    xUpperLine = ax.axvline(float(xUpper),color="Yellow")
    xLowerLine = ax.axvline(float(xLower),color="Red")
    xMiddleLine = ax.axvline((float(xLower)+float(xUpper))/2,color="Orange")
    plt.draw()

def updateXUpper(text):
    # Setup the x's
    xUpper = float(text)
    xLower = float(xLowerBox.text)
    iterSlider.set_val(0)

    # Remove existing xUpper xLower and xMiddle
    ax.lines[-1].remove()
    ax.lines[-1].remove()
    ax.lines[-1].remove()
    # New x's
    xUpperLine = ax.axvline(xUpper,color="Yellow")
    xLowerLine = ax.axvline(xLower,color="Red")
    xMiddleLine = ax.axvline((xLower+xUpper)/2,color="Orange")

def updateXLower(text):
    # Setup the x's
    xLower = float(text)
    xUpper = float(xUpperBox.text)
    iterSlider.set_val(0)

    # Remove existing xUpper xLower and xMiddle
    ax.lines[-1].remove()
    ax.lines[-1].remove()
    ax.lines[-1].remove()

    # New x;s
    xUpperLine = ax.axvline(xUpper,color="Yellow")
    xLowerLine = ax.axvline(xLower,color="Red")
    xMiddleLine = ax.axvline((xLower+xUpper)/2,color="Orange")

text_box.on_submit(updateFunction)
iterSlider.on_changed(updateIteration)
xUpperBox.on_submit(updateXUpper)
xLowerBox.on_submit(updateXLower)

plt.show()