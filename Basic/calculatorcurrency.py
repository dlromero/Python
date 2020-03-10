
def foreign_exchange_calculator(ammount):
    col_to_mex = 0.0058

    return (col_to_mex * ammount)/1


def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos colombianos a pesos mexicanos')
    print('')

    ammount = float(
        input('Ingresa la cantidad de pesos colombianos que quieres convertir: '))

    result = foreign_exchange_calculator(ammount)

    print('${} pesos colombianos son ${} pesos mexicanos'.format(ammount, result))
    print('')


if __name__ == '__main__':
    run()
