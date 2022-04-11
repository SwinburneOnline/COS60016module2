def multiply(a, b):
  """Multiplies two numbers and returns the result."""
  return a * b

#....................................................


class Fruit:
  """
  A class used to represent a Fruit

  ...

  Attributes
  ----------
  origin_str : str
      a formatted string to print out where the fruit originates
  name : str
      the name of the fruit
    """


#....................................................


class fruit():
  """
  A class used to represent a Fruit

  ...

  Attributes
  ----------
  origin_str : str
      a formatted string to print out where the fruit originates
  name : str
      the name of the fruit
  """

  def __init__(self, origin_str, name):
    self.origin_str = origin_str
    self.name = name


  def print_attr(self):
    print(f"I am {self.name} and a I am from {self.origin_str}")

  def importance(self, imp_str):
    print(f"{self.name} Importance is {imp_str}")


fruit  # __main__.fruit is class object
apple = fruit('Originated from Central Asia', 'Apple')
apple.importance("slows the growth of cancer cells")


#....................................................

"""


""""""
Class: Fruit
...
Attributes
----------
origin_str : str
    a formatted string to print out where the fruit originates
name : str
    the name of the fruit


Function: importance: to explain about the fruit importance
...
Attributes
----------
imp_str : str
    a formatted string to print the importance of the fruit

"""


class fruit():
  """
  A class used to represent a Fruit
  ...

  Attributes
  ----------
  origin_str: str
      a formatted string to print out where the fruit originates
  name: str
      the name of the fruit
  """

  def __init__(self, origin_str, name):
    self.origin_str = origin_str
    self.name = name

  def importance(self, imp_str):
    print(f"{self.name} Importance is {imp_str}")

  """
"""


class fruit():
  """
  A class used to represent a Fruit

  ...

  Attributes
  ----------
  origin_str : str
      a formatted string to print out where the fruit originates
  name : str
      the name of the fruit
  """

  def __init__(self, origin_str, name):
    self.origin_str = origin_str
    self.name = name

  def print_attr(self):
    print(f"I am {self.name} and a I am from {self.origin_str}")

  def importance(self, imp_str):
    print(f"{self.name} Importance is {imp_str}")


fruit  # __main__.fruit is class object
apple = fruit('Originated from Central Asia', 'Apple')
apple.importance("slows the growth of cancer cells")

#....................................................



"""

       This script is used for importing the package which contains vege and fruit class


        Importing the vege class and fruit class from the package


        Created 2 objects, one for vege class and one for fruit class


        """

from package import vege, fruit

apple = fruit('Originated from Central Asia', 'Apple')

apple.importance("slows the growth of cancer cells")

okra = vege('Originated from Southern Asia', 'Okra')

okra.importance("rich in antioxidants that may reduce your risk of serious diseases")


#..............................................