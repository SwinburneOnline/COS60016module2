our_string = 'A long piece of text.'
our_iterator_object = iter(our_string)

while True:
    try:
        i = next(our_iterator_object)
        print(i, end=' ')
    except StopIteration:
        print()
        break


#............................................................................


class ExampleClass:
   def __init__(self, iter_range):
       self.range = iter_range

   def __iter__(self):
       # self.n = 0
       self.n = 5
       return self

   def __next__(self):
       n = self.n

       if n > self.range:
           raise StopIteration

       self.n += 3

       return n


for i in ExampleClass(30):
   print(i)

#........................................................................

