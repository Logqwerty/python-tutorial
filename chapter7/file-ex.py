import os

# C:\Users\My\Desktop\python\python-tutorial
# print(os.getcwd())

# fhand = open('chapter7/test.txt', encoding='utf-8')
# print(fhand)

# print('------------------')

# xfile = open('chapter7/mbox.txt', encoding='utf-8')

# count = 0
# for line in xfile: # 파일 한 줄씩 읽기
#     count += 1
#     print(count, line)

# print('Line Count: ', count)

# print('------------------')

# xfile = open('chapter7/mbox.txt', encoding='utf-8')
# inp = xfile.read() # 파일 전체 읽기 => 개행문자 포함 하나의 문자열로
# print(len(inp))
# print(inp[:20])

# print('------------------')

# xfile = open('chapter7/mbox.txt', encoding='utf-8')
# for line in xfile:
#     if line.startswith('From:'):
#         print(line.rstrip())

# print('------------------')

# xfile = open('chapter7/mbox.txt', encoding='utf-8')
# for line in xfile:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print(line)

# print('------------------')

# xfile = open('chapter7/mbox.txt', encoding='utf-8')
# for line in xfile:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line:
#         continue
#     print(line)

print('------------------')

fname = input('Enter the file name: ')
fname = 'chapter7/' + fname

try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
    
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count += 1
print('There were', count, 'subject lines in', fname)