# Description that can be used on a readme or something of the sort:
# This script is used to turn a srcML-generated format into a Tuple Attribute format to be compared
# with the two other methods of dependency extraction.

# This script does one thing::
# 
# Take this:
# hbase-2.1.0\hbase-zookeeper\src\test\java\org\apache\hadoop\hbase\zookeeper\TestInstancePending.java org.apache.hadoop.hbase.HBaseClassTestRule
# And turn it into something like this:
# cLinks hbase-zookeeper/src/test/java/org/apache/hadoop/hbase/zookeeper/TestInstancePending.java hbase-common/src/test/java/org/apache/hadoop/hbase/HBaseClassTestRule.java

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
    if 'org.apache.hadoop.hbase' in pkg:
        # print(pkg)
        pkg_split = pkg.split('.')

        filename = f'{pkg_split[-1]}.java'
        # print(f'Finding {filename}')

        result = find(filename, 'hbase-2.1.0')
        if result == None:
            result = 'nope111'
    else:
        result = 'nope111'

    return result

# Hello, TA. I wanted to take this time to wish you a great day. Also inform you that f1 is the XML format and out is the output of the Tuple Attributes.
f1 = open('newconcat', 'r', encoding='utf-8')

out = open('srcml7.ta', 'a', encoding='utf-8')

if sum(1 for line in open('text.txt')) == sum(1 for line in open('text2.txt')):
    # print('same')

    f1_lines = f1.read().split('\n')

    for i in f1_lines:
        a = i.split(' ')
        if len(a) == 2:
            shit = get_hbase_dir(a[1])
            if not shit == 'nope111':
                out.write(f'cLinks {a[0]} {shit}\r\n')
        

    f1.close()
    out.close()
