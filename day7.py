from collections import namedtuple

FsNode = namedtuple('FsNode', 'name size children parent')


def dir_sizes(root: FsNode) -> list[int]:
    global dir_sizes
    dir_sizes = []

    def dir_size(root: FsNode) -> int:
        global dir_sizes
        if not root.children:
            return root.size

        size = 0
        for child in root.children:
            size += dir_size(child)

        dir_sizes.append(size)

        return size

    dir_size(root)
    return dir_sizes


with open("data/day7.txt", "r") as infile:
    root = None
    curr_root = root
    while infile.readable():
        line = infile.readline()
        if not line:
            break
        if line.startswith('$ cd'):
            dirname = line.removeprefix('$ cd').strip()
            if dirname == '/':
                root = FsNode(name=dirname, size=0, children=[], parent=None)
                curr_root = root
            elif dirname == '..':
                curr_root = curr_root.parent
            else:
                for child in curr_root.children:
                    if child.name == dirname:
                        curr_root = child
        elif line.startswith('$ ls'):
            ls_output = []
            while infile.readable():
                filpos = infile.tell()
                curr_line = infile.readline()
                if curr_line.startswith('$'):
                    infile.seek(filpos)
                    break
                elif curr_line.startswith('dir'):
                    curr_dirname = curr_line.split()[1]
                    ls_output.append(FsNode(name=curr_dirname, size=0, children=[], parent=curr_root))
                else:
                    if not curr_line.split():
                        break
                    [size, name] = curr_line.split()
                    ls_output.append(FsNode(name=name, size=int(size), children=None, parent=curr_root))
                filpos = None
            curr_root.children.extend(ls_output)

    dir_sizes = dir_sizes(root)
    # Part 1
    print(sum(filter(lambda x: x < 100000, dir_sizes)))
    # Part 2
    max_space = 70000000
    expected_avail_space = 30000000
    curr_filled_space = max(dir_sizes)
    curr_avail_space = max_space - curr_filled_space
    for dir_size in sorted(dir_sizes):
        if curr_avail_space + dir_size > expected_avail_space:
            print(dir_size)
            break
