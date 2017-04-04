def successful_request(provider):
	pass


def failed_request(provider, query, status, body):
	pass


def error(provider, query, exception):
	pass


class MetricRecorder(object):
	def __init__(self, provider):
		self.provider = provider

	def succeeded(self):
		successful_request(self.provider)

	def failed(self, query, status, body):
		failed_request(self.provider, query, status, body)

	def error(self, query, exception):
		error(self.provider, query, exception)
