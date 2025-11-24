class Adress:
    def __init__(self,city,street,building,flat):
        self.__city = city
        self.__street = street
        self.__building = building
        self.__flat = flat

    @ property
    def city(self):
        return self.__city

    @ property
    def street(self):
        return self.__street

    @ property
    def building(self):
        return self.__building

    def flat(self):
        return self.__flat

    def __str__(self):
        return (f"Город - {self.__city}|Улица - {self.__street} | Дом - {self.__building} | Квартира - {self.__flat}")



