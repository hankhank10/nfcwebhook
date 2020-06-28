import time
import nfc
import requests

# this function gets called when a NFC tag is detected
def touched(tag):

    if tag.ndef:
        for record in tag.ndef.records:
            urltoget = record.text

            print("Read from NFC tag: " + urltoget)
            print ("Fetching URL via HTTP: "+ urltoget)
            r = requests.get(urltoget)
            print ("")

    else:
        print ("Tag Misread - Sorry")

    return True

beep_on_read = False

print("Setting up reader...")
reader = nfc.ContactlessFrontend('usb')
print(reader)
print("Ready!")
print("")

while True:
    reader.connect(rdwr={'on-connect': touched, 'beep-on-connect': beep_on_read})
    time.sleep(0.1);
