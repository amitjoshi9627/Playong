# Playong
### By Amit Joshi

Playong is a free weekly top-30 songs player from online music streaming website [jiosaavn.com](https://jiosaavn.com).

## Features

1. User Log in option available.
2. Checking Credentials and prompt to user to add the right username/password.
3. Choose numnber of songs you want to play.
4. Song Duration can be manually set by User.
5. Current song and album notification.
6. Logging out user at the end of program.

## Dependencies

Currently only *nix* like Operating Systems are supported.

Requires Python 3.4+ and pip3 for installing and running.

It relies on Firefox headless mode, so make sure you have Firefox version > 56.0 installed, also **geckodriver** is needed, you can follow [Install geckodriver for firefox](https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu) to see how to download and configure it.

For Notifications make sure you have notify2 installed.

*To ensure that firefox headless is supported, enter `$firefox --headless` and see that it works correctly*

*NOTE: This program is tested on Ubuntu 18.04 with Python 3.6, Firefox v64.0 and geckodriver v0.23.0*

## Usage

* Run the file using `python playong.py`.

* It will prompt you for Log in (Currently Log in option is not available due to some error.)

<img src="/Screenshots/ss1.png?raw=true">

* Select the number of songs and their duration(User's choice).

<img src="/Screenshots/ss2.png?raw=true">

* Song information is available via notification.

<img src="/Screenshots/ss3.png?raw=true">

* At the end of the program User is automatically Logged out.

<img src="/Screenshots/ss4.png?raw=true">

#### Thank You!
_Please Give a :star2: if you :+1: it._
