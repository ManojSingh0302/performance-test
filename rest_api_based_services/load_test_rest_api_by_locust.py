# !interpreter [optional-arg]
# -*- coding: utf-8 -*-

"""
This contains sample code on load test scripts to load test REST API based services with locust.
"""

# Built-in/Generic Imports
import json
import logging
from locust import task, constant
from locust.contrib.fasthttp import FastHttpUser

__author__ = "Manoj Singh"


log = logging.getLogger("rest-api-performance-test")


def get_headers():
    """ It generated the api headers."""
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def get_api_payload():
    """ It generated the body of request."""
    payload = {
    }
    return payload


class LocustClient(FastHttpUser):
    host = "https://api.nationalize.io"
    wait_time = constant(0)

    def __init__(self, environment):
        """ Class constructor."""
        super().__init__(environment)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task
    def load_rest_api_based_service(self):
        """ This method contains all the APIs that needs to be load tested for a service."""
        headers = get_headers()

        try:

            # Build your query parameter for GET API requests
            api_query_params = f"?name={'manoj'}"
            api_payload = json.dumps(get_api_payload())

            with self.client.get(api_query_params, headers=headers, catch_response=True, data=api_payload,
                                 name="Predict the nationality") as resp_of_api:

                if resp_of_api.status_code == 200:
                    resp_body_of_api = resp_of_api.json()
                    assert resp_body_of_api.get("name") == "manoj"
                    resp_of_api.success()

                    # Avoid too much logging in load test script as it may slow it
                    log.info("API call resulted in success.")

                else:
                    resp_of_api.failure(resp_of_api.text)
                    # Avoid too much logging in load test script as it may slow it
                    log.error("API call resulted in failed.")

        except Exception as e:
            log.error(f"Exception occurred! details are {e}")
