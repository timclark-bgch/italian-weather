from weather.wwo.italy import location_for_postcode


def test_location_for_postcode():
	assert location_for_postcode('00118') == 'Roma, Lazio'
	assert location_for_postcode('01100') == 'Viterbo, Lazio'
	assert location_for_postcode('02100') == 'Rieti, Lazio'
	assert location_for_postcode('03100') == 'Frosinone, Lazio'
	assert location_for_postcode('04100') == 'Latina, Lazio'
	assert location_for_postcode('05100') == 'Terni, Umbria'
	assert location_for_postcode('06121') == 'Perugia, Umbria'

