def welcome_message():
  text = """
  *********************************************
  **  Welcome to Mad Libs! Mad Libs is a     **
  **  fill-in-the-blank word game. Type in   **
  **  a word satisfying the request and I    **
  **  will return a funny story for you.     **
  *********************************************
  """
  print(text)
welcome_message()

def read_file():
    Adjective1 = input('Enter Adjective: ')
    Adjective2 = input('Enter Adjective: ')
    A_First_Name = input('Enter First Name: ')
    Past_Tense_Verb = input('Enter Past Tense Verb: ')
    Adjective3 = input('Enter Adjective: ')
    Adjective4 = input('Enter Adjective: ')
    Plural_Noun1 = input('Enter Plural Noun: ')
    Large_Animal = input('Enter Large Animal: ')
    Small_Animal = input('Enter Small Animal: ')
    A_Girl_Name = input("Enter A Girl's Name: ")
    Adjective5 = input('Enter Adjective: ')
    Plural_Noun2 = input('Enter Plural Noun: ')
    Adjective6 = input('Enter Adjective: ')
    Plural_Noun3 = input('Enter Plural Noun: ')
    Number = input('Enter Number 1-50: ')
    Plural_Noun4 = input('Enter Plural Noun: ')
    Plural_Noun5 = input('Enter Plural Noun: ')

    story = f"""
    Make Me A Video Game! I the {Adjective1} and {Adjective2} {A_First_Name} have {Past_Tense_Verb} {A_First_Name}'s 
    {Adjective3} sister and plan to steal her {Adjective4} {Plural_Noun1}! What are a {Large_Animal} and backpacking 
    {Small_Animal} to do? Before you can help {A_Girl_Name}, you'll have to collect the {Adjective5} {Plural_Noun2}
    and {Adjective6} {Plural_Noun3} that open up the {Number} worlds connected to A {A_First_Name}'s Lair. There are
    {Number} {Plural_Noun4} and {Number} {Plural_Noun5} in the game, along with hundreds of other goodies for you to find.
    """

    return story
    
    # with open('example_text.txt', 'r+') as f:
    #     text = f.read()
    #     return (text.replace('Adjective1', Adj1).replace('Adjective2', Adj2).replace('Noun', Noun))

print(read_file())
