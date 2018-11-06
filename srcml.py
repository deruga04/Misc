import re
import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def get_hbase_dir(pkg):
    if 'org.apache.hadoop.hbase.' in pkg:
        # print(pkg)
        pkg_split = pkg.split('.')

        filename = f'{pkg_split[-1]}.java'
        # print(f'Finding {filename}')

        result = find(filename, 'hbase-2.1.0')
    else:
        result = pkg

    return result



f1 = open('text.txt', 'r', encoding='utf-8')
f2 = open('text2.txt', 'r', encoding='utf-8')

out = open('srcml.con.ta', 'a', encoding='utf-8')

if sum(1 for line in open('text.txt')) == sum(1 for line in open('text2.txt')):
    print('same')

    f1_raw = re.split(r'\n', f1.read())
    f2_raw = re.split(r'\n', f2.read())

    instance = set(f1_raw)

    for line in instance:
        out.write(f'$INSTANCE {line} clinks\r\n')
    

    # print(get_hbase_dir(f2_raw[0]))

    for i in range(0, len(f1_raw) - 1):
        out.write(f'clinks {f1_raw[i]} {get_hbase_dir(f2_raw[i])}\r\n')

    f1.close()
    f2.close()
    out.close()