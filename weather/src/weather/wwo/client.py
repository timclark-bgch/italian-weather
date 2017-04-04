import re

import requests

import weather.types as types
from weather.core import observation, celcius_temperature
from weather.metrics import MetricRecorder

__headers = {'Host': 'www.worldweatheronline.com'}
__url = 'http://www.worldweatheronline.com/feed/premium-weather-V2.ashx/weather'


def perform_query(query, key, feed_key, http=requests.get, metrics=MetricRecorder('wwo')):
	payload = {
		'key': key,
		'feedkey': feed_key,
		'num_of_days': '8',
		'tp': '3',
		'format': 'json',
		'extra': 'utcDateTime,isDayTime',
		'cc': 'yes',
		'fx': 'no',
		'mca': 'no',
		'fx24': 'no',
		'query': query
	}

	try:
		r = http(__url, params=payload, headers=__headers, timeout=1)

		if r.status_code == requests.codes.ok:
			weather = __current_weather(r.json()['data']['current_condition'])
			metrics.succeeded()
			return weather
		else:
			metrics.failed(query, r.status_code, r.content)
	except requests.exceptions.RequestException as e:
		metrics.error(query, e)
	except Exception as e:
		metrics.error(query, e)

	return None


__icons = {
	'sunny': types.sunny,
	'light_snow_showers': types.light_snow_showers,
	'sleet_showers': types.sleet_showers,
	'sunny_intervals': types.sunny_intervals,
	'cloudy_sunny_intervals': types.sunny_intervals,
	'light_rain_showers': types.light_rain_showers,
	'light_snow': types.light_snow_showers,
	'cloudy_with_sleet': types.cloudy_with_sleet,
	'white_cloud': types.white_cloud,
	'cloudy': types.white_cloud,
	'black_low_cloud': types.white_cloud,
	'cloudy_with_light_rain': types.cloud_light_rain,
	'heavy_snow_showers': types.heavy_snow_showers,
	'heavy_rain_showers': types.heavy_rain_showers,
	'thundery_showers': types.thundery_showers,
	'thunderstorms': types.thunderstorms,
	'cloudy_with_heavy_snow': types.cloudy_heavy_snow,
	'cloudy_with_light_snow': types.cloudy_light_snow,
	'cloudy_with_heavy_rain': types.cloudy_heavy_rain,
	'fog': types.fog,
	'clear_sky': types.clear_sky,
}


def __icon(url):
	result = re.search(r'/wsymbol_[0-9]+_(.*).png$', url)
	if result:
		return __icons.get(result.group(1).replace('_night', ''), None)

	return None


def __current_weather(data):
	conditions = [(c['temp_C'], c['weatherDesc'], c['isdaytime'], c['weatherIconUrl']) for c in data]
	if conditions:
		temperature = conditions[0][0]
		description = conditions[0][1][0]['value']
		night_time = 'yes' != conditions[0][2]
		icon = conditions[0][3][0]['value']

		return observation(
			temperature=celcius_temperature(temperature),
			description=description,
			icon=__icon(icon),
			night=night_time)

	return None
