<h2>Python - Input/Output</h2>
<p>In this project, I practiced file handling in Python. I used the builtin with, open, and read functions with the json module to read and write files and serialize and deserialize objects with JSON.</p>

<h2>Function Prototypes 💾</h2>
<li>Prototypes for functions written in this project:</li>

<h2>Tasks 📃</h2>
<strong>0. Read file</strong>

<<<<<<< HEAD
<strong>0-read_file.py:</strong> Python function that prints the contents of a UTF8 text file to standard output.
<strong>1. Write to a file</strong>

<strong>1-write_file.py:</strong> Python function that writes a string to a UTF8 text file and returns the number of characters written.
<strong>2. Append to a file</strong>

<strong>2-append_write.py:</strong> Python function that appends a string to the end of a UTF8 text file and returns the number of characters appended.
<strong>3. To JSON string</strong>

<strong>3-to_json_string.py:</strong> Python function that returns the JSON string representation of an object.
<strong>4. From JSON string to Object</strong>

<strong>4-from_json_string.py:</strong> Python function that returns the Python object represented by a JSON string.
<strong>5. Save Object to a file</strong>

<strong>5-save_to_json_file.py:</strong>
Python function that writes an object to a text file using JSON representation.
<strong>6. Create object from a JSON file</strong>

<strong>6-load_from_json_file.py:</strong> Python function that creates an object from a .json file.
<strong>7. Load, add, save</strong>

<strong>7-add_item.py:</strong> Python script that stores all command line arguments to a Python list saved in the file add_item.json.
<strong>8. Class to JSON</strong>

<strong>8-class_to_json.py:</strong> Python function that returns the dictionary description for simple Python data structures (lists, dictionaries, strings, integers and booleans).
=======</p>
<strong>0-read_file.py:</strong> Python function that prints the contents of a UTF8 text file to standard output.

<strong>1. Write to a file</strong>

<strong>1-write_file.py:</strong> Python function that writes a string to a UTF8 text file and returns the number of characters written.

<strong>2. Append to a file</strong>

<strong>2-append_write.py:</strong> Python function that appends a string to the end of a UTF8 text file and returns the number of characters appended.

<strong>3. To JSON string</strong>

<strong>3-to_json_string.py:</strong> Python function that returns the JSON string representation of an object.

<strong>4. From JSON string to Object</strong>

<strong>4-from_json_string.py:</strong> Python function that returns the Python object represented by a JSON string.

<strong>5. Save Object to a file</strong>

<strong>5-save_to_json_file.py:</strong> Python function that writes an object to a text file using JSON representation.

<strong>6. Create object from a JSON file</strong>

6-load_from_json_file.py: Python function that creates an object from a .json file.

<strong>7. Load, add, save</strong>

7-add_item.py: Python script that stores all command line arguments to a Python list saved in the file add_item.json.

<strong>8. Class to JSON</strong>

<strong>8-class_to_json.py:</strong> Python function that returns the dictionary description for simple Python data structures (lists, dictionaries, strings, integers and booleans).

>>>>>>> 5b0d6f78f1a2f77b4ae61fe27bf726bc1288af45
<strong>9. Student to JSON</strong>

<p>9-student.py: Python class Student that defines a student. Includes:
Public instance attributes first_name, last_name, and age.
Instantiation with first_name, last_name, and age: def __init__(self, first_name, last_name, age):.
Public method def to_json(self): that returns the dictionary representation of a Student instance.
<<<<<<< HEAD
=======</p>

>>>>>>> 5b0d6f78f1a2f77b4ae61fe27bf726bc1288af45
<strong>10. Student to JSON with filter</strong>

<p>10-student.py: Python class Student that defines a student. Builds on 11-student.py with:
Public method def to_json(self, attrs=None): that returns the dictionary representation of a Student instance.
If attrs is a list of strings, only the attributes listed are represented in the dictionary.
<<<<<<< HEAD
=======</p>

>>>>>>> 5b0d6f78f1a2f77b4ae61fe27bf726bc1288af45
<strong>11. Student to disk and reload</strong>

<p>11-student.py: Python class Student that defines a student. Builds on 12-student.py with:
Public method def reload_from_json(self, json): that replaces all attributes of the Student instance using the key/value pairs listed in json.
The method assumes json is a dictionary containing attributes with name/value corresponding to key/value.
<<<<<<< HEAD
=======</p>

>>>>>>> 5b0d6f78f1a2f77b4ae61fe27bf726bc1288af45
<strong>12. Pascal's Triangle</strong>
<p>12-pascal_triangle.py: Python function that returns a list of lists of integers representing Pascal's triangle of size n.
Assumes the size parameter n is an integer.
If n is less than or equal to 0, returns an empty list.
<<<<<<< HEAD</p>
<strong>13. Search and update</strong>

<p>100-append_after.py: Python function that inserts a line of text to a file after each line containing a specified string.
=======</p>

<strong>13. Search and update</strong>

100-append_after.py: Python function that inserts a line of text to a file after each line containing a specified string.

>>>>>>> 5b0d6f78f1a2f77b4ae61fe27bf726bc1288af45
<strong>14. Log parsing</strong>

<strong>101-stats.py:</strong> Python script that reads lines from standard input. After every 10 lines or the input of a keyboard interruption (CTRL + C), computes the following metrics:
Total file size up that point: File size: <total size>
Status code of each read line, printed in ascending order: <status code>: <number>
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
