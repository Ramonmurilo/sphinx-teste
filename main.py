"""
Este é um programa teste, ao qual não sou o autor. Essa documentação tem apenas fins educativos de obtenção de conhecimentosobre como trabalhar com sphinx.

"""
from module import pets

def roda_padrao():

    """
    Roda uma série de comandos teste
    """
    # the first class
    p1 = pets.Pets('jabba', 'Dan Sheffner')
    print(type(p1))
    p1.show_pets()
    print ()
    p1.get_average_age('cat')

    print ()

    # the second class
    p2 = pets.Pets.random_pets('Chris Sheffner')
    print(type(p2))
    p2.show_pets()
    print ()

   # owner gets another pet later on and names it roo
    print ('owner buys another pet later on...')
    p2.add_pet('Roo')
    p2.show_pets()
    print ()

    p2.get_average_age('dog')
    p2.get_average_age('fish')

roda_padrao()
