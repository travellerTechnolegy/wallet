import random


class Wallet:
    """Создание экземпляров кошельков и операций с ними

    returns:
        _type_: self
    """
    dct_id = {}  # словарь[self.id_obj] = self
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name  # Имя
        self.last_name = last_name  # Фамилия
        self.currency = 'USD' # Валюта
        while True:  # генерирование уникального id объекта
            temp = random.randint(1, 1_000_001)
            if temp not in Wallet.dct_id:
                self.id_obj = temp
                Wallet.dct_id[self.id_obj] = self
                break
        self.amount = 0.0  # Количество денег

    def add_amount(self, number):
        """Пополнение средств

        args:
            number (_type_): float

        returns:
            _type_: self
        """
        self.amount += number
        return self

    def withdraw_money(self, number):
        """Списание средств

        args:
            number (_type_): float

        returns:
            _type_: self | False
        """
        if number <= self.amount:
            self.amount -= number
            return self
        else:
            return False
        
    def send_money(self, number, id_send):
        """Переслать деньги с кошелька на кошелек

        args:
            number (_type_): float
            id_send (_type_): int

        returns:
            _type_: self | False
        """
        if number <= self.amount:
            self.amount -= number
            Wallet.dct_id[id_send].add_amount(number)
            return self
        else:
            return False
        
    def __add__(self, number):
        """Пополнение средств

        args:
            number (_type_): float

        returns:
            _type_: self | False
        """
        return self.add_amount(number)
    
    def __sub__(self, number):
        """Списание средств

        Args:
            number (_type_): float

        Returns:
            _type_: self | False
        """
        return self.withdraw_money(number)
    
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    






