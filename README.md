
# Sound Level Monitor System

Server and client code to monitor sound intensity levels using a Raspberry Pi.

## Installation

### General Requirement

- Python 3.5+

### Server

```sh
pip install -r requirements.txt
```

For the Raspberry Pi Lite OS, `pulseaudio` needs to be installed:
```sh
sudo apt install -y python3-pip python3-numpy pulseaudio
sudo nano /usr/share/pulseaudio/alsa-mixer/profile-sets/default.conf
# comment the block [Mapping analog-mono] with ';'
pulseaudio -D
```

