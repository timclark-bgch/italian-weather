from mock import create_autospec
import weather.wwo.query as wwo
from weather.wwo.client import perform_query

__config = {
	'key': 'TEST_KEY',
	'feed_key': 'TEST_FEED_KEY'
}


def test_italian_query():
	mock_query = create_autospec(perform_query)
	mock_query.return_value = {'dummy': 'response'}

	result = wwo.weather('IT', '00118', __config, mock_query)
	assert result is not None
	mock_query.assert_called_once_with('Rome, Lazio', key=__config['key'], feed_key=__config['feed_key'])


def test_gb_query():
	mock_query = create_autospec(perform_query)
	mock_query.return_value = {'dummy': 'response'}

	result = wwo.weather('GB', 'SW1A 1AA', __config, mock_query)
	assert result is not None
	mock_query.assert_called_once_with('SW1A 1AA', key=__config['key'], feed_key=__config['feed_key'])

