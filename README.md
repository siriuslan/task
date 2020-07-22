# task

To run this application, please follow below
1. Configure your twitter api_key, api_key_secret, access_token and access_token_secret in main.py first.
2. Make sure you have python 3.8 installed on your computer(I develop with 3.8.5).
3. Enter project folder in terminal and run command  - "pip install -r requirements.txt".
4. Run command - "python main.py" and then follow instruction as prompted.

Dockerfile:
1. Make sure complete 1) in above.
2. Make sure docker installed on computer.
3. Enter project folder in terminal and run command - "docker build -t task ." to generate docker file.
4. Run command - "docker run task" to run it.


Assumptions:
1. All tweets get from twitte are all with valid id, created time an text and only save these 3 fields for dump.
2. As there is no specific requirement on how to implement the api to dump all tweets so I implemented by input 'dump' in command line.
