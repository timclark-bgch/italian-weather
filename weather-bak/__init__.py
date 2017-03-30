import time

import wwo

__providers = {
	'GB': wwo.weather
}


def weather(country, postcode, clock=time):
	timestamp = int(clock.time())
	observation = __cached(country, postcode, timestamp)

	if observation and observation[1]:
		return observation[0]

	provider = __providers.get(country, None)

	if provider:
		current_observation = provider(country, postcode)
		if current_observation:
			__record(country, postcode, timestamp, current_observation)
			return current_observation

	return observation[0]


__cache = {}


def __key(country, postcode):
	return '[{}][{}]'.format(country, postcode)


def __cached(country, postcode, timestamp):
	observation = __cache.get(__key(country, postcode), None)

	if observation:
		return observation[0], timestamp - observation[1] < 100

	return None


def __record(country, postcode, timestamp, observation):
	__cache[__key(country, postcode)] = (observation, timestamp)


def __response(icon=None, description=None, temperature=None):
	return {
		'icon': icon,
		'description': description,
		'temperature': temperature
	}


print weather('GB', 'SW1A')
print weather('GB', 'SW1A')
