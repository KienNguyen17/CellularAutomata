# Author: Kien Nguyen

import matplotlib.pyplot as plt
import matplotlib.animation as animation

HEIGHT = 60 # number of layers of the automata
WIDTH = HEIGHT*2+1

automata = []

def rule90(arr, index):
    '''apply rule 90 to the (index-1)-th row of arr, 
    generating index-th row and adding it to arr'''
    row = []
    for i in range(WIDTH):
        if index==0:
            if i==HEIGHT:
                row.append(1)
            else:
                row.append(0)
        else:
            left = arr[index-1][i - 1] if (i-1)>=0 else 0
            right = arr[index-1][i + 1] if (i+1)<WIDTH else 0 
            if left + right == 1:
                row.append(1)
            else:
                row.append(0)
    arr.append(row)

def getCoord(automata):
    '''take a 2d array representing a state of the automata
    return the corresponding coordinates for a visualization of the state'''
    x=[]
    y=[]
    for i in range(len(automata)):
        row = automata[i]
        if sum(row) > 0:
            for j in range(len(row)):
                item = row[j]
                if item == 1:
                    x.append(j)
                    y.append(HEIGHT-i)

    return x, y

def animate(i, automata=[]): 
    '''take an optional array, generate the i-th state of the automata
    to animate the gif'''
    rule90(automata, i)

    x,y = getCoord(automata)
    img = plt.scatter(x,y)
    
    return [img]

def generate(n, automata):
    '''given the number of layers in the array, 
    generate a scatter plot visualization of the automata'''
    for i in range(n):
        rule90(automata, i)

    x,y = getCoord(automata)
    img = plt.scatter(x,y)


def init():
    '''set up the plot and axes'''
    ax.clear()  
    ax.set_xticks([], [])  
    ax.set_yticks([], []) 

fig = plt.figure()
ax = plt.axes()

'''code to generate a gif animation of HEIGHT layers'''
# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=HEIGHT, interval=10, blit=False)
# anim.save("automata.gif")

'''code to generate an image of HEIGHT layers'''
generate(HEIGHT, automata)
plt.show()





