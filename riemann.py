from tkinter import *
import riemann2 as r
def thirdInterface():
    
    #Set Window Dimensions/Asthetics
    root3 = Toplevel()
    root3.title("Riemann Sum Calculator")
    root3.geometry("600x350")
    root3.configure(background = "pink")

    divAmount = IntVar()
    #Create Drop Down Menu
    options = ["Left Riemann Sum", "Right Riemann Sum", "Mid Point Approximation", "Trapezoid Approximation"]
    chooseOp = StringVar(root3)
    chooseOp.set(options[0])

    #Creating Table Cells Function
    class tableCell():
        def __init__(self, value):
            self.value = value
            self.x = IntVar()
            self.y = IntVar()
            self.cell0 = Entry(root3, textvariable = self.x, font = "Verdana 12").place(x = self.value, y = 30, width = 30, height = 30)
            self.cell1 = Entry(root3, textvariable = self.y, font = "Verdana 12").place(x = self.value, y = 65, width = 30, height = 30)
        def add(self):
            self.value += 35
            
    #Makes Sure Every Cell Added Is Spaced Out
    def createTable():
        if r.tableCells[0] == "":
            r.tableCells[0] = tableCell(85)
            r.tableCells[0].add()
        elif r.tableCells[0] != "":
            r.tableCells.append(tableCell(r.tableCells[-1].value))
            r.tableCells[-1].add()

    #Choose Which Approximation Method
    def chooseEstim():
        if chooseOp.get() == "Left Riemann Sum":
            ans = Label(root3, text = "Answer: " + str(r.lRiemann(divAmount.get())), bg = "hot pink").place(x = 305, y = 250)
        elif chooseOp.get() == "Right Riemann Sum":
            ans = Label(root3, text = "Answer: " + str(r.rRiemann(divAmount.get())), bg = "hot pink").place(x = 305, y = 250)
        elif chooseOp.get() == "Mid Point Approximation":
            ans = Label(root3, text = "Answer: " + str(r.Midpoint(divAmount.get())), bg = "hot pink").place(x = 305, y = 250)
        elif chooseOp.get() == "Trapezoid Approximation":
            ans = Label(root3, text = "Answer: " + str(r.Trapezoid(divAmount.get())), bg = "hot pink").place(x = 305, y = 250)
    
    table0 = Label(root3, text = "x", bg = "pink", font = "Verdana 20").place(x = 50, y = 25)
    table1 = Label(root3, text = "y", bg = "pink", font = "Verdana 20").place(x = 50, y = 60)
    table2 = Label(root3, text = "Amount of Subdivisions:", bg = "pink").place(x = 50, y = 170, height = 35)
    table3 = Entry(root3, textvariable = divAmount).place(x = 190, y = 175, width = 20, height = 25)
    #Add Table Cell Button And First Two Cells
    table4 = Button(root3, text = "Add Table Cells", command = lambda: createTable(), bg = "hot pink").place(x = 50, y = 140)
    #Drop Down Menu
    dropDown = OptionMenu(root3, chooseOp, *options)
    dropDown.config(activebackground = "hot pink", bg = "light pink")
    dropDown["menu"].config( bg = "hot pink")
    dropDown.place(x = 50, y = 220)
    #Drop Down Button
    dropDown1 = Button(root3, text = "Calculate", command = chooseEstim, bg = "hot pink").place(x = 50, y = 270)
    root3.mainloop()
    

