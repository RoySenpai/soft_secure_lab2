#     Wordlist generator for the password cracker john the ripper
#     Copyright (C) 2023  Roy Simanovich and Shahar Zaidel
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

WORDLIST = "wordlist.txt"
WORD_RAW = "words.txt"


def generateWordList():
    file = open(WORD_RAW, "r")
    file2 = open(WORDLIST, "w")
    wordlist = file.read().splitlines()
    file.close()

    for word in wordlist:
        word = word.split("-")
        actualWord = word[0].split(" ")

        if len(actualWord) == 1:
            actualWord.append(actualWord[0])

        word1down = actualWord[0].lower()
        word2down = actualWord[1].lower()

        word1Up = actualWord[0].capitalize()
        word2Up = actualWord[1].capitalize()

        file2.writelines(word1down + "\n")
        file2.writelines(word2down + "\n")
        file2.writelines(word1Up + "\n")
        file2.writelines(word2Up + "\n")
        file2.writelines(word1down + word2down + "\n")
        file2.writelines(word1down + word2Up + "\n")
        file2.writelines(word1Up + word2down + "\n")
        file2.writelines(word1Up + word2Up + "\n")
        file2.writelines(word2down + word2down + "\n")
        file2.writelines(word2down + word2Up + "\n")
        file2.writelines(word2Up + word2down + "\n")
        file2.writelines(word2Up + word2Up + "\n")

    file2.close()


if __name__ == '__main__':
    generateWordList()
