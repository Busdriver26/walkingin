print('{:*^80}'.format(" WALKING IN "))
print("AUTHOR: BU5DR1V3R , INSPIRED BY ULTRA GUO.")
print("Version -0.03, 2020/12/14")
print("Make sure that your pic is in the same folder of this .exe")

try:
    from PIL import Image, ImageDraw, ImageFont
except:
    print("There is no PIL found in your environment.Please install it first.")
    input("Press <enter>")
    quit()
import os,sys
try:
    import numpy as np
    from matplotlib import cm
    import matplotlib.pyplot as plt
except:
    print("There is no numpy or matplotlib found in your environment.Please install it first.")
    input("Press <enter>")
    quit()
from queue import Queue

max_row = 999
max_col = 999
q = Queue()
flag = np.full((1,3),0)
new_array = []
max_step = 0
output = np.full((1,3),0)

pt = os.path.dirname(sys.argv[0])
if pt!= '':
    os.chdir(os.path.dirname(sys.argv[0]))
os.getcwd()

pathLoad = input("Please input the name of your picture:(e.g. test.jpg, default:1.jpg)")
if len(pathLoad)<=4:
    pathLoad = "1.jpg"
try:
    img = Image.open(pathLoad).convert('RGB')
except:
    print("Wrong path.Try again!")
    input("Press <enter>")
    quit()
pathSave = input("Please input the name of the output picture:(e.g. out.jpg, default:1-out.jpg)")
if len(pathSave)<=4:
    pathSave = "1-out.jpg"
try:
    print("*When you see the picture is 1234X5678, the 5678 is ROW and 1234 is COL")
    rowEnterPoint = int(input("Please input the ROW enter point:(e.g.123,default:0)"))
    colEnterPoint = int(input("Please input the COLUMN enter point:(e.g.456,default:0)"))
except:
    rowEnterPoint = 0
    colEnterPoint = 0

def change(row,col,point):
    new_point = [(row,col),point,0]
    return new_point
    
def findEntry(array):
    global rowEnterPoint
    global colEnterPoint
    if array[rowEnterPoint][colEnterPoint][1] == [255,255,255]:
        print(array[rowEnterPoint][colEnterPoint])
        for row in array:
            for col in row:
                if col[1][0]!=[255,255,255]:
                    rowEnterPoint = col[0][0]
                    colEnterPoint = col[0][1]
                    return
        print("ERROR:ALL WHITE.")
        input("Press <enter>")
        quit()
    return

def inq(x,y,step):
    global q
    global flag
    global new_array
    global max_col
    global max_row
    global output
    if x<max_row and x>=0 and y<max_col and y>=0:
        if flag[x][y] == 0:
            flag[x][y] = 1
            if new_array[x][y][1] != [255,255,255]:
                new_array[x][y][2] = step + 1
                q.put(new_array[x][y])
    return

def walk():
    global q
    global flag
    global new_array
    global max_step
    ele = q.get()
    loc_x,loc_y = ele[0]
    step = ele[2]
    inq(loc_x+1,loc_y,step)
    inq(loc_x-1,loc_y,step)
    inq(loc_x,loc_y+1,step)
    inq(loc_x,loc_y-1,step)
    if step>max_step:
        max_step = step
    return
    
def main(pathLoad,pathSave):
    global flag
    global q
    global max_col
    global max_row
    global new_array
    global output
    global max_step
    img = Image.open(pathLoad).convert('RGB')
    array = np.array(img)
    array = array.tolist()
    while True:
        if array[rowEnterPoint][colEnterPoint] == [255,255,255]:
            print("You have chosen a white pixel,please try again.")
            input("Press <enter>")
            quit()
        else:
            break
    max_col = len(array[0])
    max_row = len(array)
    if rowEnterPoint<0 or rowEnterPoint>=max_row or colEnterPoint<0 or colEnterPoint>=max_col:
        print("row or col out of range, please check your input!")
        input("Press <enter>")
        quit()
    output = np.array(img)
    flag = np.full((max_row,max_col),0)
    for i in range(max_row):
        temp_row = []
        for j in range(max_col):
            temp_row.append(change(i,j,array[i][j]))
        new_array.append(temp_row)
    findEntry(new_array)
    q.put(new_array[rowEnterPoint][colEnterPoint])
    print("Drawing the route...")
    while not q.empty():
        walk()
    print("Drawing done. Now outputing pic.")
    cmap = cm.get_cmap('plasma')
    color = cmap([int(i/(max_step+1)*255) for i in range(max_step+1)])
    new_color = []
    for i in color:
        new_color.append([int(i[0]*255),int(i[1]*255),int(i[2]*255)])
    new_color = np.array(new_color)
    for i in range(max_row):
        for j in range(max_col):
            if output[i][j][0]!=255 and output[i][j][1]!=255 and output[i][j][2]!=255:
                output[i][j][0] = new_color[new_array[i][j][2]][0]
                output[i][j][1] = new_color[new_array[i][j][2]][1]
                output[i][j][2] = new_color[new_array[i][j][2]][2]
    img_tr = Image.fromarray(output).convert('RGB')
    img_tr.save(pathSave)
    print("done")
    input("Press <enter>")
    quit()
    return

main(pathLoad,pathSave)