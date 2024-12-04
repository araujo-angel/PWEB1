class Ocultacao:
    def __init__(self):
        self.val = 111

    def method(self):
        val = 444
        print('val = ',val)


class Subclasse(Ocultacao):
    def __init__(self):
        super().__init__()
        self.val = 222

    def method(self):
        super().method()
        val = 333
        print('val = ',val)

ob1 = Ocultacao()
ob2 = Subclasse()

ob1.method()
ob2.method()
print()
print(ob1.val)
print(ob2.val)
