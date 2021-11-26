import time
from dash.testing.wait import until
from dash.testing.application_runners import import_app


def wait_for_callbacks(dash_duo):
    # the extra one second sleep adds safe margin in the context
    # of wait_for_callbacks
    time.sleep(3)
    until(dash_duo._wait_for_callbacks, timeout=40, poll=0.3)


def test_app(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app, port="8000")
    dash_duo.driver.maximize_window()

    dash_duo.wait_for_page(url="{}/{}".format(dash_duo.server_url, "/"), timeout=15)
    wait_for_callbacks(dash_duo)

    dash_duo.take_snapshot("app")