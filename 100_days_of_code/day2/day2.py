# =====================================================================
# Day 2 Challange: Tip Calculator
# =====================================================================
# [Task]:
# Create a tip calculator that calculates the amount of money each person
# on your table needs to cover from the bill, when you would like to give
# a certain tip in percent.



# [Solution]:
def main()->None:

    print("Welcome to the tip calculator.")

    # request the required variables
    bill = float(input("What was the total bill? $"))
    number_of_people = int(input("How many people to split the bill? "))
    tip_perc = float(input("What percentage tip would you like to give? "))

    # calculate the amount each person need to pay
    total_bill = bill * (1 + tip_perc/100)
    amount_per_person = round(total_bill / number_of_people,2)
    print(f"Each person should pay: ${amount_per_person}")
    return



if __name__ == '__main__':
    main()
