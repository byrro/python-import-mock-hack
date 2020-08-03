'''
    Conclusion: seems that using the 'Hack' version is better, since it doesn't
    trigger syntax/linter errors (happens in the 'Mock' version).

    The 'Hack' version can't emulate an entire module, but it should not be a
    problem.
'''

import module_hack
import module_mock


print('\nHACK:')
print(module_hack.hack)
print(module_hack.hack.attr)
print(module_hack.hack.method())

print('\nMOCK:')
print(module_mock.whatever)
print(module_mock.whatever.attr)
print(module_mock.whatever.method())
