# Minimum Note Change Vending Machine in Python

## Description
This is a Python program that simulates the vending machine. The main purpose of the program is to return the balance to the customer with the least amount of note.

## Features
1. Allow customers to select the drink from the drinks menu.
2. Allow customers to input any amount to pay for the drink.
3. Calculates the balance required to be returned.
4. Returns the minimum number of notes required for the balance.

## How To Use
1. Clone the repository to your local machine.
`git clone https://github.com/benrajan3/minimum-notes-balance.git`

2. Navigate into the *minimum-notes-balance* directory.
`cd minimum-notes-balance`

3. Initialise the virtual environment as a good practice.
`python3 -m venv env`

`source env/bin/activate`

4. Run the program.
`python3 main.py`

5. Input the prompts according to its requirements.

6. The result will be the minimum number of notes required for the balance.

## Example
```
Here are the drink choices 
1. Coca Cola - RM 12.00
2. Nescafe - RM 15.00
3. Milo - RM 20.00
What is your drink of choice? Please enter the number:
3
Please pay a total of RM 20.00
27
The balance returned to the customer is: RM 7.00
The least amount of notes: [5, 1, 1]
```

## Dependencies
Python 3.x
