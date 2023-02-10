# =====================================================================
# Day 1 Challange: Band Name Generator
# =====================================================================
# [Task]:
# Create a Band Name Generator, which combines home city and pet's name
# of user into a cool band name.



# [Solution]:
def main()->None:
    print("Welcome to the Band Name Generator.")
    home_city = input("What's the name of the city you greq up in ?\n")
    pet_name = input("What's your pet's name ?\n")
    print("Your band name could be: " + home_city + " " + pet_name + " !")
    return



if __name__ == '__main__':
    main()
