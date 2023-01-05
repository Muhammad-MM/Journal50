
# Notes50

What is Notes50?

Journal50 is a secure privacy-focused journaling application.

Your notebook is stored locally on your computer and is never sent to any server, secured with a private key you provide.

Users are able to keep track of their thoughts and experiences in a safe and private space, knowing that their data is secure.

## Features

* Import button:
  * Users are able to import their .j50 notebook (secured with AES encryption)
* New Journal button:
  * Users are able to create a new notebook, initially a key inputted by the user is required to sign up
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

## Authors

99% of the code for this site was created by me (excluding libraries I used)

A big thank you to @invisifam over at the CS50 discord server for helping me debug my code and squish some bugs (:
