import json
import datetime


saldo = 0
operations = []


def GetBalance():
    return saldo

def deposit(amount : int, date:datetime.date):
    global saldo
    global operations
    if amount <=0 :
        return ValueError
    else:
        saldo += amount 
    
    operations.append(f"Se deposito {amount}: {date}")
        

def withdraw(amount: int, purpose:str , date:datetime.date):
    global saldo
    global operations
    if saldo < amount:
        return ValueError
    else:
        saldo -= amount
    operations.append(f'Se retiro {amount} para {purpose}: {date}')

schedulePath = "horario.json"
tasks = []


def loadSchedule():
    data = None
    with open(schedulePath, "r") as f:
        data = json.load(f)
        
    return data

schedule = loadSchedule()

def GetDayClasses(day: int| str):
    if type(day) == int:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        dayStr = days[day]
        return schedule[dayStr]
        
    elif type(day) == str:
        return schedule[day]
        
    else:
        return ValueError

def GetCurrentClass():
    currentHour = datetime.datetime.today().hour   
    currentDay = datetime.date.today().weekday()
    if currentDay > 4:
        return ValueError
    
    for class_  in GetDayClasses(currentDay):
        start = class_["HoraInicio"]
        end = class_["HoraFin"]
        if currentHour in range(start, end+1):
            return class_
        
    
    
class Task:
    def __init__(self, name: str, description: str, date: datetime.date):
        self.name = name
        self.description = description
        self.date = date
        tasks.append(self)
    def __str__(self):
        return f"{self.name}:{self.description}:{self.date}"
    
    def __lt__(self, other):
        return self.date < other.date
    def __eq__(self, other):
        return self.date == other.date
    def __gt__(self, other):
        return self.date > other.date
        
        