# Golf Slot Checker

This project will fetch the API of the Troon app and the Viya app to look for golf tee times
It will print the availability for each golf for the number of players (from the max to the less) with the price and the tee.

# Run it
- Open the app.py and set the constants at the top of the file
- Open the terminal
```bash
source ~/.virtualenvs/golf-slots-checker/bin/activate
python app.py
```
- Publish the output to the Whatsapp channel
Output should look like:
```bash
*Sunday 2022-01-09*
Arabian Ranches
    07:00 - 4 joueurs - dh395 - 10th
    08:20 - 2 joueurs - dh395 - 10th
Dubai Hills
    07:00 - 2 joueurs - dh551 - 1st
Fire Course
    08:00 - 4 joueurs - dh795 - Shotgun
Trump International Golf Club
    11:30 - 4 joueurs - dh650 - 1st
```

# Install
## Setup with VirtualEnv
- Create a virtualenv https://virtualenv.pypa.io/en/latest/
```bash
virtualenv ~/.virtualenvs/golf-slots-checker
source ~/.virtualenvs/golf-slots-checker/bin/activate
```

## Pip install
```bash
pip install -r requirements.txt
```

## How to update the bearer
- Launch Charles on the laptop
- Install the SSL certificate on the iOS Phone (see Charles)
    - Search for "profil" and activate the Charles one
    - In General / Informations / Reglage des certificates - activate the Charles certificate
- On iOS, go to the wifi settings and activate the proxy
    - Set the IP to the local IP of the laptop (you can get it from Charles)
    - Port is 8888
- Go to the Viya app and load a page
    - In charles, get the request as CURL and extract the Viya Bearer
- Go to the Troon app and load a page
    - In charles, get the request as CURL and extract the Viya Bearer

