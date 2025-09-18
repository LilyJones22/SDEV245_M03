import hashlib # used for hashing

message = input("Enter message: ")
                
hashed = hashlib.sha256(message.encode()).hexdigest() # creating hash

print("\nIt's a secret to everybody")
print("         (now)")
print("-" * 26)
print("    [HASHED MESSAGE]")

print(hashed)