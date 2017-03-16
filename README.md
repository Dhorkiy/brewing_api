# microsomething

A microservice project invloving Docker and splitting up an API into seperate GET, POST, PUT and DELETE. 
This will be achieved by a NGINX reverse proxy delegating these requests to the appropriate counter part. 
DB solution will be something like MySQL.

See http://codehandbook.org/python-web-application-flask-mysql/ for using flask with MySQL
## Architecture

![Architecture flowchart](/Bryggeriklubb%20API.jpg)

## TODO:

- POST, PUT, GET, DELETE
- Loadbalancer infront of the API and the client (for added microservice!!1one1)
- Database (MySQL)
	+ Id (Primary Key, Auto Increment) - INT
	+ Name (NOT NULL, Name of the product.) - VARCHAR
	+ Description (Allows NULL, Pellet or Flower, etc. Description of the product in case there are major differences.) - VARCHAR
	+ Alpha acidity (Allows NULL, Specific acidity for the product if it requires one.) - FLOAT
	+ Amount (NOT NULL (but can be '0,00' etc), Amount in grams) - FLOAT
	+ Date field (Updates on PUT, auto add on POST.) - DATETIME
	+ Type (NOT NULL, Malt, Hops etc. Type of product.) - VARCHAR
- Client