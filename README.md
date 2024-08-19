# Fundraiser Logger

## Project Description

Are you tired of manually checking the status of the fundraiser programs you support?
This project aims to create a simple and interactive enviornment for checking the status of supporing fundraiser projects and logging the progress over time.
The application will offer both automatic and manual checking/logging.
The logged data will be stored as a CSV file, and the application will be able to plot the fundraiser progress to analyze the particiption rate over time.

## Stack

* Python
* Beautiful Soup

## Supported Fundraiser Websites

* [CAMPFIRE](https://camp-fire.jp/)
* [Kickstarter](https://www.kickstarter.com/)

## To Be Implemented

* A simple CLI environment.
* A savable settings.
* CSV file I/O.
* A plot generator (raised fund vs. recorded time).
* A project searcher (showing project title and ID).
* Expand available fundraising websites.
* Update `scraper.py` whenever the interface of the supported websites changes.