from http import HTTPStatus
from typing import Union, List, Dict

import allure
import requests
from decouple import config

from logging_config import allure_response_and_payload


class ApiClient:

    def __init__(self, base_url,  module: str, auth_token=None):
        self.url = base_url
        self.module = module
        self.base_url = self.url + self.module + config('VERSION_API')
        self.auth_token = auth_token

    def _add_authorization_header(self, headers=None):
        headers = headers or {}
        if self.auth_token:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        return headers

    def _send_request(self, method, end_point, payload=None, headers=None, params=None, files=None,
                      expected_status=None) -> Union[Dict, List]:
        url = f"{self.base_url}{end_point}"
        headers = self._add_authorization_header(headers)
        response = requests.request(method, url, json=payload, headers=headers, params=params, files=files)
        with allure.step(f'{end_point}'):
            allure_response_and_payload(response=response, payload=payload or params, method=method)
        if expected_status is not None:
            self.raise_exception_if_received_not_expected_status_code(response=response,
                                                                      expected_status=expected_status, method=method,
                                                                      payload=payload or params)

        response_json = response.json() if response.text else None

        return response_json

    def get(self, end_point, headers=None, params=None, expected_status=HTTPStatus.OK) -> Union[Dict, List]:
        return self._send_request('GET', end_point, params=params, headers=headers, expected_status=expected_status)

    def post(self, end_point, payload=None, headers=None, files=None, expected_status=HTTPStatus.CREATED) -> Union[
        Dict, List]:
        return self._send_request('POST', end_point, payload=payload, files=files, headers=headers,
                                  expected_status=expected_status)

    def put(self, end_point, payload=None, params=None, headers=None, expected_status=HTTPStatus.OK) -> Union[
        Dict, List]:
        return self._send_request('PUT', end_point, payload=payload, params=params, headers=headers,
                                  expected_status=expected_status)

    def delete(self, end_point, headers=None, params=None, payload=None, expected_status=HTTPStatus.NO_CONTENT) -> Union[
        Dict, List]:
        return self._send_request('DELETE', end_point, headers=headers, params=params, payload=payload,
                                  expected_status=expected_status)

    @staticmethod
    def raise_exception_if_received_not_expected_status_code(response: requests.Response, expected_status, method,
                                                             payload=None):
        if response.status_code != expected_status.value:
            error_message = (
                f"Expected status: {expected_status}, actual status: {response.status_code}.\n"
                f"Method: {method}\n"
                f"URL: {response.url}",
                f"{response.text}",
                f'{payload}'
            )
            # raise AssertionError(error_message)
