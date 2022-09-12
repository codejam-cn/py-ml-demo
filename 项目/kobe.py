import xlrd3

data = xlrd3.open_workbook(r'resources/NBA-data.xlsx')

# table1 = data.sheet_names();

sheet0 = data.sheet_by_index(0)

nrows = sheet0.nrows
ncols = sheet0.ncols

print(nrows)

for row in range(nrows):
    for col in range(ncols):
        print(sheet0.cell(row, col), end='')
        if col == ncols - 1:
            print()
