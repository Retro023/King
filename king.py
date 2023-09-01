#!/usr/bin python3
# auto add your username to king file

def search_str(file_path, word):
        with open(file_path, 'r') as file:
                content = file.read()
        if word in content:
                print("name is still in king")

        else:
                fp = open('test.txt', 'w')
                fp.write('Retro0989')
                fp.close()

search_str(r'/root/king.txt', 'USERNAME')
