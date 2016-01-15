# Deflection
A micro service framework to provide URL redirections with API version control.
Built in Flask.

Following is the directory structure.

`├── README.md`

`├── app`

`│   ├── __init__.py`

`│   ├── __init__.pyc`

`│   ├── common_utils.py`

`│   ├── v1`

`│   │   ├── __init__.py`

`│   │   ├── mapping.py`

`│   │   ├── utils.py`

`│   │   ├── views.py`

`│   ├── v2`

`│   │   ├── __init__.py`

`│   │   ├── mapping.py`

`│   │   ├── utils.py`

`│   │   ├── views.py`

`│   └── v3`

`│       ├── __init__.py`

`│       ├── mapping.py`

`│       ├── utils.py`

`│       ├── views.py`

`├── config.py`

`├── driver.py`

`└── test_server`

`    └── driver.py`


Following URLs are available for testing:-
- http://127.0.0.1:8000/1/dummy_get
- http://127.0.0.1:8000/2/dummy_get
- http://127.0.0.1:8000/3/dummy_get

- http://127.0.0.1:8000/1/dummy_post
- http://127.0.0.1:8000/2/dummy_post
- http://127.0.0.1:8000/3/dummy_post



