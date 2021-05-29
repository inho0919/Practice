line = input()

text = ''

for i in range(0, len(line)):
  if(line[i] != ' '):
    if(line[i] == 'z'):
      chars = 'c'
      text = text + chars
    elif(line[i] == 'y'):
      chars = 'b'
      text = text + chars
    elif(line[i] == 'x'):
      chars = 'a'
      text = text + chars
    else:
      chars = ord(line[i])
      chars = chars + 3
      text = text + chr(chars)
    
  else:
    text = text + ' '

print(text)
