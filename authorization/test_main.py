from test_authorization import TestAuthorization


def test_authorization():
    run = TestAuthorization()
    run.open_browser()
    run.log_in_profile()
    # print("Hello")
    run.check_log_in_profile()
