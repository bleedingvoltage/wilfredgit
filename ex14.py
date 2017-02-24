#Wilfred Githuka
#Githuka.com
#01 January 2017
#Excercise14

from sys import argv

script, user_name, age = argv
prompt = '> '

print "Hi %s, I'm the %s script.I am %s years old" % (user_name, script, age)
print "I'd really like to ask you a few uestions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you have said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer)
