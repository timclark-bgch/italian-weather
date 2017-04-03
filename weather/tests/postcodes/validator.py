import json
import time

import requests

from weather.wwo import location_for_postcode

postcodes = [
	'00118', '01100', '02100', '03100', '04100', '05100', '06121', '07100', '07026', '07029', '08100', '08045', '08048',
	'09121', '09170', '09013', '09016', '09025', '09039',
	'10121', '11100', '12100', '13100', '13900', '14100', '15100', '16121', '17100', '18100', '19121',
	'20121', '20900', '21100', '22100', '23100', '23900', '24121', '25121', '26100', '26900', '27100', '28100', '28921',
	'29100',
	'30121', '31100', '32100', '33100', '33170', '34121', '34170', '35121', '36100', '37121', '38121', '39100',
	'40121', '41121', '42121', '43100', '44100', '45100', '46100', '47121', '47521', '47921', '47890', '48121',
	'50121', '51100', '52100', '53100', '54100', '54023', '55100', '56121', '57121', '58100', '59100',
	'60121', '61100', '61029', '62100', '63100', '63900', '64100', '65121', '66100', '67100',
	'70121', '71100', '72100', '73100', '74100', '75100', '76121', '76123', '76125',
	'80121', '81100', '82100', '83100', '83100', '84121', '85100', '86100', '86170', '87100', '88100', '88900', '89121',
	'89900',
	'90121', '91100', '92100', '93100', '94100', '95121', '96100', '97100', '98121',
]


def __check(query):
	payload = {
		'key': '3c2e8cc762120943102403',
		'feedkey': '0a8402ca22122635102403',
		'num_of_days': "8",
		"tp": '3',
		'format': 'json',
		'extra': 'utcDateTime,isDayTime',
		'query': query
	}

	headers = {'Host': 'www.worldweatheronline.com'}

	r = requests.get('http://www.worldweatheronline.com/feed/premium-weather-V2.ashx/weather', params=payload,
									 headers=headers)

	data = json.loads(r.content)['data']
	temps = ','.join(c['temp_C'] for c in data['current_condition'])
	queries = ','.join(r['query'] for r in data['request'])
	print '{} - Temps: {} - Locs: {}'.format(r.status_code, temps, queries)


def validate():
	for code in postcodes:
		location = location_for_postcode(code)
		print '{} - {}'.format(code, location)
		__check(location)
		time.sleep(20)


validate()
