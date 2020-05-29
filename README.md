# nfcwebhook
Use an NFC tag to prompt a webhook

Simple script which uses the the <a href="https://github.com/nfcpy/nfcpy">nfcpy</a> library to call the webhook contained in the presented NFC tag

Before using you will need to install nfcpy using the following commands:

<code>pip install -U nfcpy</code>

<code>python -m nfc</code>


This is a trimmed down version of my <a href="https://github.com/hankhank10/vinylemulator">vinylemulator</a> project which uses NFC tags to play spotify playlists or albums over Sonos.

If you want this to run continuiously you can do so with the following commands:

<code>sudo npm install -g pm2</code>

<code>pm2 status</code>

<code>pm2 start nfcwebhook/readnfc.py</code>

<code>pm2 startup systemd</code>

<code>pm2 save</code>

<code>sudo reboot</code>
