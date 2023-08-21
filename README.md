## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple fan application.
	
## Technologies
Project is created with:
* Flask: Flask==2.0.2
* HTML
* CSS
* JavaScript
	
## Setup
To run this project:
* Clone this repo
* open a terminal in the root directory of project
* Build the image
* docker build -t myfan .
* Run the image
* docker run -p 5000:5000 myfan
* Once everything has started up, you should be able to access the webapp via http://localhost:5000/ on your host machine.

