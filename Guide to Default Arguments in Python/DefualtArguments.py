# from gc import collect #this part is for the second example

def greeting(name = 'Guest/User'):
        print(f'Hi {name}!')

greeting()
greeting('Kristine')

#--------------------------------------------------

#WRONG WAY/COMMON INTERVIEW QUESTION, COLLECTION STAYS IN MEMORY AND ADD'S TO IT DUE TO BEING CONNECTED IE [1] THEN [1, 1], has same ID for both.

# def some_function(collection = []):
#     collection.append(1)
#     print(id(collection))
#     return(collection)

# print(some_function())

# #other part of program
# print(some_function())
