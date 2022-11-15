
# Journal50

What is Journal50?

Journal50 is a secure privacy-focused journaling application.

Your journal is stored locally on your computer and is never sent to any server, secured with a private key you provide.

Users are able to keep track of their thoughts and experiences in a safe and private space, knowing that their data is secure.

## Features

* Import button:
  * Users are able to import their .j50 journal (secured with AES encryption)
* New Journal button:
  * Users are able to create a new journal, initially a key inputted by the user is required to sign up
* Export Journal:
  * Data is encrypted with the same key used to decrypt before being downloaded back to the client
* Date selector:
  * Select date, month and year in the following format dd/mm/yyyy --> a calender is also implemented
* Time selector:
  * Select time in the format --:--
* Title & content inputs:
  * Self explanatory
* Submit button:
  * Submits the entry into the journal
* List button:
  * Lists all the entries in the journal
  * Users are also able to click on an entry to edit it --> if the content is different the entry is updated

 
## The Tech
- Python
- HTML
- Javascript
- Bootstrap
- Crypto-JS and FileSaver.js
Crypto-JS is an amazing library that allows for AES encryption of text. 

Using this library means that the journals of users will be secure, protected by a key they come up with.

FileSaver.js makes exporting files simpler, and easier to handle from the backend.

Bootstrap is used for the design of the website, making the user experience richer and more enjoyable.
## How do I install this?


Install the requirements in python virtual environment with the following command:
```
pip3 install -r requirements.txt
```

Then, simply run using 

```
flask run
```

By default, flask opens the website on PORT 5000.
## Files

- app.py - Contains the serversided code which keeps the website up and running --> routes are also handled here
- templates/layout.html - Acts as a HTML template for other files
- templates/index.html - Contains the main code for the website, most of the clientsided JavaScript code which makes the site function is also stored here
- The static folder contains the libraries used for this project (excluding bootstrap)

## Contributing

Contributions are always welcome!

Open a pull request to get started

## Scrapped Features

Originally, I was planning to implement a login and register page, handling the DB with SQL

The implementation of tags --> I never got around to this as I thought it was unnecessary

A search function --> Allows you to filter journal entries (e.g by title, date, time etc.)

Forced secure keys --> Forcing validation checks on the users to create a more secure key --> I figured this would be annoying to the user

Fun Fact:

My original final project was planned to be a metasearch engine, a secure version of Google. Users would have to host their own proxy servers, in which my site would tunnel through them --> I figured this would be a hassle and that there are other great metasearch engines out there which do the same thing e.g SEARXNG


## Authors

99% of the code for this site was created by me (excluding libraries I used)

A big thank you to @invisifam over at the CS50 discord server for helping me debug my code and squish some bugs (:
