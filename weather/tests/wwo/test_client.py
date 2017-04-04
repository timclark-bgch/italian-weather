import pytest
import requests
from mock import create_autospec

import weather.wwo.client as client
import os

from weather.metrics import MetricRecorder


@pytest.mark.skipif(
	('wwo_key' not in os.environ) or ('wwo_feed_key' not in os.environ),
	reason='Requires environment variables with API keys:[wwo_key, wwo_feed_key]')
def test_real_api():
	response = client.perform_query(query='90210', key=os.environ['wwo_key'], feed_key=os.environ['wwo_feed_key'])
	assert response.get('description', None) is not None
	assert response.get('icon', None) is not None
	assert response.get('temperature', None) is not None


def test_request_exception():
	mock_metrics = create_autospec(MetricRecorder)
	mock_response = create_autospec(requests.Response)
	mock_response.status_code = requests.codes.ok
	mock_response.json.side_effect = requests.exceptions.RequestException('Request failed')

	mock_http = create_autospec(requests.get, return_value=mock_response)

	result = client.perform_query(query='BAD_REQUEST', http=mock_http, metrics=mock_metrics, key=None, feed_key=None)

	assert result is None
	mock_metrics.error.assert_called_once()


def test_response_not_ok():
	mock_metrics = create_autospec(MetricRecorder)
	mock_response = create_autospec(requests.Response)
	mock_response.status_code = requests.codes.forbidden

	mock_http = create_autospec(requests.get, return_value=mock_response)

	result = client.perform_query(query='SERVER_PROBLEM', http=mock_http, metrics=mock_metrics, key=None, feed_key=None)

	assert result is None
	mock_metrics.failed.assert_called_once()


def test_bad_json():
	mock_metrics = create_autospec(MetricRecorder)
	mock_response = create_autospec(requests.Response)
	mock_response.status_code = requests.codes.ok
	mock_response.json.side_effect = ValueError('No JSON object could be decoded')

	mock_http = create_autospec(requests.get, return_value=mock_response)

	result = client.perform_query(query='BAD_JSON', http=mock_http, metrics=mock_metrics, key=None, feed_key=None)

	assert result is None
	mock_metrics.error.assert_called_once()


def test_incorrect_json():
	mock_metrics = create_autospec(MetricRecorder)
	mock_response = create_autospec(requests.Response)
	mock_response.status_code = requests.codes.ok
	mock_response.json.return_value = {'cabbages': [1, 2, 3], 'carrots': True}

	mock_http = create_autospec(requests.get, return_value=mock_response)

	result = client.perform_query(query='INCORRECT_JSON', http=mock_http, metrics=mock_metrics, key=None, feed_key=None)

	assert result is None
	mock_metrics.error.assert_called_once()


def test_correct_json():
	mock_metrics = create_autospec(MetricRecorder)
	mock_response = create_autospec(requests.Response)
	mock_response.status_code = requests.codes.ok
	mock_response.json.return_value = {
		'cabbages': [1, 2, 3], 'carrots': True,
		'data':
			{
				'current_condition': [
					{
						'temp_C': 10,
						'weatherDesc': [{'value': 'Grimy'}],
						'isdaytime': 'nope',
						'weatherIconUrl': [{'value': '/wsymbol_0037_cloudy_with_sleet_night.png'}]
					}
				]
			}
	}

	mock_http = create_autospec(requests.get, return_value=mock_response)

	result = client.perform_query(query='CORRECT_JSON', http=mock_http, metrics=mock_metrics, key=None, feed_key=None)

	assert result is not None
	assert result['temperature']['value'] == 10
	assert result['description'] == 'Grimy'
	assert result['icon'] == 'night_cloudy_with_sleet'
	mock_metrics.succeeded.assert_called_once()
