usage: 

from root run:
	python crawl.py

within python console:
	import pickle
	d = pickle.load(open('save.p', 'rb'))

to print course info
	d['ACCT']['101']

usage without pickle
	import beauty
	beauty.end_result['FNCE']['209']
