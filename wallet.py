"""Модуль для создания экземпляров кошельков и операций с ними

Функции:
    __init__(): инициализация кошелька;
    add_amount(): пополнение средств в кошельке;
    withdraw_money(): списание средств с кошелька;
    send_money(): переслать деньги с кошелька на другой кошелек;
    __add__(): пополнение средств в кошельке через оператор "+";
    __sub__(): списание средств с кошелька через оператор "-";
    __str__(): строковое представление экземпляра класса Wallet
"""


import random


class Wallet:
    """Создание экземпляров кошельков и операций с ними

    returns:
        _type_: self
    """
    dct_id = {}  # словарь[self.id_obj] = self
    
    def __init__(self, first_name, last_name, currency='USD'):
        """Инициализация экземпляра класса

        args:
            first_name (str): имя
            last_name (str): фамилия
        """
        self.first_name = first_name
        self.last_name = last_name
        self.currency = currency # Валюта
        while True:  # генерирование уникального id объекта
            temp = random.randint(1, 1_000_001)
            if temp not in Wallet.dct_id:
                self.id_obj = temp
                Wallet.dct_id[self.id_obj] = self
                break
        self.amount = 0.0  # Количество денег

    def add_amount(self, number: float):
        """Пополнение средств

        args:
            number (float): денежные средства в USD

        returns:
            _type_: self | False
        """
        if number <= 0:
            print("Сумма пополнения должна быть положительной")
            return False
        self.amount += number
        return self

    def withdraw_money(self, number: float):
        """Списание средств

        args:
            number (float): денежные средства в USD

        returns:
            _type_: self | False
        """
        if number <= 0:
            print("Сумма списания должна быть положительной")
            return False
        if number > self.amount:
            print("Недостаточно средств на балансе")
            return False
        self.amount -= number
        return self
        
        
    def send_money(self, number: float, id_send: int):
        """Переслать деньги с кошелька на кошелек

        args:
            number (float): денежные средства в USD
            id_send (int): id_obj экземпляра класса

        returns:
            _type_: self | False
        """
        if self.currency != Wallet.dct_id[id_send].currency:
            print("Нельзя перевести между кошельками с разной валютой")
            return False
        if number <= 0:
            print("Сумма списания должна быть положительной")
            return False
        if number > self.amount:
            print("Недостаточно средств на балансе")
            return False
        self.amount -= number
        Wallet.dct_id[id_send].add_amount(number)
        return self

    def __add__(self, number):
        """Пополнение средств через оператор "+"

        args:
            number (float): денежные средства в USD
        returns:
            _type_: self | False
        """
        if not isinstance(number, (int, float)):
            return NotImplemented
        return self.add_amount(number)
    
    def __sub__(self, number):
        """Списание средств через оператор "-"

        Args:
            number (float): денежные средства в USD

        Returns:
            _type_: self | False
        """
        if not isinstance(number, (int, float)):
            return NotImplemented
        return self.withdraw_money(number)
    
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    







