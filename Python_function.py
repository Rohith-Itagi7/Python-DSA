def something():
    print("Hello")
    print("Hey how are you?")

something()

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def detials(name):
    print(f"hello {name}")
    print(f"How are you {name}")

detials("Akshya")

#Positional Arguments
def my_function(name,birth):
    print(f"hello {name}")
    print(f"your have born on {birth}")

my_function("Rohith",1989)

#Keyword Arguments
def my_function(name,birth):
    print(f"hello {name}")
    print(f"your have born on {birth}")

my_function(birth=1989,name="Rohith")

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Default Argument
def greet(name, message="Welcome!"):
    print(f"Hello, {name}! {message}")

greet("Charlie") # Uses default message
greet("David", "Nice to meet you!") # Overrides default message