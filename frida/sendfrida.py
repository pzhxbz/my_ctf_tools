import frida,sys

def on_message(msg,data):
    if msg['type'] == 'send':
        print(msg['payload'])
    else:
        print(msg)
session = frida.get_usb_device().attach("com.example.touchgame")

jscode = open("exp.js","r").read()

script = session.create_script(jscode)
script.on('message',on_message)
script.load()
sys.stdin.read()