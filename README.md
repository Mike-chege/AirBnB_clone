# AirBnB_Clone & The_console

This project covers AirBnB clone & command interpreter(The console). The whole project will be wrtten using python3.

## :file_folder: Classes
The following are the classes used:

- A parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- Then create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- classes (`User`, `State`, `City`, `Place`…) that inherit from BaseModel
- `FileStorage` the first abstracted storage engine of the project
- `Unittests` to validate all classes and storage engine

## The console should be able to:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Execution
To run the console use:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
In non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## :scroll: Tests
To run the tests use:

```
python3 -m unittest discover tests
```
In non-interactive mode
```
echo "python3 -m unittest discover tests" | bash
```

##  :label: Authors
* **Michael Chege** - [@mikechege](https://github.com/mikechege01)
* **Muluken Tenaw** - [@amigaye](https://github.com/amigaye)
