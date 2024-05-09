# Define two classes, one of which inherits from another.
# Define methods in the child class that use the super keyword to inherit from and augment methods in the parent class.


class Student:
    def __init__(self, greeting="Hey there! I'm so excited to learn stuff."):
        self.greeting = greeting

    def hello(self):
        print(self.greeting)

    def raise_hand(self):
        print("Pick me!")

class ChattyStudent(Student):
    def hello(self):
        super().hello()  
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()
