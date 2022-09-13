import numpy as np
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
        cell = sheet0.cell(row, col)
        print(cell.value, end=' | ')
        if col == ncols - 1:
            print()

print()
print()

# 取值
# 统计项(多为正面指标): 时间, 投篮, 三分, 发球, 篮板, 助攻, 抢断, 盖帽, 失误[负面指标], 得分. 共10项

arr = np.zeros((nrows - 1, 12), dtype=float)
for row in range(nrows - 1):
    arrRow = np.zeros((1, 12), dtype=float)
    # 首发出场数
    arrRow[0, 0] = sheet0.cell(row + 1, 3).value
    # 上场时间(min)
    arrRow[0, 1] = sheet0.cell(row + 1, 4).value
    # 投篮命中数
    arrRow[0, 2] = sheet0.cell(row + 1, 6).value
    # 三分命中数
    arrRow[0, 3] = sheet0.cell(row + 1, 9).value
    # 罚球命中数
    arrRow[0, 4] = sheet0.cell(row + 1, 12).value
    # 篮板数
    arrRow[0, 5] = sheet0.cell(row + 1, 14).value
    # 助攻
    arrRow[0, 6] = sheet0.cell(row + 1, 17).value
    # 抢断
    arrRow[0, 7] = sheet0.cell(row + 1, 18).value
    # 盖帽
    arrRow[0, 8] = sheet0.cell(row + 1, 19).value
    # 失误(负面指标)
    arrRow[0, 9] = sheet0.cell(row + 1, 20).value
    # 犯规(负面指标)
    arrRow[0, 10] = sheet0.cell(row + 1, 21).value
    # 得分
    arrRow[0, 11] = sheet0.cell(row + 1, 22).value
    arr[row] = arrRow

print(arr)
print(arr.shape)


# 定义一个函数, 计算两个向量之间的余弦夹角
def are_u_ok(arr1, arr2):
    dot = np.dot(arr1, arr2)
    denom = np.linalg.norm(arr1) * np.linalg.norm(arr2);
    return (float)(dot) / denom


print()
print()

# question: 计算出kobe哪两年的表现最为相似
for row in range(arr.shape[0]):
    if row < arr.shape[0] - 1:
        res = are_u_ok(arr[row], arr[row + 1])
        print('{:<2} - {:>2}  ==>  {:<6}'.format(row, row + 1, res))
    else:
        res = are_u_ok(arr[0], arr[row])
        print('{:<2} - {:>2}  ==>  {:<6}'.format(row, 0, res))
