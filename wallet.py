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
    
    def __init__(self, first_name, last_name):
        """Инициализация экземпляра класса

        args:
            first_name (str): имя
            last_name (str): фамилия
        """
        self.first_name = first_name
        self.last_name = last_name
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
            number (float): денежные средства в USD

        returns:
            _type_: self
        """
        self.amount += number
        return self

    def withdraw_money(self, number):
        """Списание средств

        args:
            number (float): денежные средства в USD

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
            number float): денежны(е средства в USD
            id_send (int): id_obj экземпляра класса

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
            number float): денежны(е средства в USD
        returns:
            _type_: self | False
        """
        return self.add_amount(number)
    
    def __sub__(self, number):
        """Списание средств

        Args:
            number float): денежны(е средства в USD

        Returns:
            _type_: self | False
        """
        return self.withdraw_money(number)
    
    def __str__(self):
        return f"{self.amount} {self.currency}"
    
    






