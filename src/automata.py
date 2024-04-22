import matplotlib.pyplot as plt
import matplotlib.animation as animation

def rule90(arr, index):
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

def animate(i, automata): 
    rule90(automata, i)

    x,y = getCoord(automata)
    img = plt.scatter(x,y)
    
    return [img]

def generate(n, automata):
    for i in range(n):
        rule90(automata, i)

    x,y = getCoord(automata)
    img = plt.scatter(x,y)


def init():
    ax.clear()  
    ax.set_xticks([], [])  
    ax.set_yticks([], []) 

HEIGHT = 16
WIDTH = HEIGHT*2+1

automata = []

fig = plt.figure()
ax = plt.axes()

# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=HEIGHT, interval=10, blit=False)
# anim.save("automata.gif")
generate(HEIGHT, automata)
plt.show()





