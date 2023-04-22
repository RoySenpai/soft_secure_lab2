# Introduction to Software Security Assignment (Laboratory) 2
### For Computer Science B.S.c Ariel University

**By Roy Simanovich and Shahar Zaidel**

## Description
This is a demonstration of John the Ripper capabilities to crack passwords via
a generated wordlist based on some criteria. In our example, the user's password is
a Disney character.

## Requirements
* Linux machine
* Python 3
* John the Ripper

## Running
```
# Start the python3 script to generate the wordlist based on the Disney characters names.
python3 main.py

# Activate John the Ripper program on encrypted password that stored in mypass file via the generated wordlist.
john --wordlist:wordlist.txt mypass

# Show cracked password result.
john --show mypass
```
