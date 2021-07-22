def make_tree(serialized):
    tree = {'left': None, 'right': None, 'up': None, 'type': 'root'}
    now_node = tree
    for sym in serialized:
        if sym == 'D':
            new_node = {'left': None, 'right': None, 'up': now_node, 'type': 'left'}
            now_node['left'] = new_node
            now_node = new_node
        elif sym == 'U':
            while now_node['type'] == 'right':
                now_node = now_node['up']
            now_node = now_node['up']
            new_node = {'left': None, 'right': None, 'up': now_node, 'type': 'right'}
            now_node['right'] = new_node
            now_node = new_node
    return tree


def traverse(root, prefix):
    if root['left'] is None and root['right'] is None:
        return [''.join(prefix)]
    prefix.append('0')
    ans = traverse(root['left'], prefix)
    prefix.pop()
    prefix.append('1')

    ans.extend(traverse(root['right'], prefix))
    prefix.pop()
    return ans


tree = make_tree('DDUUDU')
print(traverse(tree, []))
