

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
path = [[[on,a,c],[on,b,table],[on,c,b],[clear,d],[on,d,a]],
[[clear,a],[on,a,c],[on,b,table],[on,c,b],[clear,d],[on,d,table]],
[[clear,a],[on,a,d],[on,b,table],[on,c,b],[clear,c],[on,d,table]],
[[clear,b],[on,a,d],[on,b,table],[on,c,a],[clear,c],[on,d,table]],
[[clear,a],[clear,b],[on,a,d],[on,b,table],[on,c,table],[clear,c],[on,d,table]],
[[clear,a],[clear,d],[on,a,b],[on,b,table],[on,c,table],[clear,c],[on,d,table]],
[[clear,a],[clear,d],[on,a,c],[on,b,table],[on,c,table],[clear,b],[on,d,table]],
[[clear,c],[clear,a],[clear,d],[on,a,table],[on,b,table],[on,c,table],[clear,b],[on,d,table]],
[[clear,c],[clear,d],[on,a,table],[on,b,table],[on,c,a],[clear,b],[on,d,table]],
[[clear,c],[clear,a],[on,a,table],[on,b,table],[on,c,d],[clear,b],[on,d,table]],
[[clear,c],[clear,a],[on,a,table],[on,b,table],[on,c,b],[clear,d],[on,d,table]],
[[clear,c],[on,a,table],[on,b,table],[on,c,b],[clear,d],[on,d,a]],
[[clear,c],[on,a,table],[on,b,table],[on,c,d],[clear,b],[on,d,a]],
[[clear,d],[clear,c],[on,a,table],[on,b,table],[on,c,table],[clear,b],[on,d,a]],
[[clear,d],[clear,a],[on,a,table],[on,b,table],[on,c,table],[clear,b],[on,d,c]],
[[clear,d],[on,a,table],[on,b,a],[on,c,table],[clear,b],[on,d,c]],
[[clear,d],[on,a,table],[on,b,a],[on,c,table],[clear,c],[on,d,b]],
[[clear,b],[clear,d],[on,a,table],[on,b,a],[on,c,table],[clear,c],[on,d,table]],
[[clear,b],[clear,a],[on,a,table],[on,b,d],[on,c,table],[clear,c],[on,d,table]],
[[clear,b],[clear,a],[on,a,table],[on,b,c],[on,c,table],[clear,d],[on,d,table]],]


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
    print(len(path))


blocksWorldPath(path, n)


