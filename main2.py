'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

#do NOT import ways. This should be done from other files
#simply import your modules and call the appropriate functions


from algorithms import a_star_with_information, a_star_exp3_with_information


def a_star(source, target):
    return a_star_with_information(source, target)[0]

    
def a_star_exp3(source, target, abstractMap):
    return a_star_exp3_with_information(source, target, abstractMap)[0]


def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'a_star':
        path = a_star(source, target)
    if argv[1] == 'a_star_exp3':
        import pickle as pkl
        abstractMap = pkl.load(open(argv[4],'rb'))
        path = a_star_exp3(source, target,abstractMap)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv
    dispatch(argv)
