import v1
import v2
import v3

URL_MAPPINGS = {
    '1': {
        '/1/dummy_post': v1.views.dummy_view,
        '/1/dummy_get': v1.views.dummy_view,
    },
    '2': {
        '/2/dummy_post': v2.views.dummy_view,
        '/2/dummy_get': v2.views.dummy_view,
    },
    '3': {
        '/3/dummy_post': v3.views.dummy_get_view,
        '/3/dummy_get': v3.views.dummy_post_view,
    },
}


def add_url_rule(app, allowed_versions):
    for version in allowed_versions:
        print version,
        for url, controler in URL_MAPPINGS[version].iteritems():
            print url, controler
            app.add_url_rule(
                url, url.replace('/', '_'), view_func=controler)
