# more experimaentation with strings in Python
#use of formattter to input values into strings

x = "There are  %d types of programmers." % 2
language = "python"
fakes = "dont"
y = "Those who know %s and those who %s." % (language, fakes)
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that true?! %r"

print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."

print w + e