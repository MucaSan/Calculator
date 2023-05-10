import tkinter as tk

# set the root
root = tk.Tk()
root.title('calculator')
label = tk.Label(width = 24 , height = 3, bg = 'gray')
label.pack()
## frame to map all the buttons
frame = tk.Frame(root)
frame.pack()

## display nums into the screen, and keeping the current the string had before
def display_num(element):
    global label
    current = label.cget('text')
    label.config(text= current + str(element))

def multiply(num1, num2):
    return num1 * num2
def sum (num1, num2):
    return (num1 + num2)
def minus(num1, num2):
    return (num1 - num2)
def divide(num1, num2):
    return (num1/num2)

def clear():
    global label
    label.config(text="")

def comput_result():
    global label
    arr_alphanum = []
    arr_symbols = []

    for j in range(len(label.cget("text"))):
        if label.cget("text")[j].isalnum() == False:
            arr_symbols.append(label.cget("text")[j])
        else:
            arr_alphanum.append(label.cget('text')[j])
    if len(arr_alphanum) <= len(arr_symbols):
        label.config(text='SYNTAX ERROR')
    else:
        for i in range(len(label.cget("text"))):
            if label.cget("text")[i].isalnum() == False:
                num1 = int(label.cget("text")[0:i])
                print(num1)
                num2 = int(label.cget("text")[i+1:])
                print(num2)
                if label.cget("text")[i] =='+' :
                    label.config(text=str(sum(num1, num2)))
                    print('Sum')
                elif label.cget("text")[i] =='-' :
                    label.config(text=str(minus(num1, num2)))
                    print('Minus')
                elif label.cget("text")[i] =='*' :
                    print('Multiply')
                    label.config(text=str(multiply(num1, num2)))
                else:
                    label.config(text=str(divide(num1, num2)))
                    print('Divide')


def init_numbers_grid():
    button0 = tk.Button(frame, text= 0 , width=7, height = 3, command = lambda: display_num(0))
    button0.grid(row= 1, column=0)
    button1 = tk.Button(frame, text= 1 , width=7, height = 3, command = lambda: display_num(1))
    button1.grid(row= 1, column=1)
    button2 = tk.Button(frame, text= 2 , width=7, height = 3, command = lambda: display_num(2))
    button2.grid(row= 1, column=2)
    button3 = tk.Button(frame, text= 3 , width=7, height = 3, command = lambda: display_num(3))
    button3.grid(row= 2, column=0)
    button4 = tk.Button(frame, text= 4 , width=7, height = 3, command = lambda: display_num(4))
    button4.grid(row= 2, column=1)
    button5 = tk.Button(frame, text= 5 , width=7, height = 3, command = lambda: display_num(5))
    button5.grid(row= 2, column=2)
    button6 = tk.Button(frame, text= 6 , width=7, height = 3, command = lambda: display_num(6))
    button6.grid(row= 3, column=0)
    button7 = tk.Button(frame, text= 7 , width=7, height = 3, command = lambda: display_num(7))
    button7.grid(row= 3, column=1)
    button8 = tk.Button(frame, text= 8 , width=7, height = 3, command = lambda: display_num(8))
    button8.grid(row= 3, column=2)
    button9 = tk.Button(frame, text=9, width=7, height=3, command = lambda: display_num(9))
    button9.grid(row=4, column=0)

def init_symbols_grid():
    sum = tk.Button(frame, text='+', width=7, height=3, command = lambda: display_num('+'))
    sum.grid(row=4, column= 1)
    minus = tk.Button(frame, text='-', width=7, height=3, command = lambda: display_num('-'))
    minus.grid(row=4, column=2)
    multiply = tk.Button(frame, text='*', width=7, height=3, command = lambda: display_num('*'))
    multiply.grid(row=5, column=0)
    divide = tk.Button(frame, text='/', width=7, height=3, command = lambda: display_num('/'))
    divide.grid(row=5, column=1)
    equal  = tk.Button(frame, text='=', width=7, height=3, command = comput_result)
    equal.grid(row=5, column=2)

init_numbers_grid()
init_symbols_grid()
clear_button = tk.Button(text='CLEAR', width = 24, height =3, command = clear, fg='red')
clear_button.pack()
root.mainloop()
