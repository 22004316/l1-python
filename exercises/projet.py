import tkinter as tk
import random as rd
import tkinter.font as tkF

#coucou

root_1 = tk.Tk()
root_1.title("Calculator")

fontStyle = tkF.Font(family="Sergeo UI Semilight", size=200)

pi = 3.14159265358979
digit = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9, pi]                                                             #define digit list
op = ["+", ":", "*", "|", "=", "-", "^", "(", ")"]                                                      #define operator list
listNum = []
listOp = []
numRank = 0
opRank = 0
rank = 0
display = ["0"]
aa = 0
bb = 0
indexStart = 0
indexStop = 0

def number(ipt):                                                                                        #defines function which adds inputed numbers into a list named display at position [rank]
    global display, rank, opRank, numRank, listOp, listNum, aa, i, indexStart, indexStop, num
    num = str(ipt)

    listNum.append(str())
    listNum [numRank] = listNum [numRank] + num
    display [rank] = listNum [numRank]
    print (display)
    button_result ['text'] = display

def Sqrt(op, num):
    global display, rank, opRank, numRank, listOp, listNum, aa, i, indexStart, indexStop
    if display [-1] == '9':
        listNum = []
        listOp = []
        numRank = 0
        opRank = 0
        rank = 0
        display = ["0"]
        aa = 0
        display [0] = 'π'
        button_result ['text'] = display
        display = ["0"]
    else:
        operator(op)
        number(num)
        
def operator(ipu):#defines function which adds inputed operators into display at position [rank]; increments rank
    global display, rank, opRank, numRank, listOp, listNum, aa, i, indexStart, indexStop

    listOp.append(ipu)
    rank += 1
    display.append(str())
    print (display , "3")

    display [rank] = listOp [opRank]
    print (display , "4")

    if ipu == ")":
        rank += -1
        
    if ipu != ")":
        display.append(str())

    if ipu == "(" and (display [rank - 1] == "0" or display [rank - 1] == ""):
        del display [rank - 1]
        print ('aaaaaaaaaaaaaaaaaaaaaaaaa')
        rank += -1

    numRank += 1
    opRank +=1
    rank +=1
    if ipu == "(" and display [rank - 2] in digit:
        rank += -1
        print (rank)
        del display [0]
    button_result ['text'] = display

    listNum.append(str())
    print (display, "5")

def Delete():
    global display, rank, opRank, numRank, listOp, listNum, aa, i, indexStart, indexStop
    del listNum [numRank]
    del display [rank]
    button_result ['text'] = display
    display.append(str())
    listNum.append(str())
    print (display, "6")

def AC():
    global display, rank, opRank, numRank, listOp, listNum, aa, i, indexStart, indexStop
    listNum = []
    listOp = []
    numRank = 0
    opRank = 0
    rank = 0
    display = ["0"]
    aa = 0
    listNum = []
    i = 0
    button_result ['text'] = display

def equal():
    global display, rank, opRank, numRank, listOp, listNum, aa, i, indexStart, indexStop
    le = len(display)
    i = 0
    for j in range (0, le):
        indexStart = 0
        indexStop = len(display)
        if display [j] == '(':
            indexStart = j
        if display [j] == ')':
            indexStop = j

    for j in range (indexStart, indexStop):
        if display [j - 2] == "(":
            if display [j] in op:

                if display [j] == "+":
                    aa = float(display [j-1]) + float(display [j + 1]) 

                elif display [j] == '-':
                    aa = float(display [j-1]) - float(display [j + 1])

                elif display [j] == '*':
                    aa = float(display [j-1]) * float(display [j + 1])

                elif display [j] == ':':
                    aa = float(display [j-1]) / float(display [j + 1]) 
                
                elif display [j] == '^':
                    aa = float(display [j-1]) ** float(display [j + 1]) 
                print (display, "a")
                print (aa)
                j += 1
                display [j - 2] = str(aa)
                display [j - 1] = ""
                display [j] = ""
                print (display, "aa")


    i = 0
    for i in range (0,(le-3)):
        if display [i] == '' or display [i] == ')':
            del display [i]
            print (display, "fck")
    le = len (display)
    i = 0
    for i in range (0,(le-3)):
        if display [i] == '' or display [i] == '(':
            del display [i]
            print (display, "fck")
        
    nle = len(display)
    i = 0
    for i in range (0,nle-2):
        if i not in op:
            print (display, "yes")

            if display[i+2] == "(":
                add = 3
            else:
                add = 2

            if display [i + 1] == "+":
                aa = float(display [i]) + float(display [i + add]) 

            elif display [i + 1] == '-':
                    
                    aa = float(display [i]) - float(display [i + add])

            elif display [i + 1] == '*':
                    aa = float(display [i]) * float(display [i + add])

            elif display [i + 1] == ':':
                    aa = float(display [i]) / float(display [i + add]) 
            
            elif display [i + 1] == '^':
                    aa = float(display [i]) ** float(display [i + add]) 
        display [i] = str(aa)

    acc = round((len(display [i])+len(display [(i + add)]))/2)
    button_result ['text'] = round(aa, acc)
    listNum = []
    listOp = []
    numRank = 0
    opRank = 0
    rank = 0
    display = ["0"]
    aa = 0

