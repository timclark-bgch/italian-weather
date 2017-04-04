import time

import wwo.query as wwo

__providers = {
	'GB': wwo.weather
}


def weather(country, postcode, clock=time):
	timestamp = int(clock.time())
	cached_observation = __cached(country, postcode, timestamp)

	if cached_observation and cached_observation[1]:
		return cached_observation[0]

	provider = __providers.get(country, None)

	if provider:
		current_observation = provider(country, postcode)
		if current_observation:
			__record(country, postcode, timestamp, current_observation)
			return current_observation

	return cached_observation[0]


__cache = {}


def __key(country, postcode):
	return '[{}][{}]'.format(country, postcode)


def __cached(country, postcode, timestamp):
	stored_observation = __cache.get(__key(country, postcode), None)

	if stored_observation:
		return stored_observation[0], timestamp - stored_observation[1] < 100

	return None


def __record(country, postcode, timestamp, current_observation):
	__cache[__key(country, postcode)] = (current_observation, timestamp)


def __response(icon=None, description=None, temperature=None):
	return {
		'icon': icon,
		'description': description,
		'temperature': temperature
	}
