"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


class MonthlySalaryEmployee(Employee):
    def __init__(self, name, base_salary):
        super().__init__(name)
        self.base_salary = base_salary

    def get_pay(self):
        return self.base_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.base_salary}. Their total pay is {self.get_pay()}."


class CommissionEmployee(MonthlySalaryEmployee):
    def __init__(self, name, base_salary, commission_rate, num_contracts):
        super().__init__(name, base_salary)
        self.commission_rate = commission_rate
        self.num_contracts = num_contracts

    def get_pay(self):
        commission = self.commission_rate * self.num_contracts
        return self.base_salary + commission

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.base_salary} and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."


class BonusCommissionEmployee(MonthlySalaryEmployee):
    def __init__(self, name, base_salary, bonus_amount):
        super().__init__(name, base_salary)
        self.bonus_amount = bonus_amount

    def get_pay(self):
        return self.base_salary + self.bonus_amount

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.base_salary} and receives a bonus commission of {self.bonus_amount}. Their total pay is {self.get_pay()}."


class ContractEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def get_pay(self):
        return self.hours_worked * self.hourly_rate

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour. Their total pay is {self.get_pay()}."


class ContractCommissionEmployee(ContractEmployee):
    def __init__(self, name, hours_worked, hourly_rate, commission_rate, num_contracts):
        super().__init__(name, hours_worked, hourly_rate)
        self.commission_rate = commission_rate
        self.num_contracts = num_contracts

    def get_pay(self):
        contract_pay = self.hours_worked * self.hourly_rate
        commission_pay = self.commission_rate * self.num_contracts
        return contract_pay + commission_pay

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a commission for {self.num_contracts} contract(s) at {self.commission_rate}/contract. Their total pay is {self.get_pay()}."


class BonusCommissionContractEmployee(ContractEmployee):
    def __init__(self, name, hours_worked, hourly_rate, bonus_amount):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus_amount = bonus_amount

    def get_pay(self):
        return (self.hours_worked * self.hourly_rate) + self.bonus_amount

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour and receives a bonus commission of {self.bonus_amount}. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlySalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = CommissionEmployee('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractCommissionEmployee('Jan', 150, 25, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = BonusCommissionEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = BonusCommissionContractEmployee('Ariel', 120, 30, 600)
