import tkinter as tk

calculation = ""
Ans = ""


def add_to_calculation(symbol):
    global calculation

    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    global Ans

    try:
        calculation = str(eval(calculation))
        Ans = calculation
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation

    calculation = ""
    text_result.delete(1.0, "end")


def make_dynamic(widget):
    col_count, row_count = widget.grid_size()

    for i in range(row_count):
        widget.grid_rowconfigure(i, weight=2)

    for i in range(col_count):
        widget.grid_columnconfigure(i, weight=2)

    for child in widget.winfo_children():
        child.grid_configure(sticky="nsew")
        make_dynamic(child)


window_height = 350  # length of row
window_width = 250  # length of column

# Create a empty window
global window
window = tk.Tk()
window.geometry(str(window_height) + "x" + str(window_width))
window.title("CalcUlator")
window.update()

# Create a place to text
global text_result
text_result = tk.Text(
    window,
    height=window.winfo_height() * 2 / 300,
    width=window.winfo_width(),
    font=("Arial", 30),
)
text_result.grid(row=0, column=0, columnspan=4, rowspan=2)

size_font = 20
height_button = 1
width_button = 5

button1 = tk.Button(
    window,
    text="1",
    command=lambda: add_to_calculation("1"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button1.grid(row=2, column=0)
button2 = tk.Button(
    window,
    text="2",
    command=lambda: add_to_calculation("2"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button2.grid(row=2, column=1)
button3 = tk.Button(
    window,
    text="3",
    command=lambda: add_to_calculation("3"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button3.grid(row=2, column=2)
button4 = tk.Button(
    window,
    text="4",
    command=lambda: add_to_calculation("4"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button4.grid(row=3, column=0)
button5 = tk.Button(
    window,
    text="5",
    command=lambda: add_to_calculation("5"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button5.grid(row=3, column=1)
button6 = tk.Button(
    window,
    text="6",
    command=lambda: add_to_calculation("6"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button6.grid(row=3, column=2)
button7 = tk.Button(
    window,
    text="7",
    command=lambda: add_to_calculation("7"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button7.grid(row=4, column=0)
button8 = tk.Button(
    window,
    text="8",
    command=lambda: add_to_calculation("8"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button8.grid(row=4, column=1)
button9 = tk.Button(
    window,
    text="9",
    command=lambda: add_to_calculation("9"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button9.grid(row=4, column=2)
button0 = tk.Button(
    window,
    text="0",
    command=lambda: add_to_calculation("0"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button0.grid(row=5, column=1)

button_plus = tk.Button(
    window,
    text="+",
    command=lambda: add_to_calculation("+"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button_plus.grid(row=2, column=3)
button_minus = tk.Button(
    window,
    text="-",
    command=lambda: add_to_calculation("-"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button_minus.grid(row=3, column=3)
button_multiply = tk.Button(
    window,
    text="*",
    command=lambda: add_to_calculation("*"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button_multiply.grid(row=4, column=3)
button_divide = tk.Button(
    window,
    text="÷",
    command=lambda: add_to_calculation("/"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button_divide.grid(row=5, column=3)
button_point = tk.Button(
    window,
    text=".",
    command=lambda: add_to_calculation("."),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button_point.grid(row=5, column=0)
button_open = tk.Button(
    window,
    text="(",
    command=lambda: add_to_calculation("("),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button_open.grid(row=6, column=0)
button_close = tk.Button(
    window,
    text=")",
    command=lambda: add_to_calculation(")"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button_close.grid(row=6, column=1)
button_ans = tk.Button(
    window,
    text="Ans",
    command=lambda: add_to_calculation("Ans"),
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button_ans.grid(row=6, column=2)
button_clear = tk.Button(
    window,
    text="C",
    command=clear_field,
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button_clear.grid(row=6, column=3)
button_equal = tk.Button(
    window,
    text="=",
    command=evaluate_calculation,
    height=height_button,
    width=width_button,
    font=("Arial", size_font),
)
button_equal.grid(row=5, column=2)


make_dynamic(window)
window.mainloop()
