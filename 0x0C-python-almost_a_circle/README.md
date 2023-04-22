<h2>Python - Almost a circle</h2>
<h4>Circle</h4>

<p>In this project, I encapsulated skills in Python object-oriented programming by coding three connected classes to represent rectangles and squares. I wrote my own test suite using the unittest module to test all functionality for each class.</p>

<h5>The three classes involved utilizing the following Python tools:</h5>

Import
Exceptions
Private attributes
Getter/setter
Class/static methods
Inheritance
File I/O
args/kwargs
JSON and CSV serialization/deserialization
Unittesting
Tests ✔️
tests/test_models: Folder containing the following independently-developed test files:
test_base.py
test_rectangle.py
test_square.py
Classes 🆑
Base
Represents the "base" class for all other classes in the project. Includes:

Private class attribute __nb_objects = 0.
Public instance attribute id.
<strong>Class constructor def __init__(self, id=None):</strong>
<p>If id is None, increments __nb_objects and assigns its value to the public instance attribute id.
Otherwise, sets the public instance attribute id to the provided id.
Static method def to_json_string(list_dictionaries): that returns the JSON string serialization of a list of dictionaries.
If list_dictionaries is None or empty, returns the string "[]".</p>
<br/>
<strong>Class method def save_to_file(cls, list_objs):</strong> that writes the JSON serialization of a list of objects to a file.
The parameter list_objs is expected to be a list of Base-inherited instances.
If list_objs is None, the function saves an empty list.
The file is saved with the name <cls name>.json (ie. Rectangle.json)
Overwrites the file if it already exists.
<strong>Static method def from_json_string(json_string):</strong> that returns a list of objects deserialized from a JSON string.
The parameter json_string is expected to be a string representing a list of dictionaries.
If json_string is None or empty, the function returns an empty list.</p>
<strong>Class method def create(cls, **dictionary):</strong><p> that instantiates an object with provided attributes.
Instantiates an object with the attributes given in **dictionary.
<strong>Class method def load_from_file(cls):</strong> that returns a lis
t of objects instantiated from a JSON file.
Reads from the JSON file <cls name>.json (ie. Rectangle.json)
If the file does not exist, the function returns an empty list.</p>
<strong>Class method def save_to_file_csv(cls, list_objs):</strong> that writes the CSV serialization of a list of objects to a file.
The parameter list_objs is expected to be a list of Base-inherited instances.
If list_objs is None, the function saves an empty list.
The file is saved with the name <cls name>.csv (ie. Rectangle.csv)
Serializes objects in the format <id>,<width>,<height>,<x>,<y> for Rectangle objects and <id>,<size>,<x>,<y> for Square objects.
<strong>Class method def load_from_file_csv(cls):</strong> that returns a list of objects instantiated from a CSV file.
Reads from the CSV file <cls name>.csv (ie. Rectangle.csv)
If the file does not exist, the function returns an empty list.
<br/>
<strong>Static method def draw(list_rectangles, list_squares):</strong> that draws Rectangle and Square instances in a GUI window using the turtle module.
The parameter list_rectangles is expected to be a list of Rectangle objects to print.
The parameter list_squares is expected to be a list of Square objects to print.
Rectangle
<strong>Represents a rectangle. Inherits from Base with:</strong>

Private instance attributes __width, __height, __x, and __y.
Each private instance attribute features its own getter/setter.
<strong>Class constructor def __init__(self, width, height, x=0, y=0, id=None):</strong>
<li>If either of width, height, x, or y is not an integer, raises a TypeError exception with the message <attribute> must be an integer.</li>
<li>If either of width or height is >= 0, raises a ValueError exception with the message <attribute> must be > 0.</li>
<li>If either of x or y is less than 0, raises a ValueError exception with the message <attribute> must be >= 0.</li>
<li>Public method def area(self): that returns the area of the Rectangle instance.</li>
<li>Public method def display(self): that prints the Rectangle instance to stdout using the # character.</li>
<li>Prints new lines for the y coordinate and spaces for the x coordinate.</li>
<li>Overwrite of __str__ method to print a Rectangle instance in the format [Rectangle] (<id>) <x>/<y>.</li>
<li>Public method def update(self, *args, **kwargs): that updates an instance of a Rectangle with the given attributes.</li>
<strong>*args must be supplied in the following order:</strong>
<li>1st: id</li>
<li>2nd: width</li>
<li>3rd: height</li>
<li>4th: x</li>
<li>5th: y</li>
**kwargs is expected to be a double pointer to a dictionary of new key/value attributes to update the Rectangle with.
**kwargs is skipped if *args exists.
Public method def to_dictionary(self): that returns the dictionary representation of a Rectangle instance.
Square
Represents a square. Inherits from Rectangle with:

<strong>Class constructor def __init__(self, size, x=0, y=0, id=None):</strong>
The width and height of the Rectangle superclass are assigned using the value of size.
Overwrite of __str__ method to print a Square instance in the format [Square] (<id>) <x>/<y>.
Public method def update(self, *args, **kwargs): that updates an instance of a Square with the given attributes.
<strong>*args must be supplied in the following order:</strong>
<li>1st: id</li>
<li>2nd: size</li>
<li>3rd: x</li>
<li>4th: y</li>
<p>**kwargs is expected to be a double pointer to a dictoinary of new key/value attributes to update the Square with.
**kwargs is skipped if *args exists.
<strong>Public method def to_dictionary(self):</strong> that returns the dictionary representation of a Square.</p>
