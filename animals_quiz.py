# This quiz is created by Leituitonga
# Date : 8/03/23
# Demonstrate asking the user questions
# provide multiple choice answers , check if its correct

# This is a function called check().It requires two arguements.
# one list and one user input.It returns True if the user is in the list.
# It returns false if the user is not in the list.

def check(options, user_input):
    if user_input in options:
        return True
    else:
        return False

options = ("cheetah")
question_one = input("What is the fastest land animal? Is it:Goose,Cheetah,Snail,Cat").lower().strip()
# print(check(options, question_one))
if check(options, question_one):
    print("True")
else:
    print("False")

options = ("giraffe")
question_two = input("What is the tallest animal in the world? Is it:Bird,Tiger,Giraffe,Fish").lower().strip()
# print(check(options, question_two))
if check(options, question_two):
    print("True")
else:
    print("False")

options = ("elephant")
question_three = input("What is the largest land animal? Is it:Elephant,Lion,Rainbow,Sunshine").lower().strip()
# print(check(options, question_three))
if check(options, question_three):
    print("True")
else:
    print("False")

options = ("a pride")
question_four = input("What is a group of lions called? Is it:A pride,A flock,Pirates,Backstreet boys").lower().strip()
# print(check(options, question_four))
if check(options, question_four):
    print("True")
else:
    print("False")

options = ("joeys")
question_five = input("What are baby kangaroos called? Is it:Joeys,Lollipops,Bubble gums,School of kangaroos").lower().strip()
# print(check(options, question_five))
if check(options, question_five):
    print("True")
else:
    print("False")

options = ("a colt")
question_six = input("What is a young male horse called? Is it:A colt,A wolf,Unicorn,Tiger").lower().strip()
# print(check(options, question_six))
if check(options, question_six):
    print("True")
else:
    print("False")

options = ("female")
question_seven = input("Are male or female elephants incharge? Is it:Male,Girl,Boy,Female").lower().strip()
# print(check(options, questions_seven))
if check(options, question_seven):
    print("True")
else:
    print("False")

options = ("200 tons")
question_eight = input("How many tons can a blue whale grow to? Is it:2000 tons,890989 tons,200 tons,2323 tons").lower().strip()
# print(check(options, question_eight))
if check(options, question_eight):
    print("True")
else:
    print("False")

options = ("a cob")
question_nine = input("What is a male swan called? Is it:A cob,A cub,Cat,Bat").lower().strip()
# print(check(options, question_nine))
if check(options, question_nine):
    print("True")
else:
    print("False")

options = ("octopus")
question_ten = input("Which animal has three hearts? Is it:Octopus,Cat,Dog,Fish").lower().strip()
# print(check(options, question_ten))
if check(options, question_ten):
    print("True")
else:
    print("False")
# Thank you for answering this quiz