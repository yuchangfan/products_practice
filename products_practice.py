# products_practice.py

import os

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 使用者輸入新品項
def user_input(products):
	while True:
		name = input('請輸入商品名稱： ')
		if name == 'q':
			break
		price = input('請輸入商品價格： ')
		products.append([name, price])
	print(products)
	return products

# 印出購買紀錄（商品 + 價格）
def print_products(products):
	for product in products:
		print(product[0], '的價格是：', product[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename , 'w') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	# 檢查檔案在不在
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yeah! 找到檔案了！')
		products = read_file(filename)
	else:
		print('找不到檔案......')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()