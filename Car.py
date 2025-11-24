class Car:
    def __init__(self,cost,engine_type,engine_power,engine_volume,age_category,registration_number,
                 model,color,is_smuggled = False):
        self.__cost = cost
        self.__engine_type= engine_type
        self.__engine_power = engine_power
        self.__engine_volume = engine_volume
        self.__age_category = age_category
        self.__is_smuggled = is_smuggled
        self.__registration_number = registration_number
        self.__model = model
        self.__color = color

    @property
    def cost(self):
        return self.__cost

    @property
    def engine_type(self):
        return self.__engine_type

    @property
    def engine_power(self):
        return self.__engine_power

    @property
    def engine_volume(self):
        return self.__engine_volume

    @property
    def age_category(self):
        return self.__age_category

    @property
    def is_smuggled(self):
        return self.__is_smuggled

    @property
    def registration_number(self):
        return self.__registration_number

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    def calculate_utill_fee(self):
        base_rates = {
            "бензиновый": 100,
            "дизельный": 200,
            "электро": 0
        }

        age_multipliers = {
            "меньше 3 лет": 1.0,
            "от 3 до 5 лет": 0.8,
            "от 5 до 7 лет": 0.6,
            "старше 7 лет": 0.4
        }

        base_rate = base_rates[self.__engine_type]
        age_multiplier = age_multipliers[self.__age_category]

        if self.__is_smuggled:
            smuggling_penalty = 50000
        else:
            smuggling_penalty = 0


        utill_fee = base_rate * self.__engine_power* age_multiplier + smuggling_penalty
        return round(utill_fee,2)


    def calculate_transport_tax(self):
        tax_rates = {
            "бензиновый": 30,
            "дизельный": 40,
            "электро": 0
        }

        age_tax_multipliers = {
            "меньше 3 лет": 1.0,
            "от 3 до 5 лет": 0.9,
            "от 5 до 7 лет": 0.8,
            "старше 7 лет": 0.7
        }

        tax_rate = tax_rates[self.__engine_type]
        age_multiplier = age_tax_multipliers[self.__age_category]

        transport_tax = tax_rate * self.__engine_power * age_multiplier

        if self.__is_smuggled:
            transport_tax *= 1.2

        return round(transport_tax,2)

    def __str__(self):
        volume_str = "Нет" if self.__engine_type == "электро" else f"{self.__engine_volume} см³"
        return (
            f"Автомобиль: \n"
            f"Стоимость: {self.__cost} ₽\n "
            f"Тип двигателя: {self.__engine_type}\n"
            f"Мощность: {self.__engine_power}\n"
            f"Объём: {volume_str}\n"
            f"Возраст: {self.__age_category}\n"
            f"Растаможено: {'Да' if not self.is_smuggled else 'Нет'}\n"
            f"Утиль сбор: {self.calculate_utill_fee()}\n"
            f"Транспортный налог: {self.calculate_transport_tax()}\n"
            f"Регистрационный номер: {self.__registration_number}\n"
            f"Цвет:{self.__color}\n"
            f"Модель:{self.__model}\n"
        )














