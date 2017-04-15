d = {
	'name': 'takuya',
	'city': 'Sydney',
	'phone': '123456789',
	'email': 'test@test.com'
}

print('&'.join(['{}={}'.format(k, v) for k,v in d.items()]))
