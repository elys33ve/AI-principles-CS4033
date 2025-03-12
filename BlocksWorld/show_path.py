

on='on'
table='table'
clear='clear'
a='🄰'
b='🄱'
c='🄲'
d='🄳'
e='🄴'
f='🄵'

n = 6
path = [[[clear,c],[clear,e],[on,e,table],[on,d,table],[on,a,d],[on,b,a],[on,c,f],[on,f,b]],
[[clear,f],[clear,c],[clear,e],[on,e,table],[on,d,table],[on,a,d],[on,b,a],[on,c,table],[on,f,b]],
[[clear,f],[clear,b],[clear,e],[on,e,table],[on,d,table],[on,a,d],[on,b,a],[on,c,table],[on,f,c]],
[[clear,a],[clear,b],[clear,e],[on,e,table],[on,d,table],[on,a,d],[on,b,f],[on,c,table],[on,f,c]],
[[clear,a],[clear,d],[clear,e],[on,e,table],[on,d,table],[on,a,b],[on,b,f],[on,c,table],[on,f,c]],
[[clear,a],[clear,d],[clear,b],[on,e,table],[on,d,table],[on,a,e],[on,b,f],[on,c,table],[on,f,c]],
[[clear,d],[clear,b],[on,e,table],[on,d,a],[on,a,e],[on,b,f],[on,c,table],[on,f,c]],
[[clear,f],[clear,b],[on,e,table],[on,d,a],[on,a,e],[on,b,d],[on,c,table],[on,f,c]],
[[clear,d],[clear,f],[clear,b],[on,e,table],[on,d,a],[on,a,e],[on,b,table],[on,c,table],[on,f,c]],
[[clear,d],[clear,a],[clear,b],[on,e,table],[on,d,f],[on,a,e],[on,b,table],[on,c,table],[on,f,c]],
[[clear,e],[clear,a],[clear,b],[on,e,table],[on,d,f],[on,a,d],[on,b,table],[on,c,table],[on,f,c]],
[[clear,e],[clear,a],[clear,d],[on,e,table],[on,d,f],[on,a,b],[on,b,table],[on,c,table],[on,f,c]],
[[clear,f],[clear,a],[clear,d],[on,e,table],[on,d,e],[on,a,b],[on,b,table],[on,c,table],[on,f,c]],
[[clear,f],[clear,c],[clear,d],[on,e,table],[on,d,e],[on,a,b],[on,b,table],[on,c,table],[on,f,a]],
[[clear,e],[clear,c],[clear,d],[on,e,table],[on,d,f],[on,a,b],[on,b,table],[on,c,table],[on,f,a]],
[[clear,e],[clear,f],[clear,d],[on,e,table],[on,d,c],[on,a,b],[on,b,table],[on,c,table],[on,f,a]],
[[clear,a],[clear,f],[clear,d],[on,e,table],[on,d,c],[on,a,b],[on,b,table],[on,c,table],[on,f,e]],
[[clear,c],[clear,f],[clear,d],[on,e,table],[on,d,a],[on,a,b],[on,b,table],[on,c,table],[on,f,e]],
[[clear,e],[clear,f],[clear,d],[on,e,table],[on,d,a],[on,a,b],[on,b,table],[on,c,table],[on,f,c]],
[[clear,e],[clear,f],[clear,c],[on,e,table],[on,d,a],[on,a,b],[on,b,table],[on,c,table],[on,f,d]],
[[clear,e],[clear,f],[on,e,c],[on,d,a],[on,a,b],[on,b,table],[on,c,table],[on,f,d]],
[[clear,d],[clear,f],[on,e,c],[on,d,a],[on,a,b],[on,b,table],[on,c,table],[on,f,e]],
[[clear,d],[clear,a],[on,e,c],[on,d,f],[on,a,b],[on,b,table],[on,c,table],[on,f,e]],
[[clear,b],[clear,a],[on,e,c],[on,d,f],[on,a,d],[on,b,table],[on,c,table],[on,f,e]],
[[clear,d],[clear,b],[clear,a],[on,e,c],[on,d,f],[on,a,table],[on,b,table],[on,c,table],[on,f,e]],
[[clear,d],[clear,f],[clear,a],[on,e,c],[on,d,b],[on,a,table],[on,b,table],[on,c,table],[on,f,e]],
[[clear,d],[clear,f],[clear,b],[on,e,c],[on,d,a],[on,a,table],[on,b,table],[on,c,table],[on,f,e]],
[[clear,d],[clear,f],[clear,e],[on,e,c],[on,d,a],[on,a,table],[on,b,table],[on,c,table],[on,f,b]],
[[clear,c],[clear,f],[clear,e],[on,e,d],[on,d,a],[on,a,table],[on,b,table],[on,c,table],[on,f,b]],
[[clear,b],[clear,f],[clear,e],[on,e,d],[on,d,a],[on,a,table],[on,b,table],[on,c,table],[on,f,c]],
[[clear,b],[clear,f],[clear,c],[on,e,d],[on,d,a],[on,a,table],[on,b,table],[on,c,table],[on,f,e]],
[[clear,f],[clear,c],[on,e,d],[on,d,a],[on,a,table],[on,b,table],[on,c,b],[on,f,e]],
[[clear,f],[clear,e],[on,e,d],[on,d,a],[on,a,table],[on,b,table],[on,c,b],[on,f,c]],
[[clear,c],[clear,f],[clear,e],[on,e,d],[on,d,a],[on,a,table],[on,b,table],[on,c,b],[on,f,table]],
[[clear,c],[clear,b],[clear,e],[on,e,d],[on,d,a],[on,a,table],[on,b,table],[on,c,f],[on,f,table]],
[[clear,c],[clear,b],[clear,f],[on,e,d],[on,d,a],[on,a,table],[on,b,table],[on,c,e],[on,f,table]],
[[clear,c],[clear,f],[on,e,d],[on,d,a],[on,a,table],[on,b,table],[on,c,e],[on,f,b]],
[[clear,c],[clear,e],[on,e,d],[on,d,a],[on,a,table],[on,b,table],[on,c,f],[on,f,b]],
[[clear,d],[clear,e],[on,e,c],[on,d,a],[on,a,table],[on,b,table],[on,c,f],[on,f,b]],
[[clear,c],[clear,d],[clear,e],[on,e,table],[on,d,a],[on,a,table],[on,b,table],[on,c,f],[on,f,b]],
[[clear,a],[clear,d],[clear,e],[on,e,table],[on,d,c],[on,a,table],[on,b,table],[on,c,f],[on,f,b]],
[[clear,a],[clear,e],[on,e,table],[on,d,c],[on,a,d],[on,b,table],[on,c,f],[on,f,b]],
[[clear,a],[clear,d],[on,e,table],[on,d,c],[on,a,e],[on,b,table],[on,c,f],[on,f,b]],
[[clear,c],[clear,d],[on,e,table],[on,d,a],[on,a,e],[on,b,table],[on,c,f],[on,f,b]],
[[clear,c],[clear,f],[on,e,table],[on,d,a],[on,a,e],[on,b,table],[on,c,d],[on,f,b]],
[[clear,d],[clear,c],[clear,f],[on,e,table],[on,d,a],[on,a,e],[on,b,table],[on,c,table],[on,f,b]],
[[clear,d],[clear,a],[clear,f],[on,e,table],[on,d,c],[on,a,e],[on,b,table],[on,c,table],[on,f,b]],
[[clear,d],[clear,a],[clear,c],[on,e,table],[on,d,f],[on,a,e],[on,b,table],[on,c,table],[on,f,b]],
[[clear,e],[clear,a],[clear,c],[on,e,table],[on,d,f],[on,a,d],[on,b,table],[on,c,table],[on,f,b]],
[[clear,e],[clear,a],[clear,d],[on,e,table],[on,d,f],[on,a,c],[on,b,table],[on,c,table],[on,f,b]],
[[clear,f],[clear,a],[clear,d],[on,e,table],[on,d,e],[on,a,c],[on,b,table],[on,c,table],[on,f,b]],
[[clear,f],[clear,e],[clear,d],[on,e,table],[on,d,a],[on,a,c],[on,b,table],[on,c,table],[on,f,b]],
[[clear,f],[clear,b],[clear,d],[on,e,table],[on,d,a],[on,a,c],[on,b,table],[on,c,table],[on,f,e]],
[[clear,f],[clear,b],[clear,e],[on,e,table],[on,d,a],[on,a,c],[on,b,table],[on,c,table],[on,f,d]],
[[clear,f],[clear,b],[on,e,table],[on,d,a],[on,a,c],[on,b,e],[on,c,table],[on,f,d]],
[[clear,f],[clear,d],[on,e,table],[on,d,a],[on,a,c],[on,b,e],[on,c,table],[on,f,b]],
[[clear,b],[clear,f],[clear,d],[on,e,table],[on,d,a],[on,a,c],[on,b,e],[on,c,table],[on,f,table]],
[[clear,b],[clear,e],[clear,d],[on,e,table],[on,d,a],[on,a,c],[on,b,f],[on,c,table],[on,f,table]],
[[clear,a],[clear,e],[clear,d],[on,e,table],[on,d,b],[on,a,c],[on,b,f],[on,c,table],[on,f,table]],
[[clear,a],[clear,c],[clear,d],[on,e,table],[on,d,b],[on,a,e],[on,b,f],[on,c,table],[on,f,table]],
[[clear,a],[clear,c],[clear,e],[on,e,table],[on,d,b],[on,a,d],[on,b,f],[on,c,table],[on,f,table]],
[[clear,d],[clear,a],[clear,c],[clear,e],[on,e,table],[on,d,b],[on,a,table],[on,b,f],[on,c,table],[on,f,table]],
[[clear,d],[clear,c],[clear,e],[on,e,a],[on,d,b],[on,a,table],[on,b,f],[on,c,table],[on,f,table]],
[[clear,a],[clear,c],[clear,e],[on,e,d],[on,d,b],[on,a,table],[on,b,f],[on,c,table],[on,f,table]],
[[clear,a],[clear,d],[clear,e],[on,e,c],[on,d,b],[on,a,table],[on,b,f],[on,c,table],[on,f,table]],
[[clear,a],[clear,d],[clear,b],[on,e,c],[on,d,e],[on,a,table],[on,b,f],[on,c,table],[on,f,table]],
[[clear,f],[clear,d],[clear,b],[on,e,c],[on,d,e],[on,a,table],[on,b,a],[on,c,table],[on,f,table]],
[[clear,f],[clear,a],[clear,b],[on,e,c],[on,d,e],[on,a,table],[on,b,d],[on,c,table],[on,f,table]],
[[clear,f],[clear,a],[on,e,c],[on,d,e],[on,a,b],[on,b,d],[on,c,table],[on,f,table]],
[[clear,b],[clear,a],[on,e,c],[on,d,e],[on,a,f],[on,b,d],[on,c,table],[on,f,table]],
[[clear,b],[clear,d],[on,e,c],[on,d,e],[on,a,f],[on,b,a],[on,c,table],[on,f,table]],
[[clear,a],[clear,b],[clear,d],[on,e,c],[on,d,e],[on,a,f],[on,b,table],[on,c,table],[on,f,table]],
[[clear,e],[clear,b],[clear,d],[on,e,c],[on,d,a],[on,a,f],[on,b,table],[on,c,table],[on,f,table]],
[[clear,e],[clear,c],[clear,d],[on,e,b],[on,d,a],[on,a,f],[on,b,table],[on,c,table],[on,f,table]],
[[clear,e],[clear,c],[clear,b],[on,e,d],[on,d,a],[on,a,f],[on,b,table],[on,c,table],[on,f,table]],
[[clear,e],[clear,b],[on,e,d],[on,d,a],[on,a,f],[on,b,c],[on,c,table],[on,f,table]],
[[clear,e],[clear,d],[on,e,b],[on,d,a],[on,a,f],[on,b,c],[on,c,table],[on,f,table]],
[[clear,a],[clear,d],[on,e,b],[on,d,e],[on,a,f],[on,b,c],[on,c,table],[on,f,table]],
[[clear,a],[clear,f],[on,e,b],[on,d,e],[on,a,d],[on,b,c],[on,c,table],[on,f,table]],
[[clear,d],[clear,a],[clear,f],[on,e,b],[on,d,e],[on,a,table],[on,b,c],[on,c,table],[on,f,table]],
[[clear,d],[clear,a],[clear,e],[on,e,b],[on,d,f],[on,a,table],[on,b,c],[on,c,table],[on,f,table]],
[[clear,a],[clear,e],[on,e,b],[on,d,f],[on,a,d],[on,b,c],[on,c,table],[on,f,table]],
[[clear,b],[clear,e],[on,e,a],[on,d,f],[on,a,d],[on,b,c],[on,c,table],[on,f,table]],
[[clear,b],[clear,c],[on,e,a],[on,d,f],[on,a,d],[on,b,e],[on,c,table],[on,f,table]],
[[clear,e],[clear,b],[clear,c],[on,e,a],[on,d,f],[on,a,d],[on,b,table],[on,c,table],[on,f,table]],
[[clear,e],[clear,a],[clear,c],[on,e,b],[on,d,f],[on,a,d],[on,b,table],[on,c,table],[on,f,table]],
[[clear,e],[clear,a],[clear,d],[on,e,b],[on,d,f],[on,a,c],[on,b,table],[on,c,table],[on,f,table]],
[[clear,e],[clear,b],[clear,d],[on,e,a],[on,d,f],[on,a,c],[on,b,table],[on,c,table],[on,f,table]],
[[clear,e],[clear,b],[clear,a],[on,e,d],[on,d,f],[on,a,c],[on,b,table],[on,c,table],[on,f,table]],
[[clear,c],[clear,b],[clear,a],[on,e,d],[on,d,f],[on,a,e],[on,b,table],[on,c,table],[on,f,table]],
[[clear,c],[clear,b],[on,e,d],[on,d,f],[on,a,e],[on,b,a],[on,c,table],[on,f,table]],
[[clear,a],[clear,b],[on,e,d],[on,d,f],[on,a,e],[on,b,c],[on,c,table],[on,f,table]],
[[clear,a],[clear,e],[on,e,d],[on,d,f],[on,a,b],[on,b,c],[on,c,table],[on,f,table]],
[[clear,d],[clear,e],[on,e,a],[on,d,f],[on,a,b],[on,b,c],[on,c,table],[on,f,table]],]


