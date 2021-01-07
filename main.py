import argparse
from lib import utils

parser = argparse.ArgumentParser(description='\nThis program Read JSON file... ')
parser.add_argument('file name',help='Add JSON file name') 
args = parser.parse_args()
file_name =  getattr(args,'file name')
json_data = utils.read_json(file_name)
print(json_data)