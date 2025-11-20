# 📘 GUI Calculator — Python + Tkinter
A colorful beginner-friendly graphical calculator built with Python.

🧮 About the Project
This project represents one of my first visual creations using Python and Tkinter.
I wanted to build something simple, functional, and fun — a small calculator application fully developed from scratch.
The app includes a custom layout, custom colors, responsive grid behavior, and a clean display for inputs and results. It was a great learning experience in GUI programming.

✨ Features
Basic arithmetic operations:
Addition ➕
Subtraction ➖
Multiplication ✖
Division ➗
Percentage %
Clear display button (C)
Decimal point support
Real-time expression input
Result calculation using Python’s eval()
Custom colors for each button
Window icon (calc-icon.ico)

🖥️ Interface Overview
The interface is built entirely with Tkinter, using:
Frame for the display
Frame for the button grid
Label for showing the current expression
Button for numbers and operations
A 4×5 responsive grid layout
Custom background colors for each key
The design aims to be visually distinct, playful, and easy to understand.

📦 Installation & Running
You only need Python installed.
To run the calculator:
python main.py

Make sure the following files are in the same directory:
main.py
calc-img.read.png
calc-icon.ico
README.md

📂 Project Structure
/your-project-folder
│── calc-img.read.png     Screenshot used in README
│── calc-icon.ico         Window icon
│── main.py               Calculator source code
│── README.md             This file

🧠 Code Overview
The core logic uses a single string (all_values) to store the current mathematical expression.
Button presses append characters to the string, and the = button triggers eval() to compute the result.

Example functions from the code:
# Add values to the input
def values(event):
    global all_values
    all_values = all_values + str(event)
    text_value.set(all_values)

# Evaluate the expression
def calculate():
    result = eval(all_values)
    text_value.set(str(result))

# Clear the display
def clear_display():
    global all_values
    all_values = ""
    text_value.set("")

🛠️ Technologies Used

Python 3
Tkinter (built-in GUI toolkit)

⭐ Final Notes

This project is special because it is one of my first visual applications in Python.
It helped me understand event handling, widget layout, and GUI architecture.

If you like this project, feel free to ⭐ star the repository or contribute with suggestions!
