# def greeting(*args): #can change *args to *names, But is NOT recommended. USE *args due to it being industry standard.
#     print('Hi ' + ' '.join(args))
#     # print(args) shows that it is using tuples.

# greeting('Tiffany', 'Hudgens')
# greeting('Kristine', 'M.', 'Hudgens')

#--------------------------------------------------------------

def greeting(time_of_day, *args):
    print(f"Hi {' '.join(args)}, I hope that you are having a good {time_of_day}")

greeting('Morning', 'Tiffany', 'Hudgens')
greeting('Afternoon', 'Kristine', 'M', 'Hudgens')