"""Instructions
Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

Add a method for interacting with a pizza's toppings, called add_topping.

Add a method for outputting a description of the pizza (sample output below).

Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()
You should produce output in the terminal similiar to the following string.

"I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."""

class Pizza:
    def __init__(self):
        self.size = ""
        self.toppings = []
        self.crust_type = ""

    def add_topping(self, new_topping):
        self.toppings.append(new_topping)

    # Add a method for outputting a description of the pizza (sample output below).
    
    def make_pizza(self):
        
            if len(self.toppings) == 1:
                print(f"I would like a {self.size} inch, {self.crust_type} pizza with {''.join(self.toppings)}.")
            elif len(self.toppings) > 1:
                sentence = f"I would like a {self.size} inch, {self.crust_type} pizza with"

            for index, topping in enumerate(self.toppings):
                # if else statement
                # if topping is last item in list, then add different string
                # print(index)
                if index == len(self.toppings) - 1:
                    sentence += f"and {''.join(topping)}."
                    
                else: 
                    sentence += f" {''.join(topping)}, "
    
            print(sentence)
            


meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.crust_type = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.add_topping("Poop")
meat_lovers.make_pizza()
