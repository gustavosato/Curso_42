class Intern:
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
        
    def __init__(self, name=None):
        if name is None:
            self.Name = "My name? I’m nobody, an intern, I have no name."
        else:
            self.Name = name

    def __str__(self):
        return self.Name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return Intern.Coffee()

def test():
    nobody = Intern()
    mark = Intern("Mark")

    print(nobody)  # Output: My name? I’m nobody, an intern, I have no name.
    print(mark)  # Output: Mark

    coffee = mark.make_coffee()
    print(coffee)  # Output: This is the worst coffee you ever tasted.

    try:
        nobody.work()
    except Exception as e:
        print(e)  # Output: I’m just an intern, I can’t do that...

if __name__ == '__main__':
    test()