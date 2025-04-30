import random

pwd_hardness = 4

def encrypt(dpwd):
    all_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '@', '#', '$', '%', '&', '!']
    list_of_encrypted_dpwd_chars = []
    for i in dpwd[::-1]:
        left_random_codes = ''
        right_random_codes = ''
        for j in range(pwd_hardness):
            left_random_codes = left_random_codes + random.choice(all_chars)
            right_random_codes = right_random_codes + random.choice(all_chars)
        list_of_encrypted_dpwd_chars.append(left_random_codes + str(i) + right_random_codes)
    encrypted_dpwd = ''.join(list_of_encrypted_dpwd_chars)
    return encrypted_dpwd

def decrypt(epwd):
    len_of_single_char_of_epwd = (2 * pwd_hardness) + 1
    dpwd = ''
    new_epwd = ' ' * pwd_hardness + epwd + ' ' * pwd_hardness
    indexes_of_dpwd_chars_in_epwd = [(i * len_of_single_char_of_epwd) - 1 for i in range(int(len(epwd) / len_of_single_char_of_epwd) + 1)]
    for i in indexes_of_dpwd_chars_in_epwd:
        dpwd = dpwd + new_epwd[i]
    return dpwd[::-1]

def pwd_management():
    mstr_pwd = input('Enter Master Password: ')
    while True:
        user_input = input('Enter your choice: [A]DD a password [V]IEW password list [Q]UIT\n> ')
        if user_input in 'aA':
            with open('Python-Projects\\P05 Password Manager\\password_manager.txt', 'a') as file:
                username = input('Enter username: ')
                password = input('Enter password: ')
                file.writelines([username, '|', encrypt(password),'\n'])
                print('* added successfully *')
        elif user_input in 'vV':
            if mstr_pwd == 'amrit':
                with open('Python-Projects\\P05 Password Manager\\password_manager.txt', 'r') as file:
                    content = file.readlines()
                    for i in content:
                        dpwd = i[i.find('|') + 1:-1]
                        print(f'Username: {i[:i.find('|')]}\nPassword: {decrypt(dpwd)}\n')
            else:
                with open('Python-Projects\\P05 Password Manager\\password_manager.txt', 'r') as file:
                    content = file.readlines()
                    for i in content:
                        print(f'Username: {i[:i.find('|')]}\nPassword: {i[i.find('|') + 1:-1]}\n')
        elif user_input in 'qQ':
            exit()
        else:
            print('invalid input')

pwd_management()
#