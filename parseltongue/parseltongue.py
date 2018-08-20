import re
import pdb
import traceback
import xml.sax.xmlreader
import xml.sax.saxutils
from lxml import etree as et

def parse_files(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        
        keywords_raw = file.read().strip()
        
        file.close()
        
        groups = re.split(r'\n{2,}', keywords_raw)

        keywords = {};

        for g in groups:
            group_parse = g.split('\n')
            result = re.sub(r'^[[]|[]]$', '', group_parse[0])
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

'''
def to_xml(file, data):
    attr0 = xml.sax.xmlreader.AttributesImpl({})
    x =  xml.sax.saxutils.XMLGenerator(file)
    x.startDocument()
    x.startElement('Synonyms', attr0)
    
    for k in data.keys():
        for word in data[k]:
            
            x.startElement('Variant', attr0)
            x.characters(k)
            x.endElement(word)

    x.endElement('Synonyms')
    x.endDocument()
'''

def to_xml2(file, data):
    root = et.Element('Synonyms')
    
    for k in data.keys():
        for word in data[k]:
            synonym = et.SubElement(root, 'Synonym', term=word)
            variant = et.SubElement(synonym, 'Variant')
            variant.text = k
    file.write('<?xml version=\'1.0\' encoding=\'UTF-8\'?')
    file.write(et.tostring(root, pretty_print=True))


input = parse_files('test.txt')
keywords_file = open('keywords.xml', 'wb')
to_xml2(keywords_file, input)
keywords_file.close()