def autoDestruct():
    root_1.destroy()

def none() :
    pass

button_result = tk.Label(root_1, text= '0', font=(10), bg = 'gainsboro')
button_7 = tk.Button(root_1, text='7', font=(10), command = lambda : number(7))
button_8 = tk.Button(root_1, text='8', font=(10), command = lambda : number(8))
button_9 = tk.Button(root_1, text='9', font=(10), command = lambda : number(9))
button_Plus = tk.Button(root_1, text='+', font=(10), command = lambda : operator('+'))
button_4 = tk.Button(root_1, text='4', font=(10), command = lambda : number(4))
button_5 = tk.Button(root_1, text='5', font=(10), command = lambda : number(5))
button_6 = tk.Button(root_1, text='6', font=(10), command = lambda : number(6))
button_Minus = tk.Button(root_1, text='- ', font=(10), command = lambda : operator('-'))
button_1 = tk.Button(root_1, text='1', font=(10), command = lambda : number(1))
button_2 = tk.Button(root_1, text='2', font=(10), command = lambda : number(2))
button_3 = tk.Button(root_1, text='3', font=(10), command = lambda : number(3))
button_Div = tk.Button(root_1, text=':  ', font=(10), command = lambda : operator(':'))
button_Mult = tk.Button(root_1, text='*', font=(10), command = lambda : operator('*'))
button_0 = tk.Button(root_1, text='0', font=(10), command = lambda : number(0))
button_Dot = tk.Button(root_1, text='.', font=(10), command = lambda : number("."))
button_Equal = tk.Button(root_1, text='=', font=(10), command = equal)
button_Del = tk.Button(root_1, text='←', font = 10, command = Delete)
button_AC = tk.Button(root_1, text='AC', font = 10, command = AC)
button_Pow = tk.Button(root_1, text='^', font = 10, command = lambda : operator('^'))
button_DivE = tk.Button(root_1, text='☠', font = 'segoe' , command = autoDestruct, bg = "red")
button_LBracket = tk.Button(root_1, text='(', font = 10 , command = lambda : operator('('))
button_RBracket = tk.Button(root_1, text=')', font = 10 , command = lambda : operator(')'))
button_switch2Graph = tk.Button(root_1 , text='Gph', )
button_Pi = tk.Button(root_1, text='π', font=(10), command = lambda : number(pi))
button_Sqrt = tk.Button(root_1, text='√', font = 10, command = lambda : Sqrt('^', '0.5'))


button_result.grid(column = 0, row = 0, columnspan = 5, ipadx = 281, ipady = 40, sticky='nesw')
button_7.grid(row = 1, column =0, ipadx = 50, ipady = 50, sticky='nesw')
button_8.grid(row = 1, column = 1, ipadx = 50, ipady = 50, sticky='nesw')
button_9.grid(row = 1, column = 2, ipadx = 50, ipady = 50, sticky='nesw')
button_Del.grid(row = 1, column = 3, ipadx = 50, ipady = 50, sticky='nesw')
button_AC.grid(row = 1, column = 4, ipadx = 50, ipady = 50, sticky='nesw')
button_4.grid(row = 2, column = 0, ipadx = 50, ipady = 50, sticky='nesw')
button_5.grid(row = 2, column = 1, ipadx = 50, ipady = 50, sticky='nesw')
button_6.grid(row = 2, column = 2, ipadx = 50, ipady = 50, sticky='nesw')
button_Mult.grid(row = 2, column = 3, ipadx = 50, ipady = 50, sticky='nesw')
button_Div.grid(row = 2, column = 4, ipadx = 50, ipady = 50, sticky='nesw')
button_1.grid(row = 3, column = 0, ipadx = 50, ipady = 50, sticky='nesw')
button_2.grid(row = 3, column = 1, ipadx = 50, ipady = 50, sticky='nesw')
button_3.grid(row = 3, column = 2, ipadx = 50, ipady = 50, sticky='nesw')
button_Plus.grid(row = 3, column = 3, ipadx = 50, ipady = 50, sticky='nesw')
button_Minus.grid(row = 3, column = 4, ipadx = 50, ipady = 50, sticky='nesw')
button_0.grid(row = 4, column = 0, ipadx = 50, ipady = 50, sticky='nesw')
button_Dot.grid(row = 4, column = 1, ipadx = 50, ipady = 50, sticky='nesw')
button_Pow.grid(row = 4, column = 2, ipadx = 50, ipady = 50, sticky='nesw')
button_DivE.grid(row = 4, column = 3, ipadx = 50, ipady = 50, sticky='nesw')
button_Sqrt.grid(row = 4, column = 4, ipadx = 50, ipady = 50, sticky='nesw')
button_LBracket.grid(row = 5, column = 0, ipadx = 50, ipady = 50, sticky='nesw')
button_RBracket.grid(row = 5, column = 1, ipadx = 50, ipady = 50, sticky='nesw')
button_switch2Graph.grid(row = 5, column = 2, ipadx = 50, ipady = 50, sticky='nesw')
button_Pi.grid(row = 5, column = 3, ipadx = 50, ipady = 50, sticky='nesw')
button_Equal.grid(row = 5, column = 4, ipadx = 50, ipady = 50, sticky='nesw')

root_1.mainloop()
