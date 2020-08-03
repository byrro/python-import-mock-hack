class Hack:

    def __call__(self):
        print('Calling Hack')
        return self

    def __getattr__(self, name):
        print(f"Getting attribute: '{name}'")
        return self

hack = Hack()
