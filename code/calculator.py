import tkinter as tk

calculation = ''

def initialization():

    window_height = 350 # length of row
    window_width = 250 # length of column

    # Create a empty window
    global window
    window = tk.Tk()
    window.geometry(str(window_height) + 'x' + str(window_width))
    window.update()

    # Create a place to text
    global text_result
    text_result = tk.Text(window, height=window.winfo_height()*2/350, width=window.winfo_width(), font=('Arial', 30))
    text_result.grid(row=0, column=0, columnspan=4, rowspan=2)

    make_button(window,'1',2,0)
    make_button(window,'2',2,1)
    make_button(window,'3',2,2)
    make_button(window,'4',3,0)
    make_button(window,'5',3,1)
    make_button(window,'6',3,2)
    make_button(window,'7',4,0)
    make_button(window,'8',4,1)
    make_button(window,'9',4,2)
    make_button(window,'0',5,1)

    make_button(window,'=',5,2)
    make_button(window,'+',2,3)
    make_button(window,'-',3,3)
    make_button(window,'x',4,3)
    make_button(window,'÷',5,3)
    
    make_button(window,'.',5,0)
    make_button(window,'(',6,0)
    make_button(window,')',6,1)
    make_button(window,'Ans',6,2)

    make_dynamic(window)
    window.mainloop()

def add_to_calculation(symbol):
    global calculation 
    calculation += str(symbol)
    text_result.delete(1.0, 'End')
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, 'End')
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.delete(1.0, 'Error!') 

def clear_field():
    global calculation
    calculation = '' 
    text_result.delete(1.0, 'End')

def make_button(window, name, row, column, height=1, width=5, font=('Arial', 20)):
    button = tk.Button(window, text=name, command=lambda: add_to_calculation(name), height=height, width=width, font=font)
    button.grid(row=row, column=column)

