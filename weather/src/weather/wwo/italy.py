__region_ab = 'Abruzzo'
__region_bc = 'Basilicata'
__region_ci = 'Calabria'
__region_cm = 'Campania'
__region_er = 'Emilia-Romagna'
__region_fb = 'Friuli-Venezia Giulia'
__region_lz = 'Lazio'
__region_lg = 'Liguria'
__region_lm = 'Lombardia'
__region_mh = 'Marche'
__region_ml = 'Molise'
__region_pm = 'Piemonte'
__region_pu = 'Puglia'
__region_sd = 'Sardegna'
__region_sc = 'Sicilia'
__region_tc = 'Toscana'
__region_tt = 'Trentino-Alto Adige'
__region_um = 'Umbria'
__region_vd = 'Valle d\'Aosta'
__region_vn = 'Veneto'

__simple_cap = {
	'00': ('Rome', __region_lz),
	'01': ('Viterbo', __region_lz),
	'02': ('Rieti', __region_lz),
	'03': ('Frosinone', __region_lz),
	'04': ('Latina', __region_lz),
	'05': ('Terni', __region_um),
	'06': ('Perugia', __region_um),
	'10': ('Turin', __region_pm),
	'11': ('Aosta', __region_vd),
	'12': ('Cuneo', __region_pm),
	'14': ('Asti', __region_pm),
	'15': ('Alessandria', __region_pm),
	'16': ('Genova', __region_lg),
	'17': ('Savona', __region_lg),
	'18': ('Imperia', __region_lg),
	'19': ('La Spezia', __region_lg),
	'21': ('Varese', __region_lm),
	'22': ('Como', __region_lm),
	'24': ('Bergamo', __region_lm),
	'25': ('Brescia', __region_lm),
	'27': ('Pavia', __region_lm),
	'29': ('Piacenza', __region_er),
	'30': ('Venezia', __region_vn),
	'31': ('Treviso', __region_vn),
	'32': ('Belluno', __region_vn),
	'35': ('Padova', __region_vn),
	'36': ('Vicenza', __region_vn),
	'37': ('Verona', __region_vn),
	'38': ('Trento', __region_tt),
	'39': ('Bolzano', __region_tt),
	'40': ('Bologna', __region_er),
	'41': ('Modena', __region_er),
	'42': ('Reggio nell\'Emilia', __region_er),
	'43': ('Parma', __region_er),
	'44': ('Ferrara', __region_er),
	'45': ('Rovigo', __region_vn),
	'46': ('Mantova', __region_vn),
	'48': ('Ravenna', __region_er),
	'50': ('Firenze', __region_tc),
	'51': ('Pistoia', __region_tc),
	'52': ('Arezzo', __region_tc),
	'53': ('Siena', __region_tc),
	'55': ('Lucca', __region_tc),
	'56': ('Pisa', __region_tc),
	'57': ('Livorno', __region_tc),
	'58': ('Grosseto', __region_tc),
	'59': ('Prato', __region_tc),
	'60': ('Ancona', __region_mh),
	'62': ('Macerata', __region_mh),
	'64': ('Teramo', __region_ab),
	'65': ('Pescara', __region_ab),
	'66': ('Chieti', __region_ab),
	'67': ('L\'Aquila', __region_ab),
	'70': ('Bari', __region_pu),
	'71': ('Foggia', __region_pu),
	'72': ('Brindisi', __region_pu),
	'73': ('Lecce', __region_pu),
	'74': ('Taranto', __region_pu),
	'75': ('Matera', __region_bc),
	'80': ('Naples', __region_cm),
	'81': ('Caserta', __region_cm),
	'82': ('Benevento', __region_cm),
	'83': ('Avellino', __region_cm),
	'84': ('Salerno', __region_cm),
	'85': ('Potenza', __region_bc),
	'87': ('Cosenza', __region_ci),
	'90': ('Palermo', __region_sc),
	'91': ('Trapani', __region_sc),
	'92': ('Agrigento', __region_sc),
	'93': ('Caltanisetta', __region_sc),
	'94': ('Enna', __region_sc),
	'95': ('Catania', __region_sc),
	'96': ('Siracusa', __region_sc),
	'97': ('Ragusa', __region_sc),
	'98': ('Messina', __region_sc),
}


def __cap_07(code):
	if code.startswith('07'):
		if code.startswith('071') or code.startswith('0701') or code.startswith('0703') or code.startswith('0704'):
			return 'Sassari', __region_sd

		if code.startswith('070'):
			if code.startswith('07026'):
				return 'Olbia', __region_sd
			return 'Tempio Pausania', __region_sd

	return None


def __cap_08(code):
	if code.startswith('08'):
		if code.startswith('08020'):
			return 'Tempio Pausania', __region_sd

		if code.startswith('081') or code.startswith('0801') or code.startswith('0802') or code.startswith('0803'):
			return 'Nuoro', __region_sd

		if code.startswith('0804'):
			if code.startswith('08045'):
				return 'Lanusei', __region_sd
			return 'Tortoli', __region_sd

	return None


