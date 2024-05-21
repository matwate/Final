
import datetime
import json


balance: int = 0
operations: list = []

schedulePath = "horario.json"

tasks = []

class Task:
    def __init__(self, name: str, description: str, date: datetime.date):
        self.name = name
        self.description = description
        self.date = date
        tasks.append(self)
    def __str__(self):
        return f"{self.name}: {self.description} - {self.date}"
    def __lt__(self, other):
        return self.date < other.date
    def __eq__(self, other):
        return self.date == other.date
    def __gt__(self, other):
        return self.date > other.date

def loadSchedule():
    with open(schedulePath, "r") as file:
        return json.load(file)
    
schedule = loadSchedule()

def deposit(amount: int,  date: datetime.date) -> str:
    global balance
    global operations
    balance += amount
    
    op =  f"{amount} depositados: {date}"
    operations.append(op)
    
    print(operations)
    return op

def withdraw(amount:int ,purpose:str, date: datetime.date) -> str:
    global balance
    global operations
    
    if balance >= amount:
        balance -= amount
        
        op = f"{amount} retirados para {purpose}, {date}"
        operations.append(op)
        print(operations)   
        return op 
    else:
        return LookupError("Fondos insuficientes")
  
def getBalance() -> int:
    return balance  
  

def getDaySchedule(day: str | int) -> list[dict] | KeyError:
    if type(day) == int:
        dayK = list(schedule.keys())[day]
        return schedule[dayK]
    elif type(day) == str:
        return schedule[day]
    else:
        return KeyError
    
    
def getCurrentClass():
    currentHour = datetime.datetime.today().hour
    currentDay = datetime.datetime.today().weekday()
    for class_ in getDaySchedule(currentDay):
       if class_["HoraInicio"] <= currentHour and class_["HoraFin"] >= currentHour:
           return class_

def NewTask(name: str, description: str, date: datetime.date):
    
    return Task(name, description, date)

currentTask =  getCurrentClass()

