def madLib():
    '''
       Mad Lib is game, where user
       enter different inputs, and
       program make story with this
       inputs.
    '''
    
    land = input("Enter name of country/city: ") or "Happy Land"
    name = input("Enter name: ") or "John"
    character = input("Enter character of person: ") or "brave"
    color = input("Enter color: ") or "red"
    
    print("Once upon a time.")
    print("There was a place called " + land)
    print("Where a prince called " + name + " lived.")
    print("The Prince was very " + character)
    print("This prince killed the " + color + " dragon, and saved the princess.")
    
madLib()
