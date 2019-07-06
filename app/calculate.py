from __future__ import print_function


class Calculate:
    def add(self, x, y):
        """Takes two integers and adds them together 
        to produce the result."""
        
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x),
                                                             type(y)))


if __name__ == '__main__':  # pragma: no cover
    calc = Calculate()
    result = calc.add("Hello", "World")
    print(result)
