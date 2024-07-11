import json
import re
def validateJSON(input):
    """
    Validates whether the given input is a valid JSON string.

    Args:
        input (str): The input string to be validated.

    Returns:
        bool: True if the input is a valid JSON string, False otherwise.
    """

    if not (input[0] == "{" and input[-1] == "}"):
        return False

    input = input[1:-1]
    if input == "":
        return True
    
    # split by comma
    list = []
    stack_object = []
    inside_string = False

    item = ""
    for i in input:
        if i=='"':
            inside_string = not inside_string
            item += i
        elif i=="," and len(stack_object)==0 and inside_string==False:
            list.append(item)
            item=""
        elif i=="{" and inside_string==False:
            stack_object.append(i)
            item += i
        elif i=="}" and stack_object[-1]=="{" and inside_string==False:
            stack_object.pop()
            item += i
        else:
            item+=i
    list.append(item)

    print("list", list)

    for element in list:
        # split by colon
        kv = []
        inside_string = False
        item = ""
        for j in element:
            if j=='"':
                inside_string = not inside_string
                item += j
            elif j==":" and inside_string==False:
                kv.append(item)
                item = element[len(item)+1:]
                break
            else:
                item+=j
        kv.append(item)

        if len(kv)==2:
            key, value = kv[0], kv[1]
            # check validity of key
            if not (key[0]=='"' and key[-1]=='"'):
                print("invalid key", key)
                return False
            if not checkValue(value):
                print("invalid value", value)
                return False
        else:
            print("invalid key value pair:", kv)
            return False

    return True

def checkValue(value):
    # check string
    if value[0]=='"' and value[-1]=='"':
        return True
    if value=="true" or value=="false":
        return True
    if value=="null":
        return True
    # check number
    pattern = r'^(?:-?(?:0|[1-9]\d*)(?:\.\d+)?|\.\d+)$'
    if re.match(pattern, value):
        return True
    if value.isdigit() and value[0]!="0":
        return True
    if value[0]=='[' and value[-1]==']':
        return True
    # check json object
    if validateJSON(value):
        return True
    return False

def main():
    # Path to your JSON file
    file_path = 'data.json'

    # Read and parse JSON file
    with open(file_path, 'r') as file:
        input = file.read()

    input = input.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "")
    
    if validateJSON(input):
        print("Valid JSON")
    else:
        print("Invalid JSON")


main()