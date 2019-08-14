# this is the only ifle in the project. If a bug is found I will edit this file.

print('Project file can be found here: https://github.com/5cans/Math1_Recursion')
print('The program finds the end value recursively, and prints the formula.')

# operation variable
print('')
print('e.g. f(x) = f(x-1) ***operation*** 1')
asdm = input('What operation would you like to use? [A/s/d/m]: ')
    
# number of terms
print('')
print("f(****x****) = f(x-1) + 1")
terms = int(input('How many terms would you like? [enter a number]: '))

# numb in operation
print('')
print('f(x) = f(x-1) + ****number****')
numb = int(input('How much would you like to add/subtract/multiply/divide each term? [enter a number]: ')) 

# starting number
print('')
print('f(0) = ****number****')
sn = int(input('What is your first [starting] number?: '))

if asdm == 'a' or asdm == 'A':
    print('Your formula:')
    print('f(0) = ' + str(sn))
    print('f(' + str(terms) + ') = f(' + str(terms - 1) + ') ' + '+' + ' ' + str(numb))
    while terms > 0:
        terms = terms - 1
        sn = sn + numb
    print(sn)
if asdm == 's' or asdm == 'S':
    print('Your formula:')
    print('f(0) = ' + str(sn))
    print('f(' + str(terms) + ') = f(' + str(terms - 1) + ') ' + '-' + ' ' + str(numb))
    while terms > 0:
        terms = terms - 1
        sn = sn - numb
    print(sn)
if asdm == 'd' or asdm == 'D':
    print('Your formula:')
    print('f(0) = ' + str(sn))
    print('f(' + str(terms) + ') = f(' + str(terms - 1) + ') ' + '/' + ' ' + str(numb))
    while terms > 0:
        terms = terms - 1
        sn = sn / numb
    print(sn)
if asdm == 'm' or asdm == 'M':
    print('Your formula:')
    print('f(0) = ' + str(sn))
    print('f(' + str(terms) + ') = f(' + str(terms - 1) + ') ' + '*' + ' ' + str(numb))
    while terms > 0:
        terms = terms - 1
        sn = sn * numb
    print(sn)
