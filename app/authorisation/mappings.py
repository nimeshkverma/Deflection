BASE_URL = "http://127.0.0.1:8080"


DESTINATION = {
		"/signin/" : {
						1: BASE_URL + "/test_get1",
						2: BASE_URL + "/test_get2",

		},
		"/signup/"	: {
						1:BASE_URL + "/test_post1",
						2:BASE_URL + "/test_post2",
		}	
}