def defangIPaddr(address):
  address.split('.')
  s = '[.]'
  return s.join(address.split('.'))


print(defangIPaddr("1.1.1.1"))