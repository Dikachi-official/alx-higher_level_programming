<h2>Python - Test-driven development</h2>

<p>In this project, I started practicing test-driven development using docstringand unittest in Python.</p>

<h2>Tests ✔️</h2>
<li>tests: Folder of test files. Includes both Holberton-provided ones as well as the following eight independently-developed:</li>
<li>0-add_integer.txt</li>
<li>2-matrix_divided.txt</li>
<li>3-say_my_name.txt</li>
<li>4-print_square.txt</li>
<li>5-text_indentation.txt</li>
<li>6-max_integer_test.py</li>
<li>100-matrix_mul.txt</li>
<li>101-lazy_matrix_mul.txt</li>
<h2>Function Prototypes 💾</h2>
<h3>Prototypes for functions written in this project:</h3>

File	Prototype
0-add_integer.py	def add_integer(a, b=98):
2-matrix_divided.py	def matrix_divided(matrix, div):
3-say_my_name.py	def say_my_name(first_name, last_name=""):
4-print_square.py	def print_square(size):
5-text_indentation.py	def text_indentation(text):
100-matrix_mul.py	def matrix_mul(m_a, m_b):
101-lazy_matrix_mul.py	def lazy_matrix_mul(m_a, m_b):
102-python.c	void print_python_string(PyObject *p);
<h2>Tasks 📃</h2>
<h3>0. Integers addition</h3>

<h4>0-add_integer.py:</h4> Python function that returns the integer addition of two numbers.
If either of a or b is not an int or float, a TypeError is raised with the message a must be an integer or b must be an integer.
If either of a or b is a float, it is casted to an int before addition.
<h4>1. Divide a matrix</h4>

<h4>2-matrix_divided.py:</h4> Python function that divides all elements of a matrix by a common divisor.
Returns a new matrix representing the division of all elements of matrix by div.
Quotients are rounded to two decimal places.
If matrix is not a list of lists of ints or floats, a TypeError is raised with the message matrix must be a matrix (list of lists) of integers/floats.
If matrix contains rows of different lengths, a TypeError is raised with the message Each row of the matrix must have the same size.
If the divisor div is not an int or float, a TypeError is raised with the message div must be a number.
If div is 0, a ZeroDivisionError is raised with the message division by zero.
<h4>2. Say my name</h4>

<strong>3-say_my_name.py:</strong> Python function that prints a name in the format My name is <first_name> <last_name>.
If either of first_name or last_name is not a str, a TypeError is raised with the message first_name must be a string or last_name must be a string.
<h4>3. Print square</h4>

<strong>4-print_square.py:</strong> Python function that prints a square using the # character.
The paramter size represents the height/width of the square.
If size is not an int, a TypeError is raised with the message, size must be an integer.
If size is less than 0, a ValueError is raised with the message size must be >= 0.
<h4>4. Text indentation</h4>

<strong>5-text_indentation.py:</strong> Python function that prints text with indentation.
Two new lines are printed after any ., ?, or : character.
If text is not a str, a TypeError is raised with the message text must be a string.
No spaces are printed at the beginning or end of each printed line.
<h4>5. Max integer - Unittest</h4>

tests/6-max_integer_test.py: Python class/scriptthat runs unittests for the function def max_integer(list=[]):.
<h4>6. Matrix multiplication</h4>

100-matrix_mul.py: Python function that multiplies two matrices.
Returns a new matrix representing the multiplication of m_a by m_b.
If either of m_a or m_b is empty (ie. == [] or == [[]]), a ValueError is raised with the message m_a can't be empty or m_b can't be empty.
If either of m_a or m_b is not a list, a TypeError is raised with the message m_a must be a list or m_b must be a list.
If either of m_a or m_b is not a list of lists, a TypeError is raised with the message m_a must be a list of lists or m_b must be a list of lists.
If either of m_a or m_b is not a list of lists of ints or floats, a TypeError is raised with the message m_a should contain only integers or floats or m_b should contain only integers or floats.
If either of m_a or m_b contains rows of different lengths, a TypeError is raised with the message each row of m_a must should be of the same size or each row of m_b must should be of the same size.
If m_a and m_b cannot be multiplied (ie. row size of m_a does not match column size of m_b), a ValueError is raised with the message m_a and m_b can't be multiplied.
<h4>7. Lazy matrix multiplication</h4>

101-lazy_matrix_mul.py: Python function that multiplies two matrices using the module NumPy.
Identical in function to 100-matrix_mul.py.
<h4>8. CPython #3: Python Strings</h4>

<strong>102-python.c:</strong> C function that prints basic information about Python string objects.
