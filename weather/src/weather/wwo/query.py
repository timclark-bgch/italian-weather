import italy
from client import perform_query
from weather import countries


def weather(country, postcode, config):
	return perform_query(__query(country, postcode), key=config['key'], feed_key=config['feed_key'])


def __query(country, postcode):
	if countries.it == country:
		return italy.location_for_postcode(postcode)

	return postcode
