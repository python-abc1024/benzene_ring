"""
—————————————————————————————————————————————————————————
| @version    : v0.5.0                                  |
| @author     : yangjinhe                               |
| @time       : 2025/2/22 21:10                         |
| @describe   : tool                                    |
| @software   : Visual Studio Code                      |
| @filename   : iterables.py                            |
| @package    : benzene_ring                            |
—————————————————————————————————————————————————————————
"""
__all__=["range","enumerate","map","filter","reversed",]

class range(object):
  """
  Benzene_ring range iterator class.
  Used to generate an iterator with a specified range and fixed span.
  ---
  parameters:
  stop: The end of the range
  start: The start of the range
  step: Specify the number of intervals between each element
  ---
  Number of cyclic variables:1
  """
  def __init__(self,stop,start=0,step=1)->None:
    self.stop=stop
    self.start=start
    self.step=step
  def __iter__(self):
    return(self)
  def __next__(self):
    if(self.start>=self.stop):
      raise(StopIteration)
    value=self.start
    self.start=value+self.step
    return(value)

class enumerate(object):
  """
  Benzene_ring enumerate iterator class.
  Outputs the content and index of the elements of an iterable object based on traversing through that iterable object.
  ---
  parameters:
  iterable: The iterable object to be traversed
  start: The start of the range
  step: Specify the number of intervals between each element
  stop: The end of the range
  ---
  Number of cyclic variables:2
  """
  def __init__(self,iterable,stop,start=0,step=1)->None:
    self.iterable=iter(iterable)
    self.start=start
    self.stop=stop
    self.step=step
  def __iter__(self):
    return(self)
  def __next__(self):
    if(self.start>=self.stop):
      raise(StopIteration)
    value=(self.start,self.iterable[self.start])
    self.start+=self.step
    return(value)

class map(object):
  """
  Benzene_ring map iterator class.
  Specify a function to map the elements in an iterable object in turn.
  ---
  parameters:
  function: The function used to map the elements
  iterable: The iterable object to be mapped
  ---
  Number of cyclic variables:1
  """
  def __init__(self,function,iterable)->None:
    self.function=function
    self.iterable=iter(iterable)
  def __iter__(self):
    return(self)
  def __next__(self):
    return(self.function(next(self.iterable)))

class filter(object):
  """
  Benzene_ring filter iterator class.
  Used to filter values in one iterator.
  ---
  prameters:
  function: The function used to filter the elements
  iterable: The iterable object to be filtered
  ---
  Number of cyclic variables:1
  """
  def __init__(self,function,iterable)->None:
    self.function=function
    self.iterable=iter(iterable)
  def __iter__(self):
    return(self)
  def __next__(self):
    value=next(self.iterable)
    return((value)if(self.function(value))else(next(self)))
  
class reversed(object):
  """
  Benzene_ring reversed iterator class.
  Used to reverse the elements in an iterator.
  ---
  parameters:
  iterable: The iterable object to be reversed.
  ---
  Number of cyclic variables:1
  """
  def __init__(self,iterable)->None:
    self.iterable=list(iterable)
  def __iter__(self):
    return(self)
  def __next__(self):
    if(len(self.iterable)==0):
      raise(StopIteration)
    return(self.iterable.pop())
