# FUNCTIONAL PROMPT
# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm

# Using the python sorted() method in the form of a callback function

def order(list):
    return sorted(list)


num_list = [4, 10, 1, 3, 23, 50, 2]
print(order(num_list))

# How does this ensure data immutability?
# This ensures data immutability by maintaining the input values through the sort method, returning all of the same values in a new order as a new list, no values were added or removed.

# Is this solution a pure function?
# Since this function returns a new list, and not the original list, it creates an external variable defined by the sorted list. So the input values were not changed, but their order was, as well as their "owner"

# Is this solution a higher order function?
# Yes, since it is mapping an unsorted iterable into a new, sorted, list (iterable) that requires callback functionality

# Would it have been easier to solve this problem using a different programming style?
# No, using a built in function provided by Python is the most dry/direct way to solve this problem.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# It keeps the code concise and doesn't leave room for any error.

######################################################################################################################################################################################################################

# OBJECT ORIENTED PROMPT

# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented Solution according to the following criteria.
# General Podracer Class


class Podracer():
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        if self.condition == 'trashed':
            self.condition = 'repaired'
        else:
            print("Your podracer does not need to be repaired")


class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def boost(self):
        self.max_speed = self.max_speed * 2
        return self.max_speed


class SebulasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    def flame_jet(self, other_podracer):
        #other_podracer = self.other_podracer
        if other_podracer.condition == 'repaired' or other_podracer.condition == 'perfect':
            other_podracer.condition = 'trashed'
        else:
            print("That podracer was already trashed.")


print("Pod Repair:")
pod = Podracer(100, 'trashed', 10000)
pod.repair()
print(pod.condition)

print("New Pod with Boost:")
new_pod = AnakinsPod(100, 'perfect', 15000)
new_pod.boost()
print(new_pod.max_speed)

print("Third Pod with Flame Jet:")
third_pod = SebulasPod(75, 'perfect', 12500)
third_pod.flame_jet(new_pod)
print(new_pod.condition)


# Is one of these coding paradigms "better" than the other? Why or why not?

# I dont think that either is particularly better, since they both provide different methods of solving a problem. Different problems require different tools to solve them.

# Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?

# OOP since it seems more scalable and captures more data than Functional.

# Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?

# Functional programming appears to be more limited if the dataset is complex, where as OOP is more flexible (appears to be)


# Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?

# Functional because it may require knowing shortcuts that I currently do not know, but feel that I have a lot to learn about both. YouTube should help.
