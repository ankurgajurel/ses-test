# SES Test Sample Code

This is a sample code for SES Test.

## Installation

1. Clone the repository

```bash
git clone https://github.com/ankurgajurel/ses-test
```

2. Virtual Environment

```bash
cd ses-test
virtualenv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

First, edit env file with your ses credentials
```bash
cp .env.example .env
```

Then, run the following command to send email
```bash
python send_email.py
```
