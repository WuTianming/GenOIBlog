#!/bin/env python

import sys
import datetime

name = input('题目中文名: ')
nameEN = input('题目英文名: ')
fname = 'source/_posts/' + nameEN.lower() + '.md'
print('保存位置[回车默认为' + fname + ']:')
readln = sys.stdin.readline().strip()
if readln != '':
    fname = readln
f = open(fname, 'w')
f.write('---\ntitle: ' + nameEN.lower() + '\ndate: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\ntags: [OI,Programming]\ncategories: OI\n---\n')
f.write('## ' + name + ' / ' + nameEN.capitalize() + '\n\n### 问题描述\n')
print('题目描述: (空行表示结束)')
readln = sys.stdin.readline().strip().replace(',', '，')
while not readln == '':
    f.write(readln)
    readln = sys.stdin.readline().strip().replace(',', '，')
f.write('\n\n<!--more-->\n\n### 输入格式\n')
print('输入格式: (空行表示结束)')
readln = sys.stdin.readline().strip().replace(',', '，')
while not readln == '':
    f.write(readln)
    readln = sys.stdin.readline().strip().replace(',', '，')
f.write('\n\n### 输出格式\n')
print('输出格式: (空行表示结束)')
readln = sys.stdin.readline().strip().replace(',', '，')
while not readln == '':
    f.write(readln)
    readln = sys.stdin.readline().strip().replace(',', '，')
cnt = int(input('样例数据组数: '))
if not cnt == 0:
    f.write('\n\n### 样例数据\n')
    if cnt == 1:
        sampleIn = []
        sampleOut = []
        inLine = 0
        outLine = 0
        print('样例输入: (空行表示结束)')  
        readln = sys.stdin.readline().rstrip()
        while not readln == '':
            inLine += 1
            sampleIn.append(readln)
            readln = sys.stdin.readline().rstrip()
        print('样例输出: (空行表示结束)')  
        readln = sys.stdin.readline().rstrip()
        while not readln == '':
            outLine += 1
            sampleOut.append(readln)
            readln = sys.stdin.readline().rstrip()
        f.write(' ' + nameEN + '.in | ' + nameEN + '.out\n' + '-' * (len(nameEN) + 5) + '|' + '-' * (len(nameEN) + 6) + '\n')
        totLine = max(inLine, outLine)
        for i in range(0, totLine):
            if (i >= inLine):
                f.write(' | ' + sampleOut[i] + '\n')
            elif (i >= outLine):
                f.write(sampleIn[i] + ' | \n')
            else:
                f.write(sampleIn[i] + ' | ' + sampleOut[i] + '\n')
    else:
        for i in range(0, cnt):
            sampleIn = []
            sampleOut = []
            inLine = 0
            outLine = 0
            print('样例输入 #' + str(i + 1) + ': (空行表示结束)')
            readln = sys.stdin.readline().rstrip()
            while not readln == '':
                inLine += 1
                sampleIn.append(readln)
                readln = sys.stdin.readline().rstrip()
            print('样例输出 #' + str(i + 1) + ': (空行表示结束)')
            readln = sys.stdin.readline().rstrip()
            while not readln == '':
                outLine += 1
                sampleOut.append(readln)
                readln = sys.stdin.readline().rstrip()
            f.write(' ' + nameEN + str(i + 1) + '.in | ' + nameEN + str(i + 1) + '.out\n' + '-' * (len(nameEN) + 5 + len(str(i + 1))) + '|' + '-' * (len(nameEN) + 6 + len(str(i + 1))) + '\n')
            totLine = max(inLine, outLine)
            for i in range(0, totLine):
                if (i >= inLine):
                    f.write(' | ' + sampleOut[i] + '\n')
                elif (i >= outLine):
                    f.write(sampleIn[i] + ' | \n')
                else:
                    f.write(sampleIn[i] + ' | ' + sampleOut[i] + '\n')
            f.write('\n')
print('数据范围: (空行表示结束, 无内容则省略)')
readln = sys.stdin.readline().strip().replace(',', '，')
hasContent = False
while not readln == '':
    if (hasContent == False):
        hasContent = True
    f.write('\n### 数据范围\n')
    f.write(readln + '\n')
    readln = sys.stdin.readline().strip().replace(',', '，')
f.close()
