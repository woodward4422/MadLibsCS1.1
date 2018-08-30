# This is the MadLibs project created by Noah Woodward 
import random 

inital_story = ["There once was a (Noun) at (Noun), who loved to (Verb) and would always (Verb).", "At Make School, it is said that you can see a (Noun) and a (Noun), and can be seen (Verb), but they are also know to be (Verb)"]
def get_Initial_Story():
    return random.choice(inital_story)
def display_first_story(story): 
    print(story)
def test():
 story = get_Initial_Story()
 display_first_story(story)


test()

