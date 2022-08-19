def greeting(first, last):
    def full_name():
        return f'{first} {last}'
    
    print(f'Hi {full_name()}!')

greeting('Kristine', 'Hudgens')

#best to use when function does not need to exist outside of parent function use the above way.