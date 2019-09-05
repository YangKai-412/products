import os  # poerating system

products = []
if os.path.isfile('products.csv'): #檢察檔案在不在
	print('yeah! 找到檔案了')
	# 讀取檔案
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue  #繼續下一個迴圈
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)

else:
	print('找不到檔案.....')

# 讓使用者輸入
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

# 印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
