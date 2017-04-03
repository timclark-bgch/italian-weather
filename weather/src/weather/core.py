def observation(temperature=None, description='', icon=None, night=False):
	return {
		'description': description,
		'icon': __icon(icon, night),
		'temperature': temperature
	}


def __icon(icon, night):
	if icon:
		if night:
			return 'night_{}'.format(icon)

		return 'day_{}'.format(icon)

	return None


def celcius_temperature(value):
	return {'unit': 'C', 'value': value}
