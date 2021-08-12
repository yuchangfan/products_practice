# products_practice.py

import os
products = []

# 檢查檔案在不在
if os.path.isfile('products.csv'):
	# 讀取檔案
	print('yeah! 找到檔案了！')
	with open('products.csv', 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
else:
	print('找不到檔案......')

# 使用者輸入新品項

while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')

	# 第一種寫法：
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)

	# 第二種寫法：
	# p = [name, price]
	# products.append(p)

	# 第三種寫法：
	products.append([name, price])

print(products)

# 印出購買紀錄（商品 + 價格）
for product in products:
	print(product[0], '的價格是：', product[1])

# 寫入檔案
with open('products.csv' , 'w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')