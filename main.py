# Built-in imports
def reverse(txt: str) -> str:
  """
  Revserses a string
  
  Parameter
  ----------
  txt: str
    The string to reverse

  Returns
  ----------
  str
    The reversed string
  """
  if txt:
    return reverse(txt[1:])+txt[0]
  else:
    return txt

def is_palindrome(txt: str) -> bool:
  """
  checks if the string is a palindrome
  
  Parameter
  ----------
  txt: str
    The string to check

  Returns
  ----------
  bool
    whether the string is palindrome
  """
  if len(txt)<2:
    return True
  txt = txt.strip()
  txt = txt.replace('.','').replace(',','')
  if txt[0] == txt[-1]:
    return is_palindrome(txt[1:-1])
  else:
    return False

#print(is_palindrome('hello'))