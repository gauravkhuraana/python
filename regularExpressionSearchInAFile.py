#SAMPLE.TXT
#Hello World!
#I am a sample file.
#Hello and goodbye!
import re
pattern = re.compile("^Hello")

for line in open("sample.txt"):
    for match in re.finditer(pattern, line):
        print(line)