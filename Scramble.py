import random
import pyperclip
def scramble(source):
    if len(source) > 1: #Ensures the word is more than two letters long
        result = []
        new = list(source) #Turns word into a list to scramble with shuffle()
        length = len(new)
        result.append(new[0]) #Places first letter into new string, saves last, then scrambles the rest in order to prevent first and last letters from changing
        end = new[length - 1]
        if not end.isalpha():
            end = new[length - 2] + new[length - 1]
            del new[length - 2]
            del new[length - 2]
        else:
            end = new[length - 1]
            del new[length - 1]
        del new[0]
        random.shuffle(new)
        result.append(''.join(new))
        result.append(end)
        return ''.join(result)#Returns the word from a scrambled list to a string
    else:
        return source
def answer(source):
    final = ""
    new_source = source.split()
    for i in new_source: #Takes each word as separated by a space and sends it to scramble, then adds scrambled word to final string with a space to make up for split() removing them
        final += scramble(i) + " " 
    return final[:-1]
again = "y"
while again == "y":
    Text = raw_input("Please enter the sentence: ")
    gg = answer(Text)
    print "\n" + gg
    pyperclip.copy(gg)
    again = raw_input("\n" + "Would you like to go again? Y/N" + "\n")
