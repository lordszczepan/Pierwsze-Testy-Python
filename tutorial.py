# int
lesson_number = 1
print(lesson_number, type(lesson_number))

# string
lesson_name = "python tutorial"
print(lesson_name, type(lesson_name))

# list
tweet_lenght = [140, 80, 20, 105]
print(tweet_lenght, type(tweet_lenght))

# tuple
tweet_lenght_inmutable = (140, 80, 20, 105)
print(tweet_lenght_inmutable, type(tweet_lenght_inmutable))

# dict
tweet_by_user = {
    'klucz': 'wartość',
    'John': [1, 15],
    'Marry': [2, 5]
}

print(tweet_by_user, type(tweet_by_user))
print(tweet_by_user['John'])

# if
if False:
    print("Yes")
else:
    print("No")

x = ['test']
if type(x) == int:
    print("This is int")
elif type(x) == str:
    print("This is str")
else:
    print("I don't know")

# for
for tweet in tweet_lenght:
    print(tweet)

for x in range(len(tweet_lenght)):
    print(tweet_lenght[x])


def print_line():
    print("=====")


print_line()


def type_print(var):
    print(var, type(var))


type_print(1)


def custom_print(var, list_var=None, *args, **kwargs):
    print_line()
    print("Start")
    print("Var:", var)
    if list_var:
        for element in list_var:
            print("List Var:", element)
    print("Args", args)
    print("KwArgs", kwargs)
    print("End")


custom_print(1)
custom_print(1, [2, 3, 4])

custom_print(1, [2, 3, 4], 'arg3', 'arg4', arg5=1, arg6={'test': 'python'})
