# Coding Challenge 2
# Name: Joge Eduardo Dal Santo Caetano
# Student No: 2038025

# A Morse code encoder/decoder
from os.path import exists as check_file

MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"),
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)


def print_intro():
    print("Welcome to Wolmorse\nThis program encodes and decodes Morse code.")


def get_input(mode):
    #ask a question based on the mode
    msg = ''
    if mode == "d":
        msg = input("What message would you like to decode:")

    elif mode == "e":
        msg = input("What message would you like to encode:")
    return msg


def encode(message):
    morse = ''
    for o in message.upper():#puts word by word inside o
        for i in MORSE_CODE:#puts each tuple inside i
            if o == i[1]:#gets the second object in the tuple and checks if it is equals the l
                morse += i[0] + ' '#add corresponding morse to string
            elif o == ' ':
                morse += '   '
                break
            elif o == '\n':
                morse += '\n'
                morse += ' '
                break
    return morse


def decode(message):
    morse = []
    morse2 = []
    morse3 = ''
    words = message.split('   ')
    for word in words:
        cha = word.split(' ')
        morse.clear()
        for i in cha:
            if i == '\n':# adds new lines so that format can be preserved
                morse.append('\n')
            for o in MORSE_CODE:
                if o[0] == i:
                    morse.append(o[1])
        morse2.append(' '.join(morse))
    for i in range(0, len(morse2)):
        morse3 += morse2[i].replace(" ", "")
        morse3 += ' '
    return morse3


# ---------- Challenge Functions (Optional) ----------


def process_lines(filename, mode):
    input_file = open(filename, 'r')
    line = input_file.readline()
    stir = ''
    while line != '':
        stir += line
        line = input_file.readline()
    input_file.close()

    if mode == 'e':
        return encode(stir).split('\n')
    elif mode == 'd':
        return decode(stir).split('\n')


def write_lines(lines):
    output_file = open('results.txt', 'w')
    for i in lines:
        output_file.write(i + '\n')
    output_file.close()
    print("Done!")


def check_file_exists(filename):
    return check_file(filename)

def get_filename_input():
    ok1 = True
    ok2 = True
    ok3 = True
    file = ''
    form = ''
    while ok1:
        code = input("Would you like to encode(e) or decode(d):")
        if code == 'e' or code == 'd':
            ok1 = False
        else:
            print("Invalid Mode")

    while ok2:
        form = input("Would you like to read from a file (f) or the console (c)")
        if form == 'f' or form == 'c':
            ok2 = False
        else:
            print("Invalid Mode")

    while ok3 and form == 'f':
        file = input("Enter a file name: ")
        if check_file_exists(file):
            ok3 = False
        else:
            print("Invalid Mode")

    return code,form,file


"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encode (e) or decode (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encode/decode.
    • Encode/decode the message as appropriate and print the output.
    • Prompt the user whether they would like to encode/decode another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.

Hints:
    • Use the tuple MORSE_CODE above to convert between plain text/Morse code
    • You can make use of str.split() to generate a list of Morse words and characters
      by using the spaces between words and characters as a separator.
    • You will also find str.join() useful for constructing a string from a list of strings.
    • You should use a loop to keep the programming running if the user says that would like to
      encode/decode another message after the first.
    • Your program should handle both uppercase and lowercase inputs. You can make use of str.upper()
      and str.lower() to convert a message to that case.
    • Check the assessment specification for code examples.
"""


def main():
    state = 'y'
    while state == 'y':
        #code,form,file = get_filename_input()
        get = get_filename_input()
        if get[1] == 'f':
            write_lines(process_lines(get[2],get[0]))

        elif get[1] == 'c':
            if get[0] == 'e':
                print(encode(get_input(get[0])))
            elif get[0] == 'd':
                print(decode(get_input(get[0])))
        state = input("Would you like to encode/decode another message? (y/n)")
        while state != 'y':
            if state == 'n':
                break
            state = input("Would you like to encode/decode another message? (y/n)")
    else:
        print("Thanks for using the program, goodbye!")



    #write_lines(process_lines('morse_input.txt', 'd'))


# Program execution begins here
if __name__ == '__main__':
    main()
