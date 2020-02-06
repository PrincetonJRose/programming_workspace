class JavaScriptObject(dict):
	def __getattribute__(self, item):
		try:
			return self[item]
		except KeyError:
			return super()._getattribute__(item)
		else:
			pass