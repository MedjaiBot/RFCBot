# RFCBot

## About the project

The RFCBot listens for GitHub webhooks on a specified port.

It then creates a Discord message to notify a server about a new created `Request for comments` issue.

## Installation

You need Python 3 to run the bot.

It's your choice if you want to use `virtualenv` or not.

### Using with virtualenv

Initialize the virtual environment with the following command:

```bash
python3 -m virtualenv venv
```

Source the virtual environment with the following command:

```bash
source venv/bin/activate
```

Then proceed with the normal installation.

### Normal installation

#### Install the requirements

Run pip for fetching and installing all the dependencies:

```bash
pip install -r requirements.txt
```

### Editing the secrets

Rename the `.env.dist` file to `.env`.

Edit the entries to the values you want.

Which variable does what?

- `HTTP_INTERFACE` defines on which IP-Adress to listen
- `HTTP_PORT` defines on which port to listen

## Start the bot

Start the bot with the following command:

```bash
python __main__.py
```
