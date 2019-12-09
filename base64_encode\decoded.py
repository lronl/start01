import base64
def encoding(var1):
  encoded = base64.b64encode(var1.encode('ascii'))
  print(encoded)
  return
 
def decoding(var2):
  decode = base64.b64decode(var2)
  print(decode)
  return

q= True
while q:
  print("What are we doing (encoded ore decoded) ?:")
  name = input("Your choice?:")
  if ('encode' in ("%s" % name )):
    print(name)
    var1 = input("String to encode?:")
    encoding(var1)
 
  elif ('decode' in ("%s" % name )):
      print(name)
      var2 = input("String to decode?:")
      decoding(var2)
 
  elif ('exit' in ("%s" % name )):
    q = False
