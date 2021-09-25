from tkinter import *
import euler as e
import riemann as r

root = Tk()
root.title("Calculus Tools")
root.configure(background = "light green")
#Create Window Size
width = 650
height = 400
#Find Center of Screen
sWidth = root.winfo_screenwidth()
sHeight = root.winfo_screenheight()
x = (sWidth/2) - (width/2)
y = (sHeight/2) - (height/2)
#Create Window In Center 
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

def About():
    about = Tk()
    about.title("About")
    a = Label(about, text = "This is a cool program").place(x = 0, y = 0)
    about.mainloop()


#Menu
menu = Menu(root)
root.config(menu=menu)
#Exit0
exit0Menu = Menu(menu)
menu.add_cascade(label = "File", menu=exit0Menu)
exit0Menu.add_separator()
exit0Menu.add_command(label="Exit", command=root.destroy)
#Help
helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About...", command=About)

#Euler's Method Window
def eulerInterface():
    e.secondInterface()
#Riemann Sum Window
def riemannInterface():
    r.thirdInterface()
#Hub or Main Window
def mainInterface():
    
    #Buttons for openning new windows
    euler = Button(root, text = "Euler's Method For Estimating Points",command = lambda:eulerInterface(), fg = "white", bg = "black")
    euler.place(x = 200, y = 50, width = 250, height = 100)
    rRie = Button(root, text = "Riemann Sum", command = lambda:riemannInterface(),fg = "white", bg = "black")
    rRie.place(x = 200, y = 250, width = 250, height = 100)
 
    root.mainloop()
    
mainInterface()
