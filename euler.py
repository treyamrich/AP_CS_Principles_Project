from tkinter import *

def secondInterface():
    root2 = Toplevel()
    root2.title("Euler's Method Calculator")
    root2.geometry("400x400")
    root2.configure(background = "light blue")
    
    dydx = StringVar()
    stepSize = DoubleVar()
    initialx = IntVar()
    initialy = DoubleVar()
    desVal = DoubleVar()
    
    def eulers():
        #For exponents in the input
        equationList = []
        equation = ""
        
        for i in dydx.get():
            if i == "^":
                equationList.append("**")
            else:
                equationList.append(i)

        
        #Recombine the string and check for user var
        for j in equationList:
            equation += j
        #Calculate the amount of times the loop goes
        loopRange = (desVal.get() - initialx.get())/stepSize.get()
        loopRange = int(loopRange)
        x = initialx.get()
        y = initialy.get()
        for k in range(initialx.get(), loopRange):
            derivativeValue = eval(equation)
            y = y + (stepSize.get() * derivativeValue)
            
            x += stepSize.get()
        #For decent accurate answer use 3 decimal places
        y = round(y, 3)

        answer = Label(root2, text = "f(" + str(desVal.get()) + ") = " + str(y), bg = "light blue").place(x = 50, y = 240)
        
    #The Derivative Equation
    deriv0 = Label(root2, text = "Derivative Equation:", bg = "light blue").place(x = 50, y = 30)
    deriv1 = Entry(root2, textvariable=dydx).place(x = 100, y = 50)
    deriv2 = Label(root2, text = "dy/dx = ", bg = "light blue").place(x = 48, y = 50)
    #Delta x
    step0 = Label(root2, text = "Step size (dx):", bg = "light blue").place(x = 50, y = 70)
    step1 = Entry(root2, textvariable=stepSize).place(x = 80, y = 90, width = 50)
    step2 = Label(root2, text = "dx = ", bg = "light blue").place(x = 48, y = 90)
    #Starting point
    intial0 = Label(root2, text = "Initial Value:", bg = "light blue").place(x = 50, y = 110)
    initial1 = Entry(root2, textvariable=initialx).place(x = 62, y = 130, width = 25)
    initial2 = Label(root2, text = "f(", bg = "light blue").place(x = 48, y = 130)
    initial3 = Label(root2, text = ") = ", bg = "light blue").place(x = 80, y = 130)
    initial4 = Entry(root2, textvariable=initialy).place(x = 100, y = 130, width = 20)
    #Estimation value
    desireVal0 = Label(root2, text = "Ending Value (Ex: f(3):", bg = "light blue").place(x = 50, y = 150)
    desireVal1 = Entry(root2, textvariable=desVal).place(x = 62, y = 170, width = 25)
    desireVal2 = Label(root2, text = "f(", bg = "light blue").place(x = 48, y = 170)
    desireVal3 = Label(root2, text = ")", bg = "light blue").place(x = 85, y = 170)
    
    estimate0 = Button(root2, text = "Calculate", command = lambda:eulers(), bg = "royal blue").place(x = 50, y = 200)

    root2.mainloop()
