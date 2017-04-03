import pytest

import weather.wwo.client as client
import os


@pytest.mark.skipif(
	('wwo_key' not in os.environ) or ('wwo_feed_key' not in os.environ),
	reason='Requires environment variables with API keys:[wwo_key, wwo_feed_key]')
def test_real_api():
	response = client.perform_query(query='90210', key=os.environ['wwo_key'], feed_key=os.environ['wwo_feed_key'])
	assert response.get('description', None) is not None
	assert response.get('icon', None) is not None
	assert response.get('temperature', None) is not None


def test_timeout():
	pass


def test_bad_json():
	pass


def test_bad_network():
	pass
