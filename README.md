# angel-enrichment
Backend service that enriches technical indicators from Angel surveys to provide additional context to an individual's situation

#### First Steps
1. Create a Python3.6 virtualenv in the root of the git folder
2. pip3 install all requirements
3. `chmod +x scripts/bootstrap.sh`
4. Use .env-example as a template to populate .env
5. Run `scripts/bootstrap.sh`

#### Deploying to Heroku
1. Fork this repo
2. Create a new Heroku Project
3. Connect to Github and select correct repo
4. Populate .env variables in Heroku Config section
5. Make a commit to master