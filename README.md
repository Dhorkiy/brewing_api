# microsomething

A microservice project invloving Docker and splitting up an API into seperate GET, POST, PUT and DELETE. 
This will be achieved by a NGINX reverse proxy delegating these requests to the appropriate counter part. 
DB solution will be something like MySQL.

See http://codehandbook.org/python-web-application-flask-mysql/ for using flask with MySQL

TODO:

- POST, PUT, GET, DELETE
- Loadbalancer infront of the API and the client (for added microservice!!1one1)
- Database (MySQL)
	+ Id (PK) - INT
	+ Name - TEXT
	+ Description - TEXT
	+ Amount - FLOAT
	+ Date field (updates on PUT, auto add on POST) - DATETIME
	+ 
- Client

