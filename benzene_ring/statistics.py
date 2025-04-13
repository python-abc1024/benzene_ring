"""
—————————————————————————————————————————————————————————
| @version    : v0.1.0                                  |
| @author     : yangjinhe                               |
| @time       : 2025/4/13 15:40                         |
| @describe   : statistics                              |
| @software   : Visual Studio Code                      |
| @filename   : statistics.py                           |
| @package    : benzene_ring                            |
—————————————————————————————————————————————————————————
This is a statistics module.
It provides a DataSet class to perform various statistical operations on a set of numbers.
"""
import matplotlib.pyplot as plt

class DataSet(object):
  """
  A better data set to store data and perform statistical operations.
  IMPORTANT!: The data set must be a number, not a string or other type.
  --- parameters:
    data_set: A tuple of numbers.
  --- example:
    >>> data_set=DataSet(1,2,3,4,5)
    >>> print(data_set)
    >>> data_set=DataSet(data_set=(1,2,3,4,5))
    >>> print(data_set.population_variance())
    >>> 2.0
    >>> print(data_set.sample_variance())
    >>> 2.5
    ...
  --- methods:
    __init__: Initialize the data set.
    __str__: Return a string representation of the data set(for user).
    __repr__: Return a string representation of the data set(for developer).
    __len__: Return the length of the data set.
    __add__: Add two data sets together.
    sum_: Return the sum of the data set.
    product: Return the product of the data set.
    deduplication: Remove duplicate elements from the data set.
    element_count: Count the number of each element in the data set.
    arithmetic_mean: Return the arithmetic mean of the data set.
    geometric_mean: Return the geometric mean of the data set.
    harmonic_mean: Return the harmonic mean of the data set.
    quadratic_mean: Return the quadratic mean of the data set.
    population_variance: Return the population variance of the data set.
    sample_variance: Return the sample variance of the data set.
    population_standard_deviation: Return the population standard deviation of the data set.
    sample_standard_deviation: Return the sample standard deviation of the data set.
    extreme_deviation: Return the extreme deviation of the data set.
    mean_deviation: Return the mean deviation of the data set.
    median: Return the median of the data set.
    mode: Return the mode of the data set.
    pie_chart: Draw a pie chart of the data set.
  """
  def __init__(self,*args)->None:
    self.data_set=args
    if(not(all([isinstance(i,(int,float))for(i)in(self.data_set)]))):
      raise TypeError("data_set must be a number")
  def __str__(self)->str:
    return(f"DataSet(data_set={self.data_set})")
  def __repr__(self)->str:
    return(f"DataSet{self.data_set}")
  def __len__(self)->int:
    return(len(self.data_set))
  def __add__(self,other)->float:
    return(DataSet(*(self.data_set+other.data_set)))
  def sum_(self)->float:
    return(sum(self.data_set))
  def product(self)->float:
    i=1
    for(j)in(self.data_set):
      i*=j
    return(i)
  def deduplication(self)->list:
    return(DataSet(*set(self.data_set)))
  def element_count(self)->int:
    return(DataSet(*[self.data_set.count(i)for(i)in(self.deduplication().data_set)]))
  def arithmetic_mean(self)->float:
    return(sum(self.data_set)/len(self.data_set))
  def geometric_mean(self)->float:
    return(self.product()**(1/len(self.data_set)))
  def harmonic_mean(self)->float:
    return(len(self.data_set)/sum([(1/i)for(i)in(self.data_set)]))
  def quadratic_mean(self)->float:
    return(((sum([(i**2)for(i)in(self.data_set)])/(len(self.data_set))))**(1/2))
  def population_variance(self)->float:
    return(sum([((i-self.arithmetic_mean())**2)for(i)in(self.data_set)]))/len(self.data_set)
  def sample_variance(self)->float:
    return(sum([((i-self.arithmetic_mean())**2)for(i)in(self.data_set)]))/(len(self.data_set)-1)
  def population_standard_deviation(self)->float:
    return(self.population_variance()**(1/2))
  def sample_standard_deviation(self)->float:
    return(self.sample_variance()**(1/2))
  def extreme_deviation(self)->float:
    return(max(self.data_set)-min(self.data_set))
  def mean_deviation(self)->float:
    return(sum([abs(self.arithmetic_mean()-i)for(i)in(self.data_set)])/len(self.data_set))
  def median(self)->float:
    if(len(self.data_set)%2==0):
      return((self.data_set[len(self.data_set)//2]+self.data_set[len(self.data_set)//2-1])/2)
    else:
      return(self.data_set[len(self.data_set)//2])
  def mode(self)->float:
    count_dict={}
    for(i)in(self.data_set):
      if((i)in(count_dict)):
        count_dict[i]+=1
      else:
        count_dict[i]=1
    max_count=max(count_dict.values())
    mode_list=tuple([(k)for(k),(v)in(count_dict.items())if(v==max_count)])
    return(mode_list)