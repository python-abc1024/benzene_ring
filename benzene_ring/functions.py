"""
—————————————————————————————————————————————————————————
| @version    : v0.1.0                                  |
| @author     : yangjinhe                               |
| @time       : 2025/2/22 21:10                         |
| @describe   : tool                                    |
| @software   : Visual Studio Code                      |
| @filename   : functions.py                            |
| @package    : benzene_ring                            |
—————————————————————————————————————————————————————————
"""
__all__=["deduplication"]

def deduplication(iterable,return_type=list):
  """
  Benzene_ring deduplication function.
  Used to remove duplicate elements from an iterable object.
  ---
  parameters:
  iterable: The iterable object to be deduplicated
  return_type: The type of the object to be returned: list, tuple, set
  """
  return(return_type(set(iterable)))