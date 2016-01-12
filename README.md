# Deflection
A micro service framework to provide URL redirections with API version control.
Built in Flask.

Following is the directory structure.

`
├── README.md
├── app
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── common_utils.py
│   ├── common_utils.pyc
│   ├── v1
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── mapping.py
│   │   ├── mapping.pyc
│   │   ├── utils.py
│   │   ├── utils.pyc
│   │   ├── views.py
│   │   └── views.pyc
│   ├── v2
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── mapping.py
│   │   ├── mapping.pyc
│   │   ├── utils.py
│   │   ├── utils.pyc
│   │   ├── views.py
│   │   └── views.pyc
│   └── v3
│       ├── __init__.py
│       ├── __init__.pyc
│       ├── mapping.py
│       ├── utils.py
│       ├── views.py
│       └── views.pyc
├── config.py
├── config.pyc
├── driver.py
└── test_server
    └── driver.py
`

