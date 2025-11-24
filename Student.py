class Student:
    def __init__(self,name,age,group_number):
        self.__name = name
        self.__age = age
        self.__group_number = group_number

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def group_number(self):
        return self.__group_number

    def define_gender(self):
        if self.__name [-1]== "а":
            return 'Пол - женский'
        else:
            return 'Пол - мужской'
    def __str__(self):
        return (f" Имя - {self.__name}| Возраст - {self.__age}|Номер группы - {self.__group_number}|{self.define_gender()}")