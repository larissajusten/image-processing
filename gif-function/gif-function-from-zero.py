from struct import unpack as unpck

with open('primeira-gif.gif', mode='rb') as file: # b is important -> binary
  gifSignature = file.read(4)
  gifVersion = file.read(2)
  gifWidth = file.read(2)
  gifHeigth = file.read(2)
  gifFlags = file.read(1)

  gifGCTSize= int(((1<<(gifFlags and 0b111) +1)*3)/8)

  gifGCT = file.read(gifGCTSize)
  extensionBlock = file.read(8)
  #Image header contains 11 bytes, but the last is the flag (the only important byte for us now)
  imgBlockHeader = file.read(10)
  imgBlockFlags = file.read(1)
  print(bin(imgBlockHeader[0]))
  print(bin(imgBlockFlags[0]))
  if(bin(imgBlockFlags[0]).lstrip('0b')[0] == '0'):
    print("não tem essa merdaaa")
  else:
    print("tem essa merda")

  # imgBlockGCTSize = int(((1<<(imgBlockFlags and 0b111) +1)*3)/8)

  print('[gif] signatura:', gifSignature)
  print('[gif] version:', gifVersion)
  print('[gif] width:', gifWidth)
  print('[gif] heigth:', gifHeigth)
  print('[gif] flags:', gifFlags)
  print('[gif] global color table:', gifGCT)
  print('extensionBlock:', extensionBlock)
  print('[img] header:', imgBlockHeader)
  print('[img] flags:', imgBlockFlags)


# print(int.from_bytes(flags, byteorder='little'))
#   allFileContent = file.read()
# print(allFileContent)

# header = unpck("iiiii", fileContent[:20])
# body = unpck("i" * ((len(fileContent) -24) // 4), fileContent[20:-4])
# footer = unpck("i", fileContent[-4:])

# print('header:', header)
# print('body:', body)
# print('footer:', footer)