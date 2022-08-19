# def greeting(**kwargs):
#     print(kwargs)

# greeting() #returns {} with everything above ^^^

#----------------------------------------------------

# def greeting(**kwargs):
#     print(kwargs)

# greeting(first_name = 'Kristine', last_name = 'Hudgens') #returns {'first_name': 'Kristine', 'last_name': 'Hudgens'}

#-----------------------------------------------------

def greeting(**kwargs):
    if kwargs:
        print(f"Hi {kwargs['first_name']} {kwargs['last_name']}, have a great day!")
    else:
        print(f"Hi Guest, have a great day!")

greeting(first_name = 'Kristine', last_name = 'Hudgens') #returns Hi Kristine Hudgens, have a great day!
greeting() #returns Hi Guest, have a great day!

