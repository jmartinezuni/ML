from pattern.web import URL, DOM, plaintext


def data_from_reddit():
	url = URL('https://www.reddit.com/r/pygame/')
	dom = DOM(url.download(cached=True))
	for e in dom('div.entry')[:10]: # Top 10 reddit entries.
		for a in e('a.title')[:1]: # First <a class="title">.
			print '> '+ str(a.content)


def data_from_itebooks():
	url = URL('https://it-ebooks.info/tag/programming/')
	dom = DOM(url.download(cached=True))
	for e in dom('table.main')[:1]: 
		for t in e('td.top td')[:2]:
			print t

def data_from_coursera():
	pass