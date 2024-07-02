#Command to run:  python .\FileHashing_v2.py TI64_THINWALL.txt  TI64_THINWALL_C.txt
import hashlib
import time
import sys

dict_={}
dict_c={}
file_path_original=""
file_path_modified=""
def ArgumentCheck():
    global file_path_original
    global file_path_modified
    if len(sys.argv) < 2:
        print("Please provide a file name as a command-line argument.")
        return False
    else:
        file_path_original = sys.argv[1]
        file_path_modified = sys.argv[2]
        print(f"Original File name provided: {file_path_original}")
        print(f"Modifed File name provided: {file_path_modified}")
        return True
        

def compute_file_hash(file_path, algorithm="sha256", buffer_size=20):
    hash_function = hashlib.new(algorithm)
    count = 1
    with open(file_path, 'r') as file:
        for line in file:
            #print(line.strip())  
            encoded_string = line.encode('utf-8')
            hashed = hashlib.sha256(encoded_string).hexdigest()
            dict_[count] = hashed
            count = count +1
    return dict_

def compute_file_hash_comp(file_path, algorithm="sha256", buffer_size=20):
    hash_function = hashlib.new(algorithm)
    count = 1
    with open(file_path, 'r') as file:
        for line in file:
            #print(line.strip()) 
            encoded_string = line.encode('utf-8')
            hashed = hashlib.sha256(encoded_string).hexdigest()
            dict_c[count] = hashed
            count = count +1
    return dict_c 

def compare_dictionaries(dict1, dict2):
    value = False
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1:
        if dict1[key] != dict2[key]:
            print("Modification detected at line ", key)
            value = True
    if value:
        return True
    else:
        return False

if ArgumentCheck() == False:
    exit()
print(f"Original File name provided: {file_path_original}")
print(f"Modifed File name provided: {file_path_modified}")
# Original file reading
#file_path = "TI64_THINWALL.txt"
start_time = time.time()
hash_value = compute_file_hash(file_path_original)
#print(f"SHA-256 hash of {file_path}: {hash_value}")
end_time = time.time()
elapsed_time = end_time - start_time
#print(f"Execution time: {elapsed_time} seconds")
for item in dict_.items():
    print(item)


# Compromised file reading
#file_path = "TI64_THINWALL - C.txt"
start_time = time.time()
hash_value2 = compute_file_hash_comp(file_path_modified)
#print(f"SHA-256 hash of {file_path}: {hash_value2}")
end_time = time.time()
elapsed_time = end_time - start_time
#print(f"Execution time: {elapsed_time} seconds")
#print("Line # hash: ", dict_)
for item in dict_c.items():
    print(item)

val = compare_dictionaries(dict_c,dict_)
if val == True:
    print("AM File Scanner: File is compromised...!")
else:
    print("AM File Scanner: No modification detected...!")    
