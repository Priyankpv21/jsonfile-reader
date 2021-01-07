import json

def read_json(json_filename):

    
    file = open(json_filename,"r")
    data = json.load(file)
    file.close()
    return data