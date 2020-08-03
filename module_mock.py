import sys


class Insider:

    def __call__(self):
        print('CALLing insider')
        return self

    def __getattr__(self, name):
        print(f"Getting insider attribute: '{name}'")
        return self


class Module:

    def __getattr__(self, name):
        print(f"Getting from module: '{name}'")
        return Insider()


sys.modules[__name__] = Module()
