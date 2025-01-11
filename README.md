# Serverless Web Scraper Built on AWS
This repository is for my course, https://courses.beabetterdev.com/courses/web-scraping-bot

## Module 1 

### Lesson 2 - Course Pre-requisites
python 3.10+ -> https://www.python.org/downloads/

pip -> https://pip.pypa.io/en/stable/installation/

npm/nvm -> https://nodejs.org/en/download/package-manager

cdk -> npm install -g aws-cdk -> https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html

aws cli -> https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

Docker Desktop -> https://www.docker.com/get-started/...

Discord account -> https://discord.com/

## Module 4 

### Lesson 1 - Finding and Testing Discord Webhook URL

#### Resources
Discord Webhook Documentation - https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks
Discord Homepage - https://discord.com
Discord Webhook URL Tester - https://disforge.com/tool/webhook-tester

### Lesson 2 - CDK Project Setup & Structure

#### Resources
Download VSCode - https://code.visualstudio.com/

#### Initialize CDK Project 
`cdk init app --language python`

#### Activating Virtual Environment
`source .venv/bin/activate (mac)`

`.\.venv\Scripts\activate (windows)`

#### Installing CDK Dependencies
`python -m pip install -r requirements.txt`

#### Bootstrapping CDK project (one-time only)
`cdk bootstrap`

### Lesson 3 - Parameter Store Setup

#### Setting Environment Variables

Remember: you must re-run these commands each time you re-load your code editor. 

Windows:

`$env:DISCORD_WEBHOOK_URL="YOUR DISCORD URL HERE!"`

`echo $env:DISCORD_WEBHOOK_URL`

Mac/Linux:

`export DISCORD_WEBHOOK_URL="YOUR DISCORD URL HERE!"`

`echo $DISCORD_WEBHOOK_URL`

### Lesson 4 - Lambda Docker Image Setup

#### Resources
Docker File Link: https://github.com/beabetterdevv/ServerlessWebScraper/blob/master/StockNotifier/lambda/Dockerfile

## Module 5

### Lesson 1 - Adding Dependencies & Structuring our Project

#### Installing Project Dependencies

`python -m pip install -r requirements.txt`

Note: You may also need to run the following command to install playwright locally

`playwright install`

## Module 6

### Lesson 1 - Writing our Parameter Store Client

#### Resources

Parameter Store boto3 Documentation - https://boto3.amazonaws.com/v1/documentation/api/1.35.6/reference/services/ssm/client/get_parameter.html

#### Setting Environment Variables

Remember: you must re-run these commands each time you re-load your code editor. 

Windows:

`export DISCORD_WEBHOOK_URL_ARN="YOUR PARAMETER STORE ARN HERE!"`

`echo $env:DISCORD_WEBHOOK_URL_ARN`

Mac/Linux:

`export DISCORD_WEBHOOK_URL_ARN="YOUR DISCORD URL HERE!"`

`echo $DISCORD_WEBHOOK_URL_ARN`

### Lesson 2 - Implementing our Discord Publisher

#### Resources

Discord Webhooks & Embeds Documentation - https://discord.com/safety/using-webhooks-and-embeds

## Module 7

### Lesson 1 - Storing Scraping Results in DynamoDB 

#### Resources

DyamoDB Resource Interface - https://boto3.amazonaws.com/v1/documentation/api/1.35.8/reference/services/dynamodb/table/index.html
DynamoDB Client Interface (Low Level) - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html

DynamoDB PutItem API - https://boto3.amazonaws.com/v1/documentation/api/1.35.8/reference/services/dynamodb/table/put_item.html

### Lesson 2 - Retrieving Saved Results from DynamoDB

#### Resources
DynamoDB Query API - https://boto3.amazonaws.com/v1/documentation/api/1.35.9/reference/services/dynamodb/table/query.html
