from url_utils import gen_from_urls

urls = ('http://instagram.com','http://oreilly.com','http://python.com')

for resp_len, status, url in gen_from_urls(urls):
	print(resp_len,'->',status,'->',url)