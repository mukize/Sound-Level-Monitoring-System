
# Sound Level Monitor System

Server and client code to monitor when sounds peaks in a room remotely
Supports using Pi GPIO pins or audio devices.

## Installation

1. Requires at least Python 3.5+
2. Install requirements:
```sh
pip install -r server_requirements.txt
```
3. Copy `.example_env` to `.env` and adjust necessary values.

## Usage

The client can be ran with `python src/client.py`.

You can run either one of two files for the server:
1. `pi_server.py` for using GPIO pins,
2. `audio_server.py` for using audio devices.

