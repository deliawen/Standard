# -*- coding: utf-8 -*-

import os
import re
import urllib


def genSpec(type):
    mdContent = []
    catalogFile = open(type + '/README.md', 'r')
    rootChapter = {
        'title': 'root',
        'children': []
    }
    readState = [ 0, 0, 0, 0 ]
    

    # read title
    titleFile = open(type + '/title.md', 'r');
    title = titleFile.read();
    titleFile.close()


    for line in catalogFile.readlines():
        match = re.search('\[[^\]]+\]\(([^\)]+)\)', line)
        
        if match is not None:
            chapter = type + '/' + match.group(1)
            
            if os.path.exists(chapter):
                genChapter(chapter, mdContent, readState, rootChapter)

    catalogFile.close()

    output = open(type + '-github.md', 'w')
    output.write(title + genCatalog(rootChapter) + ''.join(mdContent))
    output.close()


def genCatalog(root):
    catalogContent = []
    catalogContent.append('\n\n')

    for node in root['children']:
        genCatalogNode(node, catalogContent, 0)

    catalogContent.append('\n\n')
    return '\n\n'.join(catalogContent)

def genCatalogNode(node, catalogContent, level):
    catalogContent.append(level * '　　' + '[{}](#user-content-{})'.format(node['title'], titleHash(node['title'])))
    for child in node['children']:
        genCatalogNode(child, catalogContent, level + 1)

def genChapter(chapter, contentBucket, readState, rootChapter):
    chapterFile = open(chapter, 'r')
    for line in chapterFile:
        match = re.search('^(#(#+)\s+)[^\[]', line)

        if match is not None:

            level = len(match.group(2))
            title = line[len(match.group(1)):]
            titleIndex = []
            parentNode = rootChapter

            for i in range(4):
                if i == level - 1:
                    readState[i] += 1
                    titleIndex.append(str(readState[i]))
                    title =  '.'.join(titleIndex) + ' ' + title.strip()
                    parentNode['children'].append({
                        'title': title,
                        'children': []
                    })
                elif i >= level:
                    readState[i] = 0
                else:
                    parentNode = parentNode['children'][readState[i] - 1]
                    titleIndex.append(str(readState[i]))
            
            contentBucket.append((level + 1) * '#' + ' ' + title + '\n\n')

        else:

            contentBucket.append(line)

    contentBucket.append('\n\n\n')
    chapterFile.close()

def titleHash(title):
    return urllib.quote(re.sub(
            '\s+', 
            ' ', 
            title.strip().lower().replace('.', '').replace('(', '').replace(')', '').replace('!', '')
        ).replace(' ', '-'))

genSpec('javascript')
genSpec('css')
genSpec('html')
genSpec('es-next')


