listData=[10,20,30,40,50]
print(type(listData))

byteData=bytes(listData)
print(byteData)

# Decode the bytes to a string
decodedData = byteData.decode()

# Print the data in bytes
print("Data in bytes:")
for byte in byteData:
    print(byte)

bytearrays=bytearray(listData)
print(bytearrays)

# Print the data in bytearray
print("\nData in bytearray:")
for byte in bytearrays:
    print(byte)

# Print the decoded data
print("\nDecoded data:")
print(decodedData)