def blockspace(tblocks, onblocks, n):
    space = [[0 for _ in range(n)] for _ in range(n)]
    for x in tblocks:
        idx = space[n-1].index(0)
        space[n-1][idx] = x

    for on in onblocks:
        if on[1] not in tblocks:
            onblocks.remove(on)
            onblocks.append(on)
 
    for on in onblocks:
        for i in range(n-1,-1,-1):
            if on[1] in space[i]:
                space[i-1][space[i].index(on[1])] = on[0]
    return space


def print_steps(arr):
    n = len(arr[0])
    num_arrays = len(arr)

    for start_index in range(0, num_arrays, 5):  # 5 states at once / per line
        end_index = min(start_index + 5, num_arrays)
        current_arrays = arr[start_index:end_index]

        # print header for current chunk
        header = "\t".join(f"state[{i}]" for i in range(start_index, end_index))
        print(header)

        for row_index in range(n):  # go thru rows
            row_line = ""
            for array in current_arrays:
                row = array[row_index]
                s = " ".join(map(str, row)) + "\t|\t"
                row_line += s.replace('0'," ")
            print(row_line)
        print()

def print_steps2(arr):
    n = len(arr[0])
    num_arrays = len(arr)

    for start_index in range(0, num_arrays, 5):  # 5 states at once / per line
        end_index = min(start_index + 5, num_arrays)
        current_arrays = arr[start_index:end_index]

        # print header for current chunk
        header = "\t".join(f"state[{i}]" for i in range(start_index, end_index))
        print(header)

        for row_index in range(n):  # go thru rows
            row_line = ""
            for array in current_arrays:
                row = array[row_index]
                s = " ".join(map(str, row)) + "\t\t"
                row_line += s.replace('0',"🅉")
            print(row_line)
        print()

def print_steps3(arr):
    for i in range(len(arr)):
        state = arr[i]
        print(f"\nstate[{i}]")
        for row in state:
            s = " ".join(map(str, row))
            print(s.replace('0',"🅉"))

def blocksWorldPath(path, n):
    steps = []
    for state in path:
        table_blocks = []
        on_blocks = []

        for x in state:
            if table in x:
                table_blocks.append(x[1])
            elif clear not in x:
                on_blocks.append([x[1], x[2]])
        
        steps.append(blockspace(table_blocks, on_blocks, n))
    print_steps2(steps)


blocksWorldPath(path, n)


