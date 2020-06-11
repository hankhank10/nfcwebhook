# nfcwebhook
Use an NFC tag to call an HTTP request

Simple script which uses the the [nfcpy](https://github.com/nfcpy/nfcpy) library to call the webhook contained in the presented NFC tag

Before using you will need to install nfcpy using the following commands:

```pip install -U nfcpy
python -m nfc
```


This is a trimmed down version of my [vinylemulator](https://github.com/hankhank10/vinylemulator) project which uses NFC tags to play spotify playlists or albums over Sonos.

If you want this to run continuiously you can do so with the following commands:

```sudo npm install -g pm2
pm2 status
pm2 start nfcwebhook/readnfc.py<
pm2 startup systemd
pm2 save
sudo reboot
```
