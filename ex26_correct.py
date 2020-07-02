def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): #semi-colon was missing
    """Prints the first word after popping it off."""
    word = words.pop(0) #pop was misspelled
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #close parentheses
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6 #changed last number to 6 instead of 5
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #changed division symbol from \ to /
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #change hyphen to underscore in start_point also change == to =

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point) #correct misspelling of start_point and close parentheses


sentence = "All good things come to those who wait." #correct spellings of good and wait, removed /t as it is not needed.  You could fix this with single quotes too as in line 39.

words = break_words(sentence) #remove references to ex25 for this test.
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words) #remove typo of period
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence) #remove reference to ex25
print sorted_words #misspelled print

print_first_and_last(sentence) #misspelled first.

print_first_and_last_sorted(sentence) #correct tabbing and spelling of and, and of sentence