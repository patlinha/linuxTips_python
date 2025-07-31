
def welcome():
    print("Welcome to the test.")
    input("When you're ready press enter.")

def ask_questions(ask_color=False):
    name = input("Name: ")
    print(f"It's nice to meet you {name}")

    if ask_color:
        color = input("What is your favorite color? ")
        print(f"{color} is a great color!")
    
    input("Describe yourself: ")
    print("admirable!")

def goodbye():
    print("Goodbye.")

welcome()
ask_questions(ask_color=True)
goodbye()