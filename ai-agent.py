class AIAgent:
    def __init__(self, name, age=0, height=0.0):
        self.name = name
        self.age = age
        self.height = height
        self.skills = ['running', 'jumping', 'coding']

    def greet(self):
        return f"Hello, I am {self.name}, your AI assistant!"

    def perform_task(self, task):
        return f"Performing task: {task}"
p1 = AIAgent("Osama", 36, 1.75)
print(p1.greet())
print(p1.perform_task("Write a Python script"))
print("Skills : ", ", ".join(p1.skills))