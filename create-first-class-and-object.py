# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Students:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1 = Students("Harry", 32, "Male")
    print('Students:', s1.name, s1.age, s1.gender)
    s1.name = "Sejal"
    s1.age = 20
    s1.gender = "female"
    print('Students:', s1.name, s1.age)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
