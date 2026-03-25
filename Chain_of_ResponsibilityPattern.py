class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, problem):
        if self.next_handler:
            return self.next_handler.handle(problem)
        return f"Проблему '{problem}' ніхто не зміг обробити."

class Receptionist(Handler):
    def handle(self, problem):
        if problem in ["запис на сервіс", "прийом авто", "оформлення заявки"]:
            return f"Приймальник обробив запит: {problem}"
        print(f"Приймальник не може обробити '{problem}', передає далі.")
        return super().handle(problem)

class Diagnostician(Handler):
    def handle(self, problem):
        if problem in ["комп'ютерна діагностика", "помилка на панелі", "невідома несправність"]:
            return f"Діагност обробив проблему: {problem}"
        print(f"Діагност не може обробити '{problem}', передає далі.")
        return super().handle(problem)

class Mechanic(Handler):
    def handle(self, problem):
        if problem in ["заміна масла", "заміна колодок", "ремонт підвіски"]:
            return f"Механік виконав роботу: {problem}"
        print(f"Механік не може обробити '{problem}', передає далі.")
        return super().handle(problem)

class SeniorMotorist(Handler):
    def handle(self, problem):
        if problem in ["ремонт двигуна", "капітальний ремонт мотора", "стукіт у двигуні"]:
            return f"Старший моторист обробив складну проблему: {problem}"
        return super().handle(problem)


receptionist = Receptionist()
diagnostician = Diagnostician()
mechanic = Mechanic()
senior_motorist = SeniorMotorist()

receptionist.set_next(diagnostician).set_next(mechanic).set_next(senior_motorist)

problems = ["прийом авто", "помилка на панелі", "заміна масла", "ремонт двигуна", "заміна авто"]
for problem in problems:
    print("\nЗапит:", problem)
    result = receptionist.handle(problem)
    print("Результат:", result)