def __cap_09(code):
	if code.startswith('09'):
		if code.startswith('09013'):
			return 'Carbonia', __region_sd

		if code.startswith('09016'):
			return 'Iglesias', __region_sd

		if code.startswith('09025'):
			return 'Sanluri', __region_sd

		if code.startswith('09039'):
			return 'Villacidro', __region_sd

		if code.startswith('09170'):
			return 'Oristano', __region_sd

		if code.startswith('091') or code.startswith('0901') or code.startswith('0902') or code.startswith(
			'0903') or code.startswith('0904'):
			return 'Cagliari', __region_sd

	return None


def __cap_13(code):
	if code.startswith('13'):
		if code.startswith('131') or code.startswith('130'):
			return 'Vercelli', __region_pm

		if code.startswith('139') or code.startswith('138'):
			return 'Biella', __region_pm

	return None


def __cap_20(code):
	if code.startswith('20'):
		if code.startswith('201') or code.startswith('200'):
			return 'Milan', __region_lm

		if code.startswith('209') or code.startswith('208'):
			return 'Monza', __region_lm

	return None


def __cap_23(code):
	if code.startswith('23'):
		if code.startswith('231') or code.startswith('230'):
			return 'Sondrio', __region_lm

		if code.startswith('239') or code.startswith('238'):
			return 'Lecco', __region_lm

	return None


def __cap_26(code):
	if code.startswith('26'):
		if code.startswith('261') or code.startswith('260'):
			return 'Cremona', 'Italy' # WWO has problems with Cremona

		if code.startswith('269') or code.startswith('268'):
			return 'Lodi', __region_lm

	return None


def __cap_28(code):
	if code.startswith('28'):
		if code.startswith('281') or code.startswith('280'):
			return 'Novara', __region_pm

		if code.startswith('289') or code.startswith('288'):
			return 'Cusio', __region_pm

	return None


def __cap_33(code):
	if code.startswith('33'):
		if code.startswith('33100') or code.startswith('3301') or code.startswith('3302') or code.startswith(
			'3303') or code.startswith('3304') or code.startswith('3305'):
			return 'Udine', __region_fb

		if code.startswith('33170') or code.startswith('3307') or code.startswith('3308') or code.startswith('3309'):
			return 'Pordenone', __region_fb

	return None


def __cap_34(code):
	if code.startswith('34'):
		if code.startswith('3412') or code.startswith('3413') or code.startswith('3414') or code.startswith(
			'3415') or code.startswith('3401'):
			return 'Trieste', __region_fb
		if code.startswith('34170') or code.startswith('3407'):
			return 'Gorizia', __region_fb

	return None


def __cap_47(code):
	if code.startswith('47'):
		if code.startswith('47890'):
			return 'San Marino', 'San Marino'

		if code.startswith('471') or code.startswith('470'):
			return 'Forli', __region_er

		if code.startswith('4792') or code.startswith('478'):
			return 'Rimini', __region_er

		if code.startswith('475'):
			return 'Cesena', __region_er

	return None


def __cap_54(code):
	if code.startswith('54'):
		if code.startswith('54023'):
			return 'Carrara', __region_tc

		return 'Massa', __region_tc

	return None


def __cap_61(code):
	if code.startswith('61'):
		if code.startswith('61029'):
			return 'Urbino', 'Italy' # WWO has a problem with Urbino

		return 'Pesaro', __region_mh

	return None


def __cap_63(code):
	if code.startswith('63'):
		if code.startswith('631') or code.startswith('630'):
			return 'Ascoli Piceno', __region_mh
		if code.startswith('639') or code.startswith('638'):
			return 'Fermo', __region_mh

	return None


def __cap_76(code):
	if code.startswith('76'):
		if code.startswith('76121') or code.startswith('760'):
			return 'Barletta', __region_pu

		if code.startswith('76123'):
			return 'Andria', __region_pu

		if code.startswith('76125'):
			return 'Trani', __region_pu

	return None


def __cap_86(code):
	if code.startswith('86'):
		if code.startswith('86100') or code.startswith('8601') or code.startswith('8602') or code.startswith(
			'8603') or code.startswith('8604'):
			return 'Campobasso', __region_ml

		if code.startswith('86170') or code.startswith('8607') or code.startswith('8608') or code.startswith('8609'):
			return 'Isernia', __region_ml

	return None


def __cap_88(code):
	if code.startswith('88'):
		if code.startswith('881') or code.startswith('880'):
			return 'Catanzaro', __region_ci

		if code.startswith('889') or code.startswith('888'):
			return 'Crotone', __region_ci

	return None


def __cap_89(code):
	if code.startswith('89'):
		if code.startswith('891') or code.startswith('890'):
			return 'Reggio Calabria', __region_ci

		if code.startswith('899') or code.startswith('898'):
			return 'Vibo Valentia', __region_ci

	return None


def __format(location):
	return '{}, {}'.format(location[0], location[1])


def location_for_postcode(code):
	location = __simple_cap.get(code[0:2], None)
	if location is not None:
		return __format(location)

	exceptions = [
		__cap_07,
		__cap_08,
		__cap_09,
		__cap_13,
		__cap_20,
		__cap_23,
		__cap_26,
		__cap_28,
		__cap_33,
		__cap_34,
		__cap_47,
		__cap_54,
		__cap_61,
		__cap_63,
		__cap_76,
		__cap_86,
		__cap_88,
		__cap_89
	]

	for cap in exceptions:
		loc = cap(code)
		if loc is not None:
			return __format(loc)

	return None
