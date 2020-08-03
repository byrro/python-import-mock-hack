from module_hack import hack
from module_mock import whatever


print('\nHACK:')
print(hack)
print(hack.attr)
print(hack.method())

print('\nMOCK:')
print(whatever)
print(whatever.attr)
print(whatever.method())

'''
    Conclusion: seems that using the 'Hack' version is better, since it doesn't
    trigger syntax/linter errors (happens in the 'Mock' version).

    The 'Hack' version can't emulate an entire module, but it should not be a
    problem to 
'''
