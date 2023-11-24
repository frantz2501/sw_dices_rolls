import random
import csv

def roll_dice_uniq(init, n):
    r = random.randint(1, n)
    print('roll:', r)
    if r == n:
        r = r + roll_dice_uniq(r, n)
        print('roll_final_inter:', r)
        return r
    else:
        print('roll_final:', r)
        return r + init

def roll_savage_dices(n):
    die = roll_dice_uniq(0, n)
    wild_die = roll_dice_uniq(0, 6)
    return max(die, wild_die)

def generate_data(faces, iterations):
    dices_list = list()
    idx = 0
    while idx <= iterations:
        dices_list.append(roll_savage_dices(faces))
        idx += 1
    return dices_list

def generate_table(faces_list, table_name, iterations):
    table = list()
    for face in faces_list:
        table.append(generate_data(face, iterations))
    faces_list = ["d"+str(face) for face in faces_list]
    with open(table_name, 'w') as f:
        write = csv.writer(f)
        write.writerow(faces_list)
        write.writerows(table)

generate_table([4, 6, 8, 10, 12], 'tirage_sw.csv', 1)
