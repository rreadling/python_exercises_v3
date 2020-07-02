from sys import argv

#script calls an argument defined at execution
script, user_name = argv
#prompt can be anything as long as it is quoted
prompt = '> '


#takes the argument provided and uses the script name
#stores input in the likes variable
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

#stores input in lives variable
print "Where do you live %s?" % user_name
lives = raw_input(prompt)

#stores input in computer variable
print "What kind of computer do you have?"
computer = raw_input(prompt)

#uses style multi-line string and shows all user inputs
print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
