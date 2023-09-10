import tkinter as tk

def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    result = x - y
    return result

def multiplication(x, y):
    result = x * y
    return result

def division(x, y):
    if y != 0:
        result = x / y
        return result
    else:
        return "Cannot divide by 0"

def calculate():
    x = float(entry_x.get())
    y = float(entry_y.get())
    operation = operator_var.get()
    
    if operation == "Add":
        result = add(x, y)
    elif operation == "Subtract":
        result = subtract(x, y)
    elif operation == "Multiply":
        result = multiplication(x, y)
    elif operation == "Divide":
        result = division(x, y)
    
    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create input fields
label_x = tk.Label(root, text="enter the value of x:")
label_x.pack()
entry_x = tk.Entry(root)
entry_x.pack()

label_y = tk.Label(root, text="Enter the value of y:")
label_y.pack()
entry_y = tk.Entry(root)
entry_y.pack()


operator_var = tk.StringVar()
operator_var.set("operation")  
operators = ["Add", "Subtract", "Multiply", "Divide"]
operator_menu = tk.OptionMenu(root, operator_var, *operators)
operator_menu.pack()


calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()
