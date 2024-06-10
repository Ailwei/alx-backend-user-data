# 0x03. User Authentication Service

## Back-end Authentication

**Weight:** 1

**Project Timeline:**
- **Start Date:** June 10, 2024, 6:00 AM
- **End Date:** June 14, 2024, 6:00 AM
- **Checker Release:** June 11, 2024, 6:00 AM
- **Auto Review:** Launched at the project deadline

### Introduction
In the industry, it is recommended to use a module or framework for authentication (e.g., Flask-User in Python-Flask). However, for learning purposes, we will implement an authentication system from scratch to understand the underlying mechanisms.

### Resources
- [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Requests module](https://docs.python-requests.org/en/latest/)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### Learning Objectives
By the end of this project, you should be able to:
- Declare API routes in a Flask app
- Get and set cookies
- Retrieve request form data
- Return various HTTP status codes

### Requirements
- **Allowed editors:** vi, vim, emacs
- **Execution environment:** Ubuntu 18.04 LTS using python3 (version 3.7)
- **Code standards:**
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/env python3`
  - A `README.md` file at the root of the project is mandatory
  - Code should use `pycodestyle` style (version 2.5)
  - All files must be executable
  - File lengths will be tested using `wc`
  - All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
  - All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  - All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
  - Documentation should be meaningful sentences explaining the purpose of the module, class, or method
- **Type annotations:** All functions should be type annotated
- **Interactions:** 
  - The Flask app should only interact with `Auth` and never with the database (`DB`) directly
  - Only public methods of `Auth` and `DB` should be used outside these classes
