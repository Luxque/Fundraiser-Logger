# Fundraiser Logger

## Project Description

Are you tired of manually checking the status of the fundraiser programs you support?
This project aims to create a simple and interactive environment for checking the status of supporing fundraiser projects and logging the progress over time.
The application will offer both automatic and manual checking/logging.
The logged data will be stored as a CSV file, and the application will be able to plot the fundraiser progress to analyze the particiption rate over time.
**Please note, this project will never collect private and sensitive personal information; it will collect publicly available information only.**

## Stack

* Python
* Beautiful Soup

## Supported Fundraiser Websites

* [CAMPFIRE](https://camp-fire.jp/)

## To Be Implemented

* A savable settings.
* CSV file I/O.
* A plot generator (raised fund vs. recorded time).
* A project searcher (showing project title and ID).
* Expand available fundraising websites.
    * [Kickstarter](https://www.kickstarter.com/)
* Update `scraper.py` whenever the interface of the supported websites changes.
