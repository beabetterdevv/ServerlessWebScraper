# Serverless Web Scraper Built on AWS
This repository is for my course, https://courses.beabetterdev.com/courses/web-scraping-bot

## Requirements
python 3.10+ -> https://www.python.org/downloads/

pip -> https://pip.pypa.io/en/stable/installation/

npm/nvm -> https://nodejs.org/en/download/package-manager

cdk -> npm install -g aws-cdk -> https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html

aws cli -> https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

Docker Desktop -> https://www.docker.com/get-started/...

Discord account -> https://discord.com/

## Useful Commands
### Creating CDK project
`cdk init app --language python`

### Activating Virtual Environment
`source .venv/bin/activate (mac)`

`.\.venv\Scripts\activate (windows)`

### Bootstrapping CDK project (one-time only)
`cdk bootstrap`

### Setting Environment Variables
Remember: you must re-run these commands each time you re-load your code editor. 

Mac:

`export DISCORD_WEBHOOK_URL="YOUR DISCORD URL HERE!"`

`export DISCORD_WEBHOOK_URL_ARN="YOUR PARAMETER STORE ARN HERE!"`

Windows:

`$env:DISCORD_WEBHOOK_URL="YOUR DISCORD URL HERE!"`

`$env:DISCORD_WEBHOOK_URL_ARN="YOUR PARAMETER STORE ARN HERE!"`

### Installing Lambda dependencies locally
`pip install -r lambda/requirements.txt -t lambda/`

### Deploying CDK Project
`cdk deploy`

### Destroying CDK Project (clean up)
`cdk destroy`