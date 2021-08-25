################################################################
#  Build AMDACPexp Multiple Item updated adrenalin file
#
#  build.py
#
#  Author: Ravi Durgaganesh Gonnabattual (rgonnaba@amd.com)
#
#  Copyright (c) 2021 AMD Inc.
#
#  Contains primary implementation for ACP JSON Assembly
################################################################

import json
import os

directory_path = os.getcwd()
print(directory_path)
directory_contents = os.listdir(directory_path)

f = open(directory_path+'\\adrenalin\\acpoemcfg0001.json')
master_data = json.load(f)


def compare(lst1, lst2):
    final_list = list(set(lst2) - set(lst1))
    return final_list


for item in directory_contents:
    if os.path.isdir(item):
        # print(item)
        if(item != 'adrenalin'):
            print(item)
            f = open(directory_path+'\\'+str(item)+'\\acpoemcfg0001.json')
            slave_data = json.load(f)

            print('\n')
            master_list = []
            slave_list = []

            for key in master_data[0].keys():
                print("master keys :"+key)
                master_list.append(key)
            print('\n')
            for key in slave_data[0].keys():
                print("slave keys :"+key)
                slave_list.append(key)

            diff_len = len(compare(master_list, slave_list))
            diff_list = compare(master_list, slave_list)

            print(diff_len)
            for key_name in diff_list:
                print("diff_list :"+key_name)

            print('\n')

           # print(slave_data[0][key_name])
            if diff_len > 0:
                for key_name in diff_list:
                   ##        print (key_name)
                    with open(directory_path+'\\adrenalin\\acpoemcfg0001.json', 'r+') as file:
                        # First we load existing data into a dict.
                        file_data = json.load(file)
                        file_data[0][str(key_name)
                                     ] = slave_data[0][str(key_name)]
                        # Sets file's current position at offset.
                        file.seek(0)
                        # convert back to json.
                        json.dump(file_data, file, indent=4)
                print('data updated')
            else:
                print('no_diff')
