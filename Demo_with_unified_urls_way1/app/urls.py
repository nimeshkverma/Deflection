from v1 import views as views1
from v2 import views as views2
from v3 import views as views3

URL_MAPPINGS = {

    'dummy_post': {
        '1': views1.dummy_view,
        '2': views2.dummy_view,
        '3': views3.dummy_post_view,
    },
    'dummy_get': {
        '1': views1.dummy_view,
        '2': views2.dummy_view,
        '3': views3.dummy_get_view,
    },
}
