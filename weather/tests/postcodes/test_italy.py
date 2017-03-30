from weather.wwo.italy import location_for_postcode


def test_location_for_postcode():
	assert location_for_postcode('00118') == 'Roma, Lazio'
	assert location_for_postcode('01100') == 'Viterbo, Lazio'
	assert location_for_postcode('02100') == 'Rieti, Lazio'

