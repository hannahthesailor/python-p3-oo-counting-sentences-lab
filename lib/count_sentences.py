#!/usr/bin/env python3


class MyString:

  def __init__(self, value=''):
      self.value = value
  
  def get_value(self):
      return self.get_value
  
  def set_value(self, value):
      if not isinstance(value, str):
        print("The value must be a string.")
      else:
         self._value = value

  value = property(get_value, set_value)
  
  def is_sentence(self):
    if self._value.endswith('.'):
        return True
    else:
        return False
    
  def is_question(self):
    if self._value.endswith('?'):
        return True
    else:
        return False
    
  def is_exclamation(self):
    if self._value.endswith('!'):
        return True
    else:
        return False
    
  def count_sentences(self):
        # Split the string by '.', '?', and '!'
        sentences = filter(None, self._value.split('.'))
        sentences = sum(map(lambda x: x.split('!'), sentences), [])
        sentences = sum(map(lambda x: x.split('?'), sentences), [])
        # Count the non-empty strings
        return sum(1 for sentence in sentences if sentence.strip())
      
