# Deflection
##### URL Redirection Framework with API Versioning Service

![Flask](http://flask.pocoo.org/docs/0.10/_static/flask.png)
![API Versioning ](http://justonesandzeros.typepad.com/images/2013/PlmApiVersioning/timeline.png)

###### Aim: 
This Document aims to provide why and how of the project pursued, reasons behind the choices made for the language/framework/tools incorporated.

###### Problem statement: 
With the advent of the new features and technology support demanded by the product which they serve, APIs evolve over time. Many times the same API which serve the new features must also faithfully serve the old ones too. Hence API Versioning comes into pictures. If website's architecture handles the API Versioning logic in the Controllers, code becomes messy, convoluted and difficult to maintain.
A Micro Framework which handles the logic of the Versioning of the API and accordingly redirecting them to the old/new API will help exponentially to overcome the drawbacks mentioned above.

##### Tools used:

Language: Python
Why: Python competes head to head with Scala in the handling load and providing fast responses for our use cases. It’s little behind Exilir. The major motivation factors for choosing Python were:
	- Availability of resources at our disposal
	- Fast development
	- Python’s disadvantages can be overcome via other means like horizontal scaling
	
Framework: Flask
Why: Out of the two major player, Django and Flask, Flask was chosen because:
  - It’s a micro framework with almost no batteries shipped along with it. Also the  user community support provides pluggable batteries for all the purposes and need (ORM etc). Hence Its light weight and flexible specially in our case as we only require a middleware over WSGI for Routing
  - Very less and intuitive code
  - Flexibility to expand the Micro service keeping our need in mind

This Repository provide four different architectures for building a micro service framework to provide URL redirections with API version control feature.

Out of the Four Architecture provide two are with unified `urls.py` and other two with urls assigned in the `views.py`.
The tree structure of the Repo is:-

![Repo Tree](https://github.com/nimeshkverma/Deflection/blob/master/images/Repo_tree.jpg)

`testing` folder provides a test servers which hosts API to which the our Framework will redirect.

Following URLs are available for testing:-

- http://127.0.0.1:8000/1/dummy_get?p1=10&p2=11
- http://127.0.0.1:8000/2/dummy_get?p1=10&p2=11
- http://127.0.0.1:8000/3/dummy_get?p1=10&p2=11

Provide atleast one param and value in the payload for post request
- http://127.0.0.1:8000/1/dummy_post
- http://127.0.0.1:8000/2/dummy_post
- http://127.0.0.1:8000/3/dummy_post
