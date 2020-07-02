from sys import argv

#script calls an argument defined at execution
script, user_name = argv
#prompt can be anything as long as it is quoted
prompt = '> '


#takes the argument provided and uses the script name
#stores input in the likes variable
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

#stores input in lives variable
print(f"Where do you live {user_name}?")
lives = input(prompt)

#stores input in computer variable
print("What kind of computer do you have?")
computer = input(prompt)

#uses style multi-line string and shows all user inputs
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.
""")
