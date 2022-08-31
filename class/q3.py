import random
givenFilename = "samplefile.txt"
with open(givenFilename, 'r') as givenfilecontent:
    file_lines = givenfilecontent.read().splitlines()
    print(random.choice(file_lines))
