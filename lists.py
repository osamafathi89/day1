fruits= ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
print(fruits[0])
fruits[1] = 'blueberry'  # Change 'banana' to 'blueberry'
print(fruits)
fruits.append('honeydew')  # Add 'honeydew' to the end of the list
print(fruits)
fruits.insert(2, 'kiwi')  # Insert 'kiwi' at index 2
fruits.remove("fig")
print(fruits)
for index,fruit in enumerate(fruits):
    print(f"Fruit {index + 1} is {fruit}")