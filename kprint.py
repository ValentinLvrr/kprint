def kprint(word, delay):
    from time import sleep
    word = list(word.strip())
    for letter in word:
        print(letter, end="", flush=True)
        sleep(delay)
    print("")

def kinput(word, delay):
    from time import sleep
    word = list(word.strip())
    for letter in word:
        print(letter, end="", flush=True)
        sleep(delay)
    text = input()
    return text

"""
-----------------------------------------------

 ALERT | Spaces are not supported

-----------------------------------------------

 PRINT | Example : kprint("Hello World", 0.05)
                      |         |          |
                  fonction    text       delay

-----------------------------------------------

 INPUT | Example : text = kinput("Enter text : " 0.05)
                            |         |            |
                         fonction    text         delay

-----------------------------------------------
"""
