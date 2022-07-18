def to_underscore(string):
    s = ''
    for letter in str(string):
        if letter.isupper():
            s += '_'+ letter.lower()
        else:
            s += letter
    return s.lstrip('_')



print(to_underscore("TestController"))  # "test_controller"
print(to_underscore("MoviesAndBooks"))  # "movies_and_books"
print(to_underscore("App7Test"))        # "app7_test"
print(to_underscore(1))                 # "1"