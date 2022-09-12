import xlrd3

data = xlrd3.open_workbook(r'resources/NBA-data.xlsx')

# table1 = data.sheet_names();

sheet0 = data.sheet_by_index(0)

nrows = sheet0.nrows
ncols = sheet0.ncols

print(nrows)

# text:'赛季'text:'球队'text:'出场'text:'首发'text:'时间'text:'投篮'text:'命中'text:'出手'text:'三分'text:'命中'text:'出手'text:'罚球'text:'命中'text:'出手'text:'篮板'text:'前场'text:'后场'text:'助攻'text:'抢断'text:'盖帽'text:'失误'text:'犯规'text:'得分'text:'胜'text:'负'
for row in range(nrows):
    for col in range(ncols):
        print(sheet0.cell(row, col), end='')
        if col == ncols - 1:
            print()
