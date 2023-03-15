
products = {'pechenja':['Oreo', 'Domina', 'Tuc-Tuc'],
            'Moloko':['Limbazi', 'Dubultu'],
            'Sosiski':['Forevers','Lido', 'Rkaveras'],
            'Mineralka':['Mangali', 'Rigas']}

def teg_print(tags):
    for i in tags:
        with open('text.txt', 'a') as file:
            file.write(i + '\n')
    print('product najden')

while products:
    ask = input('Vvedite nazvanie produkta')
    if ask in products:
        teg_print(products[ask])
        products.pop(ask)
print('Produkkti zakonchilisj')