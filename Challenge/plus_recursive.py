



def run_recursive(number):
        
    
    if number == 0:
        return 0
    if number == 1:
        return 1    
    else:               
        return number + run_recursive(number-1)


def run_maths(number):
    return (number*(number+1)) / 2




if __name__ == '__main__':
    number = int(input('Ingresa un número: '))    
    result = int(run_recursive(number))
    print('La suma de {} hasta {} es: {}'.format(0,number,result) )