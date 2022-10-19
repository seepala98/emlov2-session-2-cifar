class TestClass: 
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __repr__(self):
        return repr(
            f"Test Class a={self.a}, b={self.b}"
        )


def test_func(*args, **kwargs):
    print("args",args)
    print("kwargs", kwargs)

    return "something"