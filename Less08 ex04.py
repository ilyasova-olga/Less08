class OfficeEquipmentWarehouse:
    print("Склад")


class OfficeEquipment:
    def __init__(self, producer, color):
        self.producer = producer
        self.color = color


class Printer(OfficeEquipment):
    amount_pr = 0

    def __init__(self, producer, color, pr_type):
        super().__init__(producer, color)
        self.pr_type = pr_type
        Printer.amount_pr += 1

    @staticmethod
    def name():
        return "Принтер"

    def type_printer(self):
        return self.pr_type

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}  \tтип принтера: {}".format(self.producer, self.color, self.pr_type)


class Scanner(OfficeEquipment):
    amount_sc = 0

    def __init__(self, producer, color, sc_sensor):
        super().__init__(producer, color)
        self.sc_sensor = sc_sensor
        Scanner.amount_sc += 1

    @staticmethod
    def name():
        return"Сканер"

    def type_sensor(self):
        return self.sc_sensor

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {} \tтип сенсора: {}".format(self.producer, self.color, self.sc_sensor)


class Xerox(OfficeEquipment):
    amount_x = 0

    def __init__(self, producer, color, xer_wi_fi):
        super().__init__(producer, color)
        self.xer_wi_fi = xer_wi_fi
        Xerox.amount_x += 1

    @staticmethod
    def name():
        return "Ксерокс"

    def wi_fi_module(self):
        return self.xer_wi_fi

    def __str__(self):
        return "\tпроизводитель: {} \tцвет: {}   \tWi-Fi модуль: {}".format(self.producer, self.color, self.xer_wi_fi)


p = Printer('Canon', 'white', 'струйный')
p2 = Printer('HP', 'blue', 'лазерный')
print(p.name(), p.amount_pr, "шт")
print(p.__str__())
print(p2.__str__())


s = Scanner('HP', 'black', 'CIS')
s2 = Scanner('Epson', 'white', 'CCD')
s3 = Scanner('Kodak', 'yellow', 'CMOS')
print(s.name(), s.amount_sc, "шт")
print(s.__str__())
print(s2.__str__())
print(s3.__str__())


x = Xerox('HP', 'white', 'есть')
x2 = Xerox('Phaser', 'black', 'есть')
x3 = Xerox('Xerox', 'white', 'есть')
x4 = Xerox('Pantum', 'red', 'отсутствует')
print(x.name(), x.amount_x, "шт")
print(x.__str__())
print(x2.__str__())
print(x3.__str__())
print(x4.__str__())