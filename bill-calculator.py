"""
This is Part 4 of the Hackbright Prep functions exercise 
 """


def calculate_tip(bill_amt, tip_percentage):
    """Given the bill amount and tip percentage, calculates the tip."""

    tip = bill_amt * tip_percentage
    return tip

def calculate_total(bill_amt, tip_amt):
    """Given the tip amount and the bill amount, calculates the total bill."""

    total = bill_amt + tip_amt
    return total

def split_bill(total, number_of_people):
    """Given the bill total and the number of people, calculates the total per person."""

    total_per_person = total / number_of_people
    return total_per_person


def total_per_person():
    """Gets user input for bill amount, tip %, and # of people. Returns total per person.

    This function should:
    1. Get user input for the bill amount, tip percentage, and # of people
    2. Calculate the tip amount and save it to a variable.
    3. Using the tip amount calculated above, find the total bill amount.
    4. Using the total found above, calculate the total per person. 
    """

    bill_amount = int(raw_input("What is the bill amount?"))
    tip_percentage = float(raw_input("What is the tip percentage?"))
    num_people = int(raw_input("What is the total amount of people?"))

    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total = calculate_total(bill_amount, tip_amount)#
    total_per_person = split_bill(total, num_people)

    print total_per_person

    

##############################################################################
# Don't touch the code below, this will allow us to run the total_per_person function when we
# run our python file in the terminal using `python bill-calculator.py`

if __name__ == "__main__":
    total_per_person()