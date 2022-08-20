def greeting(time_of_day, *args, **kwargs):
    print(f"Hi {' '.join(args)}, I hope you are having a great {time_of_day}")

    if kwargs:
        print('Your task for the day are as follows:')
        for key, val in kwargs.items():
            print(f"{key} => {val}")

greeting('morning!',
        'Kristine', 'Hudgens',
        First = 'Empty dishwasher',
        Second = 'Take puppy outside',
        Third = 'Math homework')