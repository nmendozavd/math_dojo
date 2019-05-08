
"""
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for k in i:
                    self.result += k
            else:
                self.result += i
        return self
"""
#Part I
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *arg):
        self.result += sum(arg)
        return self

    def subtract(self, *arg):
        self.result -= sum(arg)
        return self

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result

#Part II & III

class MathDojo2(object):
    def __init__(self):
        self.result = 0

    def add(self, *arg):
        for i in range(len(arg)):
            if isinstance(arg[i], list) or isinstance(arg[i], tuple):
                self.result += sum(arg[i])
            else:
                self.result += arg[i]
        return self

    def subtract(self, *arg):
        for i in range(len(arg)):
            if isinstance(arg[i], list) or isinstance(arg[i], tuple):
                self.result -= sum(arg[i])
            else:
                self.result -= arg[i]
        
        return self

md2 = MathDojo2()
print md2.add([1], 3, 4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result
