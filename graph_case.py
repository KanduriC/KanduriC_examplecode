# See exdata1.txt for how the data looks. Provided is a list of IDs. Some have a reference to their immediate parent. Some parents have their own parents.
# This program produces a list with child and ultimate parents, in other words all nodes and their oldest ancestors, if any.

def _readGraphFile(graphFn):
    with(open(graphFn)) as gdata:
        graphdata = gdata.readlines()
    return graphdata

def _getNodes(graphdata):
    nodes = [graph_line.strip("\n").split("\t")[0] for graph_line in graphdata]
    return nodes

def _getParentNodes(graphdata):
    parentnodes = [graph_line.strip("\n").split("\t")[1] for graph_line in graphdata]
    return parentnodes

def _getParents(nodes,parentnodes):
    relations = dict(zip(nodes,parentnodes))
    return relations

def _returnParent(relations,node,parentnode):
    orig_key = node
    orig_value = parentnode
    if node == parentnode:
        pass
    else:
        previous_keys = [orig_key]
        while orig_value in relations.keys():
            previous_keys.append(orig_value)
            if relations[orig_value] in previous_keys:
                orig_value = relations[orig_value]
                break
            else:
                orig_value = relations[orig_value]
        previous_keys = []
    return orig_value

def _reassignParent(relations):
    for key, value in relations.items():
        relations[key] = _returnParent(relations,node=key, parentnode=value)
    return relations

def getAncestors(graphFn):
    gdat = _readGraphFile(graphFn)
    gnodes = _getNodes(graphdata=gdat)
    gparents = _getParentNodes(graphdata=gdat)
    grelations = _getParents(nodes=gnodes,parentnodes=gparents)
    gancestors = _reassignParent(grelations)
    return gancestors


if __name__ == "__main__":
    import time
    start_time = time.time()
    ex1 = getAncestors(graphFn="exdata1.txt")
    print ex1
    # print("example data_1: --- %s seconds ---" % (time.time() - start_time))
    # getAncestors(graphFn="exdata2.txt")
    # print("example data_2: --- %s seconds ---" % (time.time() - start_time))
    # getAncestors(graphFn="exdata3.txt")
    # print("example data_3: --- %s seconds ---" % (time.time() - start_time))