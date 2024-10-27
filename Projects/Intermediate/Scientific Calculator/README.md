Scientific Calculator

A fully functional scientific calculator built with Python and Tkinter, featuring a graphical user interface (GUI) that supports basic arithmetic operations, advanced mathematical functions, and constants. This calculator provides a user-friendly experience with clear button layouts and intuitive functionality.

Table of Contents

	•	Features
	•	Technologies Used
	•	Installation
	•	Usage
	•	Button Functions
	•	Screenshots
	•	Customization
	•	License

Features

	•	Basic Arithmetic Operations: Addition, subtraction, multiplication, division, modulus, and exponentiation.
	•	Advanced Mathematical Functions: Trigonometric functions (sin, cos, tan), logarithmic functions, square root, exponential, factorial, and absolute value.
	•	Mathematical Constants: Access to pi and e.
	•	Parentheses Support: Ability to handle complex expressions using parentheses.
	•	Clear Display: Easily clear the current input or result.
	•	Error Handling: Provides clear error messages for invalid inputs or expressions.

Technologies Used

	•	Python 3.x: The programming language used to develop the calculator.
	•	Tkinter: Python’s standard GUI library for creating the graphical interface.
	•	Standard Libraries:
	•	math: Provides access to mathematical functions and constants.
	•	ast: Used to parse and evaluate mathematical expressions safely.
	•	operator: Offers efficient functions corresponding to the intrinsic operators.

Installation

	1.	Prerequisites:
	•	Ensure you have Python 3.x installed on your system.
	•	Verify that the Tkinter library is available:
	•	Run python3 -m tkinter in your terminal. If a small window appears, Tkinter is installed.
	•	If not installed, follow instructions specific to your operating system to install Tkinter.
	2.	Download the Code:
	•	Save the calculator script as scientific_calculator.py.
	3.	Run the Application:
	•	Open a terminal or command prompt.
	•	Navigate to the directory containing scientific_calculator.py.
	•	Execute the command:

python3 scientific_calculator.py

	•	Replace python3 with python if necessary.

Usage

Launching the Calculator

	•	Upon running the script, a window titled “Scientific Calculator” will appear.
	•	The calculator window contains:
	•	A display screen at the top to show input expressions and results.
	•	A grid of buttons representing numbers, operators, functions, and constants.

Performing Calculations

	1.	Entering Numbers and Operators:
	•	Click on the numeric buttons (0–9) to input numbers.
	•	Use operator buttons (+, -, *, /, %, **) for arithmetic operations.
	2.	Using Functions:
	•	Click on function buttons (e.g., sin, cos, log) to include them in your expression.
	•	Functions require parentheses with arguments inside (e.g., sin(pi/2)).
	3.	Utilizing Constants:
	•	Use pi and e buttons to include these constants in your calculations.
	4.	Evaluating Expressions:
	•	After constructing your expression, press the = button to compute the result.
	•	The result will be displayed on the screen.
	5.	Clearing Input:
	•	Press the C button to clear the current input or result from the display.

Button Functions

Below is a detailed explanation of each button and its usage:

Numeric Buttons

	•	0 – 9: Enter digits to form numbers.

Decimal Point

	•	.: Use to input decimal numbers (e.g., 3.14).

Arithmetic Operators

	•	+: Addition operator.
	•	-: Subtraction operator.
	•	*: Multiplication operator.
	•	/: Division operator.
	•	%: Modulus operator (remainder of division).
	•	**: Exponentiation operator (power).

Parentheses

	•	( and ): Use to group expressions and define the order of operations.

Functions

	•	Trigonometric Functions (Input in radians):
	•	sin: Sine function.
	•	cos: Cosine function.
	•	tan: Tangent function.
	•	Logarithmic Function:
	•	log: Natural logarithm (base e).
	•	Other Mathematical Functions:
	•	sqrt: Square root function.
	•	exp: Exponential function (returns e raised to the power of the argument).
	•	factorial: Factorial function (argument should be a non-negative integer).
	•	abs: Absolute value function.
	•	mod: Modulus function (alternate way to compute the remainder).

Constants

	•	pi: Represents the mathematical constant π (approximately 3.14159).
	•	e: Represents Euler’s number (approximately 2.71828).

Control Buttons

	•	=: Evaluates the expression entered in the display.
	•	C: Clears the current input from the display.

Screenshots

(As this is a text-based README, please visualize the calculator interface with the descriptions provided.)

Customization

You can customize the calculator to suit your preferences:

	•	Adding Functions:
	•	Modify the functions dictionary in the script to include additional mathematical functions from the math module or custom functions.
	•	Add corresponding buttons in the button_texts list within the script.
	•	Changing Themes:
	•	Adjust the color scheme by modifying the bg (background) and fg (foreground/text) parameters for the window, display, and buttons.
	•	Example: Change master.configure(bg="#f0f0f0") to a different color code.
	•	Adjusting Font Sizes:
	•	Modify font=("Helvetica", size) in the display and button configurations to increase or decrease text size.
	•	Resizing the Window:
	•	Remove or adjust master.resizable(False, False) to allow window resizing.

License

This project is open-source. 
Enjoy using the Scientific Calculator! If you have any questions or need further assistance, feel free to reach out.
