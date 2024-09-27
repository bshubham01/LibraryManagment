# Library Management System

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Features](#features)
4. [Setup Instructions](#setup-instructions)
5. [Running Tests](#running-tests)
6. [Running the Application](#running-the-application)
7. [Example Usage](#example-usage)

## Introduction
The Library Management System is a Python-based application that allows users to manage books in a library. Users can add new books, borrow and return books, and view available books. This project is designed to demonstrate basic object-oriented programming principles, test-driven development (TDD), and the use of Python collections.

## Technologies Used
- **Python 3.8 or higher**
- **pytest** for unit testing

## Features
- **Add new books** to the library.
- **Borrow books** if they are available.
- **Return books** that have been borrowed.
- **View all available books** in the library.

## Setup Instructions
To set up and run the project locally, follow these steps:

```bash
git clone git@github.com:bshubham01/LibraryManagment.git
cd LibraryManagment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest


