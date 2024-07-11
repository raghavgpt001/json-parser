import json

def step1(input):
    input = input.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")

    if not (input[0] == "{" and input[-1] == "}"):
        print("Step 1: Failed")
        return False

    input = input[1:-1]
    if input == "":
        return True
    
    list = input.split(",")
    print("input", input)
    print("list", list)

    for i in list:
        kv = i.split(":")
        if len(kv)==2:
            key, value = kv[0], kv[1]
            # check validity of key
            if not (key[0]=='"' and key[-1]=='"'):
                print("key", key)
                print("Step 2: Failed")
                return False
            if not checkValue(value):
                print("value", value)
                print("Step 2: Failed")
                return False
        else:
            print("kv", kv)
            print("Step 2: Failed")

    print("Step 2: Passed")
    return True

def checkValue(value):
    # check string
    if value[0]=='"' and value[-1]=='"':
        return True
    if value=="true" or value=="false":
        return True
    if value=="null":
        return True
    if value.isdigit():
        return True
    if value[0]=='[' and value[-1]==']':
        return True
    if step1(value):
        return True
    return False

def main():
    # Path to your JSON file
    file_path = 'data.json'

    # Read and parse JSON file
    with open(file_path, 'r') as file:
        input = file.read()

    print(input)

    return step1(input)


main()