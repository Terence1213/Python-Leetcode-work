import random
import methods

def main():
    lowNum = 10
    highNum = 100
    randNum = random.randint(lowNum, highNum) # Note that both lowNum and highNum are included as the possible random number to be generated.

    names = ["Terence", "Adam", "Ylenia"]

    randName = random.choice(names)
    shuffledNames = random.shuffle(names)

    def do_something(number_one, number_two=5):
        print(number_one)
        print(number_two)

    do_something(3) # Setting number_two=5 in the parameters acts as a default value for if we call the method without entering a value for that paraemeter.
    do_something(3, 10)

    do_something(number_one=10) # You can specify what you're setting the value for in the parameter as is done in this line of code

    # The * makes it so that the programmer can enter as many parameters representing numbers as he wants when calling the method.
    def add_nums(*numbers) -> int:
        total = 0
        for number in numbers:
            total += number
        
        return total

    print(add_nums(5, 10, 13, 12))

    def display_student(**details): # The double ** allows us to enter as many key value pairs within the parameters as we want.
        print("Student details: ")
        for key, value in details.items():
            print(f"{key}: {value}")

    display_student(name="Terence", surname="Portelli", course_applied="Computer Science", age=17)

    methods.say_hello()

if __name__ == "__main__":
    main()