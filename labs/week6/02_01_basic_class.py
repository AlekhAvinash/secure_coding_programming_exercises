# make the most simple class possible


class SimpleClass:
    pass


# create an instance of your SimpleClass and print it out
an_inst = SimpleClass()
print(an_inst)

# now add some functionality to your simple class


class LessSimpleClass:
    cls_atr = "This is a simple attribute!"
    # add one class attribute

    def cls_fn(self):
        print(f"Hello!!, {self.cls_atr}")
    # add a class method

# print out your class attribute both from an instance of the class and through the class directly
# run the method - both directly from the class and through an instance.

nt_inst = LessSimpleClass()
print(nt_inst.cls_atr)
print(nt_inst.cls_fn())