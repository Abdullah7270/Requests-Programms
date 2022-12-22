import requests
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://books.toscrape.com/')

book_cats = r.html.find('#default > div > div > div > aside > div.side_categories > ul > li > ul > li')

book_info = []
for book_cat in book_cats:
	book_cat_link =list(book_cat.absolute_links)[0]
	book_cat_name =book_cat.text
	category = {
		'Book Name': book_cat_name,
		'Link': book_cat_link
	}
	book_info.append(category)

	for category in book_info:
		print(category['Book Name'])
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		url = category['Link']
		r = session.get(url)
		books = r.html.find('#default > div.container-fluid.page > div > div > div > section > div:nth-child(2) > ol > li')

	for book in books:
		try:
			book_url = list(book.absolute_links)[0]
			r = session.get(book_url)
			book_name = r.html.find('#content_inner > article > div.row > div.col-sm-6.product_main > h1', first=True).text
			book_price = r.html.find('#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color', first=True).text
			book_stock = r.html.find('#content_inner > article > div.row > div.col-sm-6.product_main > p.instock.availability', first=True).text
			book_description = r.html.find('#content_inner > article > p', first=True).text
			print(book_name)
			print(book_price)
			print(book_stock)
			print(book_description)
			print('=============================================================================')
		except AttributeError:
			pass


















