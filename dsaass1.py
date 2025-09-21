class hashtable:
def __init__(self):# Initialize hash table properties self.m =
int(input("Enter size of hash table: ")) # Size of hash table
self.hashTable = [None] * self.m # Initialize hash table with none
self.elecount = 0 # Count of elements inserted self.comparisons =
0 # Track number of comparisons
print("Initialized hash table:", self.hashTable)

# Hash function to calculate the index for a key
def hashFunction(self, key): return key %
self.m

def isfull(self): # check if the hash table is full
return self.elecount == self.m

# Insert using Linear Probing
def linearprobe(self, key, data):
index = self.hashFunction(key) # Calculate hash index compare = 0 #
Counter for comparisons while self.hashTable[index] is not None: # Loop
until an empty slot is found index = (index + 1) % self.m # Move to the
next index (circular) compare += 1
self.hashTable[index] = [key, data] # Insert key-data pair
self.elecount += 1 # Increment element count print("Data
inserted at index", index) print("Hash table:",
self.hashTable) print("Number of comparisons (Linear
Probing):", compare)

# Search using Linear Probing def getlinear(self, key, data): index =
self.hashFunction(key) while self.hashTable[index] is not None: #
Traverse until an empty slot if self.hashTable[index] == [key, data]: #
Key found return index index = (index + 1) % self.m # Move to the
next index (circular) return None # Key not found

# Insert using Quadratic Probing

def quadraticprobe(self, key, data): index = self.hashFunction(key)
compare = 0 # Counter for comparisons i = 0 # Step counter for quadratic
probing while self.hashTable[index] is not None: # Loop until an empty slot
is found i += 1 index = (index + i * i) % self.m # Quadratic probing formula
compare += 1
self.hashTable[index] = [key, data] # Insert key-data pair
self.elecount += 1 # Increment element count print("Data
inserted at index", index) print("Hash table:", self.hashTable)
print("Number of comparisons (Quadratic Probing):", compare)

# Search using Quadratic Probing
def getQuadratic(self, key, data):
index = self.hashFunction(key)
i = 0
while self.hashTable[index] is not None: # Traverse until an empty slot
if self.hashTable[index] == [key, data]: # Key found return index
i += 1

index = (index + i * i) % self.m # Quadratic probing formula

return None # Key not found

# Wrapper for Linear Probing insertion def
insertvialinear(self, key, data): if self.isfull(): #
Check if the table is full print("Table is full") return
False index = self.hashFunction(key) if

self.hashTable[index] is None: # No collision
self.hashTable[index] = [key, data] self.elecount
+= 1

print("Data inserted at index", index) print("Hash
table:", self.hashTable) else: # Collision occurred
print("Collision occurred, applying Linear Probing")
self.linearprobe(key, data)

# Wrapper for Quadratic Probing insertion def
insertviaQuadratic(self, key, data): if
self.isfull(): # Check if the table is full
print("Table is full") return False index =
self.hashFunction(key) if
self.hashTable[index] is None: # No collision
self.hashTable[index] = [key, data]
self.elecount += 1 print("Data inserted at
index", index) print("Hash table:",
self.hashTable)

else: # Collision occurred print("Collision occurred,
applying Quadratic Probing") self.quadraticprobe(key,
data)

# Menu function to interact with the hash table
def menu():
print("Welcome to Hash Table Program!") obj
= hashtable() # Initialize hash table object
ch = 0
while ch != 3:
print("\n********************")
print("1. Linear Probe")
print("2. Quadratic Probe")
print("3. Exit")
print("**********************")

ch = int(input("Enter your choice: "))
if ch == 1: # Menu for Linear
Probing ch2 = 0
while ch2 != 3: print("\n*** Linear
Probing Menu* **") print("1. Insert")
print("2. Search") print("3. Exit")

ch2 = int(input("Enter your choice: "))
if ch2 == 1:
a = int(input("Enter phone number (key): "))
b = input("Enter name (data): ")
obj.insertvialinear(a, b)
elif ch2 == 2:

k = int(input("Enter phone number to search: "))
b = input("Enter name to search: ") f =
obj.getlinear(k, b) if f is None:
print("Key not found")
else:
print("Key found at index:", f)
elif ch == 2: # Menu for
Quadratic Probing ch2 = 0
obj1 = hashtable() # Separate hash table for quadratic probing
while ch2 != 3: print("\n*** Quadratic Probing Menu ***")
print("1. Insert") print("2. Search") print("3. Exit") ch2 =
int(input("Enter your choice: ")) if ch2 == 1:
a = int(input("Enter phone number (key): "))
b = input("Enter name (data): ")
obj1.insertviaQuadratic(a, b) elif ch2 == 2:
k = int(input("Enter phone number to search: "))
b = input("Enter name to search: ") f =
obj1.getQuadratic(k, b) if f is None:
print("Key not found")
else:
print("Key found at index:", f)
# start the program menu()