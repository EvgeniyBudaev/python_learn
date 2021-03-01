# walrus = False
# print(walrus)

print(walrus := True)

# ===

# rows = input('Enter the number: ')
# for i in range(int(rows)):
#     print('*' * (i+1))
# print(f'Number of rows: {rows}')

for i in range(rows := int(input('Enter the number'))):
    print('*' * (i+1))
print(f'Number of rows: {rows}')

# ===

# def read_file(fp):
#     while True:
#         line = fp.readline()
#         if not line:
#             break
#
#         split_line = line.split(';')
#         print(split_line[1])


def read_file(fp):
    while line := fp.readline():
        if not line:
            break

        split_line = line.split(';')
        print(split_line[1])