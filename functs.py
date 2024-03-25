import random
import time
import requests
from settings import debug

global first, second, third, fourth, mode_choice

def api_debug():
    debug = requests.get(url='https://lassehelbling.ch/api/transalator/transalator_app.php',params={'id':'debug'})
    print(debug.text)

def download_file(id_):
    file_content = requests.get(url='https://lassehelbling.ch/api/transalator/transalator_app.php',params={'id':id_}).text
    save_to_file(strip_metadata_from_file(file_content), 'data.txt')

def import_file(filename):
    first_part = []
    second_part = []
    third_part = []
    fourth_part = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split(';')
                first_part.append(parts[0])
                second_part.append(parts[1])
                third_part.append(int(parts[2]))  # Convert to integer
                fourth_part.append(int(parts[3].rstrip()))  # Convert to integer

    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
        if debug != 1:
            exit(1)
    except Exception as e:
        print("An error occurred while reading the file:", e)
        if debug != 1:
            exit(1)

    return first_part, second_part, third_part, fourth_part

def save_to_file(content, filename):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print("File saved successfully.")
    except Exception as e:
        print("An error occurred while writing to the file:", e)

def save():
    output_filename = 'data.txt'  # Specify the output filename
    save_to_file('\n'.join([f"{first[i]};{second[i]};{third[i]};{fourth[i]}" for i in range(len(first))]), output_filename)
    if debug == 1:
        print(f"Data saved to '{output_filename}'")

def ask(n):
    global mode_choice
    if mode_choice == '1':
        print('Translate: ' + first[n])
        sol = input()
        if sol.lower() in ['exit', 'quit']:
            save()
            print("Goodbye.")
            exit(0)
        elif sol == second[n]:
            print('Correct.')
            third[n] += 1
        else:
            print('Incorrect.')
            fourth[n] += 1
    else:
        print('Translate: ' + second[n])
        sol = input()
        if sol.lower() in ['exit', 'quit']:
            save()
            print("Goodbye.")
            exit(0)
        elif sol == first[n]:
            print('Correct.')
            third[n] += 1
        else:
            print('Incorrect.')
            fourth[n] += 1
    save()

def mainloop():
    item = algo_choice()
    ask(item)
    time.sleep(1)

def good_nogood_list():
    global fift
    fift = []
    for i in range(len(third)):
        fift.append(third[i] - fourth[i])

def algo_choice():
    good_nogood_list()
    choice_dict = {i: fift[i] for i in range(len(fift))}
    if debug == 1:
        print("choice_dict:", choice_dict)  # Add this line for debugging
    
    if choice_dict:
        choice_index = sorted(choice_dict.keys())[random.randint(0, len(choice_dict.keys()) - 1)]
        return choice_index
    else:
        print("Error: choice_dict is empty")
        return None

def mode():
    mode_input = input('1. 1 to 2\n2. 2 to 1\n')

    if mode_input not in ['1', '2']:
        print('Bad input: ' + mode_input)
        if debug != 1:
            exit(1)

    return mode_input

def strip_metadata_from_file(file_content):
    global stript_filecontent, stript_metadata
    lines = file_content.split('\n')
    stript_metadata = lines[0]
    stript_filecontent = ''.join(lines[1:])
    metadata_explode(stript_metadata)
    return stript_filecontent

def metadata_explode(meta):
    global name, createtime, id
    main_thing = meta.split(';')
    if debug == 1:
        print("main_thing:", main_thing)  # Add this line for debugging

    if len(main_thing) >= 2:
        id = main_thing[1]
        createtime = main_thing[2]
        name = main_thing[3]
    else:
        print("Metadata format error: Insufficient elements in main_thing")

def ids_download():
    global metadata
    ids = []
    names = []
    metadata = []
    idsndmore = requests.get('https://lassehelbling.ch/api/transalator/transalator_app.php', params={'doawnload_list': 'True'}).text
    lines = idsndmore.split('\n')
    for line in lines:
        parts = line.split(';')
        if len(parts) >= 4:
            ids.append(parts[0])
            metadata.append(parts[1])
            names.append(parts[2])
    
    return ids, names

def namesearch_for_ids(search):
    ids, names = ids_download()
    chosen_ids = []
    chosen_name = []
    i = 0
    for line in names:
        if line == search:
            chosen_ids.append(ids[i])
            chosen_name.append(names[i])

        i += 1
    out = ''
    i = 0

    for line in chosen_ids:
        out =  out + chosen_ids[i] + chosen_name[i] + '\n'
        i += 1
    
    return out

def downloadandload():
    download_file(input('File ID: '))
    first, second, third, fourth = import_file('data.txt')

def first_send():
    return first

def second_send():
    return second

def third_send():
    return third

def fourth_send():
    return fourth

def do_things_with_variables():
    global first, second, third, fourth
    first, second, third, fourth = import_file('data.txt')

def dododo():
    global mode_choice
    mode_choice = mode()

def main(mode_main):
    if mode_main == 1:
        dododo()
        i = 0
        while True:
            i += 1
            print('Question number:', i)
            mainloop()
    
    elif mode_main == 2:
        dododo()
        i = 0
        while True:
            i += 1
            print('Question number:', i)
            mainloop_multipel_choiche()

def mainloop_multipel_choiche():
    item = algo_choice()
    ask_mtp_c(item)
    time.sleep(1)

def ask_mtp_c(item):
    thing = [1,2,3]
    random.shuffle(thing)
    if mode == 1:
        print(f"Does '{first[item]}' Translate to:")
        for i in range(1,3):
            if thing[i] == 1:
                print('1: ' + second[item])
            elif thing[i] == 2:
                print('2: ' + second[item + 1])
            elif thing[i] == 3:
                print('3: ' + second[item - 1])

    elif mode == 2:
        print(f"Does '{second[item]}' Translate to:")
        for i in range(1,3):
            if thing[i] == 1:
                print('1: ' + first[item])
            elif thing[i] == 2:
                print('2: ' + first[item + 1])
            elif thing[i] == 3:
                print('3: ' + first[item - 1])

if __name__ == '__main__':
    print('debuging')
    api_debug()