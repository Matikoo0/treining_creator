import jsonschema
import os
import configparser

config = configparser.ConfigParser()
config.read('../config')

ERRORPATH=config['ERROR']['PATH']

def read_schema():
    with open('schema.json','r')as f:
        schema=f.read()
        f.close()
    return schema


def validate_json(json_data):
    schema=read_schema()
    try:
        jsonschema.validate(json_data,schema)
    except jsonschema.ValidationError as e:
        return False,e.message
    return True,None

def handle_error(error:str,json_data:str):
    global ERRORPATH
    file=os.listdir(ERRORPATH)
    for i in range(1,10):
        if f"{i}.error" not in file:
            with open(f"{i}.txt",'w') as f:
                f.write(error)
                f.write("\n\n")
                f.write(json_data)
                f.close()
            break

