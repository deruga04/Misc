import re
import pdb
import status_messages as stat
import traceback

def parse_files(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        
        stat.print_success('File ' + filename + ' found!')
        print('Building vocabulary list...')

        keywords_raw = file.read().strip()
        
        file.close()
        
        groups = re.split(r'\n{2,}', keywords_raw)

        keywords = {};

        for g in groups:
            group_parse = g.split('\n')
            result = re.sub(r'^[[]|[]]$', '', group_parse[0])
            print(result)
            keywords[result] = group_parse[1:]
            # print(group_name)

            #for p in group_parse[1:]:
                # pair = re.split(r'(\b=\b|\s{1,}=\s{1,})', p)
                # print(pair[0] + pair[1])
		
               # keywords[result].extend(p)

    except Exception as e:
        keywords = {}
        #stat.print_fail('File location ' + filename + ' not found. Please double-check the file name and make sure it exists.')
        print(traceback.format_exc())

    return keywords

def to_xml(data):
    pass

parse_files('test.txt')
