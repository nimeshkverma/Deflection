BASE_URL = "http://0.0.0.0:8080"

URL = {
    "version_one_get_one": {
        "params": ['p1', 'p2'],
        "API_method": ['GET'],
        "redirection_to": "/test_get1",
        "output_format": "JSON"
    },

    "version_one_post_one": {
        "params": ["p1", "p2"],
        "API_method": ['POST'],
        "redirection_to": "/test_post1",
        "output_format": "JSON",
    }
}
