import database

 # this Menu prompt is how we communitcate with the user, guide them for what they want to do.
MENU_PROMPT = """
-- Coffee Bean App -- 

Please Choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preperation method is best for a bean.
5) Exit.

Your Selection:"""

def menu():
    connection = database.connect() #grab the connection
    database.create_table(connection) 

    while(user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
                prompt_add_new_bean(connection)
        elif user_input == "2":
                prompt_see_all_beans(connection)

        elif user_input == "3":
                prompt_find_bean(connection)

        elif user_input == "4":
                prompt_find_best_method(connection)

                print(f"The best preperation method for {name} is: {best_method[2]}")
        else:
              print("Invalid input, please try again!")


def prompt_add_new_bean(connection):
     name = input("Enter new bean")
     method = input("Enter how you've prepared it")
     rating = int(input("Enter your rating score (0-100): "))

     database.add_bean(connection, name, method, rating)

def prompt_see_all_beans(connection):
     beans = database.get_all_beans(connection)

     for bean in beans:
          print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

def prompt_find_bean(connection):
     name = input("Enter bean name to find: ")
     beans = database.get_beans_by_name(connection, name)

     for bean in beans:
          print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_best_method(connection):
    name = input("Enter bean name to find: ")
    best_method = database.get_best_preperation_for_bean(connection, name)

    print(f"The best preparation method for {name} is: {best_method[2]}.")


menu()

