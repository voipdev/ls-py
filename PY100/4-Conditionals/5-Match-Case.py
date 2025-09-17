animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'bird':
        print('tweet tweet')
    case 'horse':
        print('neigh')
    case _:
        print('*cricket*')
