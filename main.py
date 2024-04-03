"""
Idea:
- A list to show the available notes and amount of per note in the vending machine. 
- A function to loop through the available notes in the vending machine and determine the largest valued notes to return
    - Check if the current largest valued note has any quantity. If not, skip to the next index
    - Check if the current balance is less than expected. Then check if the next sum of current balance and current largest note is 
    greater than expected balance
        - Check if current balance is equivalent to expected balance. Break the loop then return
    - Requires a condition to add the index in case of not meeting the condition above. Look at the next largest note

Time Complexity: 
- Best Case: O(1)
- Worst Case: O(n) where n is the note value in the list
"""

available_notes = [[100,0],[50,2],[20,5],[10,5],[5,5],[1,5]]
drinks_dict = {
    1: 12,
    2: 15,
    3: 20
}

def main(drinks):
    print("Here are the drink choices \n1. Coca Cola - RM 12.00\n2. Nescafe - RM 15.00\n3. Milo - RM 20.00")
    customer_option = int(input("What is your drink of choice? Please enter the number:\n"))
    try:
        drink_price = drinks[customer_option]
        customer_payment = int(input(f"Please pay a total of RM {drink_price}.00\n"))
        customer_balance = customer_payment - drink_price
        print(f"The balance returned to the customer is: RM {customer_balance}.00")
        optimal_customer_balance = balance_change(customer_balance, available_notes)
        return f"The least amount of notes: {optimal_customer_balance}"
    except KeyError:    # handle error in case of customer choosing other options
        return "The choice you have entered is invalid. Please try again!"
    

def balance_change(expected_balance, vending_notes):
    balance_notes = []
    current_balance = 0
    i = 0

    if current_balance == expected_balance:     # if no balance is required. O(1)
        return "No balance required to return."
    
    while True:
        curr_largest_note = vending_notes[i][0] # the note value
        number_of_notes = vending_notes[i][1]   # the quantity of note 

        if current_balance < expected_balance and current_balance + curr_largest_note <= expected_balance:
            if number_of_notes != 0:    # ensure that the note value is available
                current_balance += curr_largest_note    
                number_of_notes -= 1    # used note. deduct from the original count
                vending_notes[i][1] = number_of_notes
                balance_notes.append(curr_largest_note) # used note appended into list to be output

                if current_balance == expected_balance: # if the current balance in calculation is equal to expected balance. Return the list of notes.
                    break

                elif current_balance + curr_largest_note > expected_balance:    # if the current note value is too large where it exceeds the expected balance value. Next note
                    i += 1
            else:
                if i >= len(vending_notes)-1:   # if no note is available to return the balance. 
                    return "There is not enough note to return the balance."
                i += 1  # check next index if the current note value is unavailable

        else:
            if i >= len(vending_notes)-1:   # assertion for error handling
                assert IndexError   
            i += 1  # check the next index if the current note value is too large which has exceeded the expected balance
        
    return balance_notes


print(main(drinks_dict))
