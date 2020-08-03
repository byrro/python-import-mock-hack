# Python Import Mock Hack

Sometimes using the magic method `__getattr__` in a `Class` is quite useful when we want to expose functionality without having to hard code it.

But how about a module?

Turns out that an acceptable _(is it?)_ solution is to replace the module in `sys` with a `Class`. Then normally have fun with the `__getattr__` magic.

Why not have this `Class` as an instance of Mock? That would be a lot of funny mockery! _(sorry, couldn't resist the cheap pun)_
