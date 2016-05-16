# 将一个包含多个列表的列表中的元素按照每个子列表相同索引成一行打印出来.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def x2y(lists=None):
    if lists is None:
        lists = []
    for y in range(len(grid[0])):
        print('')
        for x in range(len(grid)):
            show = ''
            show += grid[x][y]
            print(show, end='')

x2y(grid)

