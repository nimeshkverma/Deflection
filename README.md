# Deflection
##### URL Redirection Framework with API Versioning
![Flask](http://flask.pocoo.org/docs/0.10/_static/flask.png) 
![API Versioning ](http://justonesandzeros.typepad.com/images/2013/PlmApiVersioning/timeline.png)

This project provide four different architectures for building a micro service framework to provide URL redirections with API version control feature.

Out of the Four Architecture provide two are with unified `urls.py` and other two with urls assigned in the `views.py`.
The tree structure of the Repo is:-

![Repo Tree](https://github.com/nimeshkverma/Deflection/tree/master/images/repo_tree.jpg)

`testing` folder provides a test servers which hosts API to which the our Framework will redirect.

Following URLs are available for testing:-

- http://127.0.0.1:8000/1/dummy_get?p1=10&p2=11
- http://127.0.0.1:8000/2/dummy_get?p1=10&p2=11
- http://127.0.0.1:8000/3/dummy_get?p1=10&p2=11

Provide atleast one param and value in the payload for post request
- http://127.0.0.1:8000/1/dummy_post
- http://127.0.0.1:8000/2/dummy_post
- http://127.0.0.1:8000/3/dummy_post






