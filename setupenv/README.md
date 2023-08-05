# Hugging Face Environment Setup

This tutorial explain how to create a Python Virtual Environment.

## Prerequisites

We assume you've already installed Python 3.11 or next versions on your computer.

## How to install the Python 3 Virtual Environment

To create a Python Virtual Environment use the following commands:

```
python3 -m venv .env
```

This will create a `.env` folder of 23 Mb with a Python Virtual Environment where you can install the dependencies and run your 
tutorials without affect the Global Python Environment.

## Activate and Deactivate your Python Virtual Environment

You can activate the Python Virtual Environment with the command:

```
source .env/bin/activate
```

Once in the Python Virtual Environment you can install dependencies with the command:

```
pip3 install -r requirements.txt
```

Then you can run your tutorials without affect the Global Python Environment. When you finished you can deactivate the environment with 
the command:

```
deactivate
```
 
