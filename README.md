# Scratch Bot

A telegram bot for vaccination tracking using mysql

## Requirements

- Python 3^
- Git
- A sound mind

## Setup

Clone the repo and install the dependencies.

```bash
git clone https://github.com/barbara99/vaccinationbot.git
cd vaccinationbot
```

```bash
python -m pip install virtualenv
python -m venv env
source env/bin/activate
```

```bash
python -m pip install -r requirements.txt
```

Configure environment variables

```bash
# create an env file
cp .example.env .env

#create a python file 
cp db_copy.py db.py
```

Open up the env file and add up telegram token

Open the python file and replace "host", "user", "password", "database" 

## Running The Bot

To run the bot, run the following

```bash
python vaccinationbot.py
```

Open [http://t.me/wordpuzzlegamebot](http://t.me/wordpuzzlegamebot) and play around.
