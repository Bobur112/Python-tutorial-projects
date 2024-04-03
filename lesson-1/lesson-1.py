#print("Hello world")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

fruits.discard("banana")
print(fruits)


def my_function(**kids):
    print("The youngest child is " + kids[2])
my_function()