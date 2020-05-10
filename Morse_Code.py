import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
        'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',
        'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.',
        }
DOT_LENGTH = 0.5  #seconds value for dot '.'

def translate_message(message):
    for character in message:
        if character.upper() not in CODE.keys() and character != " ":
            return ""
        else:
            return message #make sure the message only has letters, numbers and spaces

def trigger_led(on_or_off):
    GPIO.output(11,on_or_off) #control on-or-off of the LED

def morse(message):
    morse_code=""
    message=translate_message(message)
    for character in message:
        trigger_led(False)
        time.sleep(DOT_LENGTH*3) #pause between characters
        print(" ")
        if character==" ":
            morse_code += character
            time.sleep(DOT_LENGTH*6) #pause between words
            print("pause between words")
        else:
            for code in CODE[character.upper()]:
                morse_code += code
                time.sleep(DOT_LENGTH) #pause between dots and dashes
                if code==".":
                    trigger_led(True)
                    time.sleep(DOT_LENGTH) #dot will cause the LED to blink for 0.5 sec
                    print(code)
                else:
                    trigger_led(True)
                    time.sleep(DOT_LENGTH*3) #dash will cause the LED to blink for 1.5 sec
                    print(code)
                trigger_led(False)
                    
message=input("Enter a sentence with words and spaces: ")
morse(message)
        
        
        
        
