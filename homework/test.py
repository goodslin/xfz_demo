# class Foo:
#     pass


class F1:
    def show(self):
        print('F1.show')


class F2:
    def show(self):
        print('F2.show')


def Func(obj):
    print(obj.show())


s1_obj = F1()
Func(s1_obj)

s2_obj = F2()
Func(s2_obj)
