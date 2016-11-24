def ransom_note(magazine, ransom):
    flag = True
    for val in ransom:
        print(val)
        if val not in magazine:
            flag = False
        else:
            magazine.remove(val)

    return flag



def list_to_hash(my_list):
    dictionary = {}
    for i in my_list:
        dictionary[i] = 1

    return dictionary


def ransom_note_hash(magazine, ransom):
    hashed_magazine = list_to_hash(magazine)

    for val in ransom:
        if val not in hashed_magazine:
            return False
        else:
            del hashed_magazine[val]
    return True



m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')

ransom = input().strip().split(' ')

source = {}
answer = ransom_note_hash(magazine, ransom)
if answer:
    print("Yes")
else:
    print("No")
