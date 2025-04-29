PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_list = PRICE_LIST.split()

new_price_list = dict(
    zip(price_list[::2], [int(x.rstrip('р')) for x in price_list[1::2]])
)
print(new_price_list)

new_price_list_2 = {
    line.split()[0]: int(line.split()[1].rstrip('р')) for line in PRICE_LIST.splitlines()
}
print(new_price_list_2)
