from tkinter import *
tableCells = [""]

def lRiemann(divisions):
    listLen = len(tableCells)
    total = 0
    
    if listLen - divisions == 1:
        for i in range(listLen):
            if i == listLen - 1:
                break
            h = i + 1
            base = tableCells[h].x.get() - tableCells[i].x.get()
            height = tableCells[i].y.get()
            subtotal = base * height
            total += subtotal
    #If Cell Number Is Odd
    elif listLen % 2 == 1:
        oddLen = int(listLen / divisions)
        h = 0
        for j in range(oddLen):
            j = h
            h = j + oddLen
            try:
                base = tableCells[h].x.get() - tableCells[j].x.get()
                height = tableCells[j].y.get()
                subtotal = base * height
                total += subtotal
            except:
                break
    #If Cell Number Is Even    
    else:
         evenLen = int(listLen / divisions)
         v = 0
         for u in range(divisions):
             u = v
             v = u + evenLen
             try:
                 base = tableCells[v-1].x.get() - tableCells[u].x.get()
                 height = tableCells[u].y.get()
                 subtotal = base * height
                 total += subtotal
             except:
                 break
    return total
    
def rRiemann(divisions):
    listLen = len(tableCells)
    total = 0
    
    if listLen - divisions == 1:
        for i in range(listLen):
            if i == listLen - 1:
                break
            h = i + 1
            base = tableCells[h].x.get() - tableCells[i].x.get()
            height = tableCells[h].y.get()
            subtotal = base * height
            total += subtotal
    #If Cell Number Is Odd
    elif listLen % 2 == 1:
        oddLen = int(listLen / divisions)
        h = 0
        for j in range(oddLen):
            j = h
            h = j + oddLen
            try:
                base = tableCells[h].x.get() - tableCells[j].x.get()
                height = tableCells[h].y.get()
                subtotal = base * height
                total += subtotal
            except:
                break
    #If Cell Number Is Even    
    else:
         evenLen = int(listLen / divisions)
         v = 0
         for u in range(divisions):
             u = v
             v = u + evenLen
             try:
                 base = tableCells[v-1].x.get() - tableCells[u].x.get()
                 height = tableCells[v-1].y.get()
                 subtotal = base * height
                 total += subtotal
             except:
                 break
    return total

def Midpoint(divisions):
    listLen = len(tableCells)
    total = 0
    a = 0
    midLen = int(listLen / divisions)
    for i in range(divisions):
        if i == listLen:
            break
        else:
            for j in range(divisions):
                if j > i:
                    break
                else:
                    try:
                        j = a
                        a = j + midLen
                        base = tableCells[a].x.get() - tableCells[j].x.get()
                        height = tableCells[a-1].y.get()
                        subtotal = base * height
                        total += subtotal
                    except:
                        break

    return total
    
def Trapezoid(divisions):
    listLen = len(tableCells)
    total = 0
    
    if listLen - divisions == 1:
        for i in range(listLen):
            if i == listLen - 1:
                break
            h = i + 1
            height = tableCells[h].x.get() - tableCells[i].x.get()
            bases = (tableCells[h].y.get() + tableCells[i].y.get()) / 2
            subtotal = bases * height
            total += subtotal
    #If Cell Number Is Odd
    elif listLen % 2 == 1:
        oddLen = int(listLen / divisions)
        h = 0
        for j in range(oddLen):
            j = h
            h = j + oddLen
            
            try:
                height = tableCells[h].x.get() - tableCells[j].x.get()
                bases = (tableCells[h].y.get() + tableCells[j].y.get()) / 2
                subtotal = bases * height
                total += subtotal
            except:
                break
    #If Cell Number Is Even    
    else:
         evenLen = int(listLen / divisions)
         v = 0
         for u in range(divisions):
             u = v
             v = u + evenLen
             try:
                 height = tableCells[v-1].x.get() - tableCells[u].x.get()
                 bases = (tableCells[v-1].y.get() + tableCells[u].y.get()) / 2
                 subtotal = bases * height
                 total += subtotal
             except:
                 break
    return total
