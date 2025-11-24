from Student import Student
from Car import Car
from Adress import Adress

if __name__ == '__main__':
    student1 = Student("Иван",20,110)
    print(student1)
    student2 = Student("Варвара",21,110)
    print(student2)
    student3 = Student("Анна",19,111)
    print (student3)
    car1 = Car(500000,"бензиновый",200,4000,"меньше 3 лет","А223БВ337","Kia Sportage","черный",is_smuggled=False)
    print(car1)
    car2 = Car(1500000,"дизельный", 300, 3000,"старше 7 лет", "А223БВ337", "Skoda Yeti","белый",is_smuggled=False)
    print(car2)
    car3 = Car(13000000,"электро", 700, 3000,"от 5 до 7 лет", "А223БВ457", "Tesla Model S","морозный голубой",is_smuggled=False)
    print(car3)
    adress1 = Adress("Москва", "Тургеневская",11,5)
    print(adress1)
    adress2 = Adress("Тула","Терешковой",12,25)
    print(adress2)
    adress3 = Adress("Краснодар", "Королева", 8, 3)
    print(adress3)
