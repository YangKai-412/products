products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格: ')
#	p = [name, price]  #此行如同以下三行
#	p = []
#	p.append(name)
#	p.append(price)
	products.append([name, price]) #此行如同第七行
print(products)

for p in products:
	print(p[0], '的價格是', p[1])
	