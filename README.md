# A better library of python tools
## Installation or uninstallation
```shell
pip3 install benzene-ring
pip3 uninstall benzene-ring
```
## import
```python
1. import benzene_ring
2. from benzene import *
```
## Content
- _iterable_
  1. range()
  2. enumerate()
  3. map()
- _function_
  1. deduplication
## Example
- range
```python
import benzene_ring
a=benzene_ring.iterable.range(stop=10)
print(list(a))
>>> [0,1,2,3,4,5,6,7,8,9]
```
- map
```python
import benzene_ring
a=benzene_ring.iterable.map(function=lambda x:x**2,iterable=[1,2,3])
print(list(a))
>>> [1,4,9]
```
## Common mistakes
### "TypeError: '' object is not iterable"
  - Solution: Check whether the value of the iterable parameter is an iterable object