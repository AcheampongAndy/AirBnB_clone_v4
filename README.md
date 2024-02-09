# AirBnB Clone Project

## Project Description
Welcome to the AirBnB clone project! This project involves creating a command interpreter to manage AirBnB objects. The command interpreter allows you to perform various operations such as creating new objects, retrieving objects, performing operations on objects, updating object attributes, and destroying objects.

## Command Interpreter

### How to Start
To start the command interpreter, follow these steps:
```bash
$ ./console.py
```

### Available Commands
Once the command interpreter is running, you can use the following commands:

**create:** Create a new instance of a specified class and save it to the JSON file.
```bash
(hbnb) create <class_name>
```
**show:** Display the string representation of an instance based on the class name and ID.
```bash
(hbnb) show <class_name> <id>
```

**destroy:** Delete an instance based on the class name and ID.
```bash
(hbnb) destroy <class_name> <id>
```

**all:** Display the string representation of all instances or all instances of a specific class.
```bash
(hbnb) all [class_name]
```

**update:** Update an instance based on the class name and ID by adding or updating attributes.
```bash
(hbnb) update <class_name> <id> <attribute_name> "<attribute_value>"
```

**EOF:** Exit the program gracefully using the "EOF" command or by pressing Ctrl+D.
```bash
(hbnb) EOF
```

**quit:** Exit the program gracefully using the "quit" command.
```bash
(hbnb) quit
```


### Testing
To run the tests for the AirBnB clone project, use the following command:
```bash
$ python3 -m unittest discover tests
```

### Project Structure
The project is organized into the following directories and files:

**models:** Contains the implementation of the various classes used in the project, such as *BaseModel, User, State, City, Amenity, Place,* and *Review*.

**tests:** Includes unit tests for the project. The test_models directory contains test files for the classes in the models directory.

**console.py:** The main file for the command-line interface. It provides an interactive shell for managing AirBnB objects.

**file_storage.py:** Implements the serialization and deserialization of instances to a JSON file.
