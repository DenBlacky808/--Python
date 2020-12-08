class Date:
    def __init__(self, date):
        self.date = date
        self.date_list = []

    @property
    def p_method(self):
        date_str_1 = self.date
        return date_str_1

    @classmethod
    def get_date(cls, data):
        try:
            Date.date_list = [int(digit) for digit in data.split('-')]
            return Date.date_list
        except ValueError:
            return [int(faulty) if faulty.isdigit() else faulty for faulty in data.split('-')]

    @staticmethod
    def check_date(obj):
        day, month, year = Date.get_date(obj)
        if day in range(1, 32) and month in range(1, 13) and year in range(1, 9999):
            return True
        else:
            return False


date_1 = Date('06-12-2040')
date_2 = Date('13-O1-2021')
date_3 = Date('01-07-1980')

print(date_1.check_date(date_1.p_method))
print(date_1.get_date(date_1.p_method))
print(date_2.check_date(date_2.p_method))
print(date_2.get_date(date_2.p_method))
print(date_3.check_date(date_3.p_method))
print(date_3.get_date(date_3.p_method))
