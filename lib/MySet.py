class MySet:
    def __init__(self, enumerable=None):
        if enumerable is None:
            enumerable = []
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):  # Added self parameter to the has method
        return value in self.dictionary  # Added self before dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):  # Removed space before the parenthesis
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)  # Added return statement

    def clear(self):
        self.dictionary.clear()

    def __str__(self):
        set_list = []
        for key in self.dictionary.keys():  # Removed unused value variable
            set_list.append(str(key))
        return f'Myset: {{{",".join(set_list)}}}'  # Added f before the string


# Testing the MySet class
my_set = MySet([1, 2, 3, 4, 5])
print(my_set)  # Output: Myset: {1,2,3,4,5}
my_set.add(6)
print(my_set)  # Output: Myset: {1,2,3,4,5,6}
my_set.delete(3)
print(my_set)  # Output: Myset: {1,2,4,5,6}
print(my_set.size())  # Output: 5
my_set.clear()
print(my_set)  # Output: Myset: {}
