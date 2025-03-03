import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import math, mpmath

def format_result(value):
    """Format the result to remove unnecessary .0"""
    return int(value) if isinstance(value, float) and value.is_integer() else value

# Existing calculator functions
def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(format_result(num1 + num2))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(format_result(num1 - num2))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(format_result(num1 * num2))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Math Error", "Division by zero is not allowed")
        else:
            result.set(format_result(num1 / num2))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def power():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(format_result(num1 ** num2))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

def log_function():
    try:
        num = float(entry1.get())
        base = base_entry.get().strip()
        if num <= 0:
            messagebox.showerror("Math Error", "Logarithm is defined only for positive numbers")
        else:
            if base == "":
                log_base = 10  # Default to base 10
            else:
                log_base = float(base)
                if log_base <= 0:
                    messagebox.showerror("Math Error", "Logarithm base must be greater than 0")
                    return
            result.set(format_result(math.log(num, log_base)))
    #Nice.
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number and base")

def ln_function():
    try:
        num = float(entry1.get())
        if num <= 0:
            messagebox.showerror("Math Error", "ln is defined only for positive numbers")
        else:
            result.set(format_result(math.log(num)))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

def sin_function():
    try:
        num = float(entry1.get())
        result.set(format_result(math.sin(math.radians(num))))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number in the first input")

def cos_function():
    try:
        num = float(entry1.get())
        result.set(format_result(math.cos(math.radians(num))))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number in the first input")

def tan_function():
    try:
        num = float(entry1.get())
        if (num % 90 == 0) and (int(num / 90) % 2 == 1):  # Undefined for tan(90), tan(270), etc.
            messagebox.showerror("Math Error", "tan is undefined for angles like 90°, 270°, etc.")
        else:
            result.set(format_result(math.tan(math.radians(num))))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number in the first input")

def arcsin_function():
    try:
        num = float(entry1.get())
        if -1 <= num <= 1:
            result.set(format_result(math.degrees(math.asin(num))))
        else:
            messagebox.showerror("Math Error", "arcsine is defined only for values between -1 and 1")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number in the first input")

def arccos_function():
    try:
        num = float(entry1.get())
        if -1 <= num <= 1:
            result.set(format_result(math.degrees(math.acos(num))))
        else:
            messagebox.showerror("Math Error", "arccosine is defined only for values between -1 and 1")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number in the first input")

def arctan_function():
    try:
        num = float(entry1.get())
        result.set(format_result(math.degrees(math.atan(num))))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number in the first input")

def cot_function():
    try:
        num = float(entry1.get())
        if (num % 180 == 0):  # Undefined for cotangent at 0°, 180°, etc.
            messagebox.showerror("Math Error", "cotangent is undefined at angles like 0°, 180°, etc.")
        else:
            result.set(format_result(1 / math.tan(math.radians(num))))  # Cotangent is 1/tan
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number in the first input")

def sec_function():
    try:
        num = float(entry1.get())
        if num == 90 or num == 270:  # Undefined for secant at 90° and 270°
            messagebox.showerror("Math Error", "secant is undefined at 90° and 270°")
        else:
            result.set(format_result(1 / math.cos(math.radians(num))))  # Secant is 1/cos
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number in the first input")

def csc_function():
    try:
        num = float(entry1.get())
        if num == 0 or num == 180:  # Undefined for cosecant at 0° and 180°
            messagebox.showerror("Math Error", "cosecant is undefined at 0° and 180°")
        else:
            result.set(format_result(1 / math.sin(math.radians(num))))  # Cosecant is 1/sin
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number in the first input")

def pi():
    result.set("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063")

# Function to open the image viewer window
def open_image_viewer():
    def go_back():
        viewer_window.destroy()
        root.deiconify()

    root.withdraw()

    viewer_window = tk.Toplevel(root)
    viewer_window.title("Professional Gallery Of Thy Photographs And Text")
    viewer_window.geometry("500x500")
    viewer_window.iconphoto(False, tk.PhotoImage(file="SillyCat.png"))

    canvas = tk.Canvas(viewer_window, bg="white")
    scrollbar = tk.Scrollbar(viewer_window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="white")

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Display images (customizable list)
    image_paths = ["SillyCat.png"]
    for img_path in image_paths:
        try:
            img = PhotoImage(file=img_path)
            img_label = tk.Label(scrollable_frame, image=img, bg="white")
            img_label.image = img  #Reference to avoid garbage collection
            img_label.pack(pady=10)
        except Exception as e:
            error_label = tk.Label(
                scrollable_frame, text=f"Error loading {img_path}: {e}", bg="white", fg="red"
            )
            error_label.pack(pady=10)

    # Add the canvas and scrollbar to the viewer window
    canvas.pack(side="left", fill="both", expand=True)
    tk.Button(viewer_window, text="Go Back", command=go_back).pack(pady=10)

# Main application window
root = tk.Tk()
root.title("Filip's Simple Calculator (Giganometry Edition)")
root.iconphoto(False, tk.PhotoImage(file="SillyCat.png"))

# Input fields
tk.Label(root, text="Enter First Number:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Second Number:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Base (For Log):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
base_entry = tk.Entry(root)
base_entry.grid(row=2, column=1, padx=10, pady=5)

# Result display
tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
result = tk.StringVar()
tk.Entry(root, textvariable=result, state="readonly").grid(row=3, column=1, padx=10, pady=5)

# Standard Buttons
tk.Button(root, text="Add", command=add).grid(row=0, column=2, padx=10, pady=5)
tk.Button(root, text="Subtract", command=subtract).grid(row=1, column=2, padx=10, pady=5)
tk.Button(root, text="Multiply", command=multiply).grid(row=2, column=2, padx=10, pady=5)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=2, padx=10, pady=5)
tk.Button(root, text="Power", command=power).grid(row=4, column=2, padx=10, pady=5)

# Trigonometric buttons
tk.Button(root, text="sin", command=sin_function)     .grid(row=0, column=3, padx=10, pady=5)
tk.Button(root, text="cos", command=cos_function)     .grid(row=1, column=3, padx=10, pady=5)
tk.Button(root, text="tan", command=tan_function)     .grid(row=2, column=3, padx=10, pady=5)
tk.Button(root, text="sin⁻¹", command=arcsin_function).grid(row=3, column=3, padx=10, pady=5)
tk.Button(root, text="cos⁻¹", command=arccos_function).grid(row=4, column=3, padx=10, pady=5)
tk.Button(root, text="tan⁻¹", command=arctan_function).grid(row=5, column=3, padx=10, pady=5)
tk.Button(root, text="csc", command=csc_function)     .grid(row=6, column=3, padx=10, pady=5)
tk.Button(root, text="sec", command=sec_function)     .grid(row=7, column=3, padx=10, pady=5)
tk.Button(root, text="cot", command=cot_function)     .grid(row=8, column=3, padx=10, pady=5)

# Logarithmic buttons
tk.Button(root, text="Log", command=log_function).grid(row=0, column=4, padx=10, pady=5)
tk.Button(root, text="ln", command=ln_function).grid(row=1, column=4, padx=10, pady=5)

#Pi
tk.Button(root, text="π", command=pi).grid(row=2, column=4, padx=10, pady=5)

#Miscellaneous
tk.Button(root, text="Professional Gallery Of Thy Photographs And Text", command=open_image_viewer).grid(row=4, column=0, padx=10, pady=5)

# Run the application
root.mainloop()