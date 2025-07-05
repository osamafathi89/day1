name = "Osama"
age = 36    
height = 1.75  # in meters
print(f"The name {name} and the age {age} and the height {height} m")
for i in range(5,10):
    print(i)
    
names = ["Osama", "Ahmed", "Ali"]
for [index,name] in enumerate(names):
    print(f"Name {index + 1} is {name}")
age = input("Enter your age: ")
age = int(age)  # Convert input to integer
if age > 18:
    print(f"{name} is an adult.")
elif age < 18:
    print(f"{name} is a minor.")
else:
    print(f"{name} is exactly 18 years old.")
