class MyException(Exception):

    def division_func(self, a, b):
        try:
            res = round(a / b, 2)
        except ZeroDivisionError:
            print(f"{a} / {b} - на ноль делить нельзя!")
        else:
            print(f"{a} / {b} = {res}")


m_e = MyException()

m_e.division_func(10, 5)
m_e.division_func(10, 3)
m_e.division_func(3, 0)
m_e.division_func(0, -5)