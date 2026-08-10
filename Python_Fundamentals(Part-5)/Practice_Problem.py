
'''This is a demo file
to store some words
for the Python activity
that is to be solved by us.

#*Find the word "Python" in Sample.txt, also print the line no
'''

data = True
line = 1
word = "Python"

with open("sample.txt","r") as f:
    while data:
        data = f.readline()

        if word in data:
            print(f"{word} found at line {line}")
            break

        line+=1


