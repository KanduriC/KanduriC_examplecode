# method that sums up all integers in any array; basically involves flattening a nested list

def _flattenNestedList(inputlist):
    for item in inputlist:
        if not isinstance(item,(list,tuple)):
            yield item
        else:
            for subitem in _flattenNestedList(item):
                yield subitem

def _extractIntList(list):
    integer_list = [item for item in list if isinstance(item, (int,long))]
    return integer_list

if __name__ == "__main__":
    test_list = ['1', 3, ['the'], 'quick', [3, [['lazy'], [4, [-6]]]], 'fox', [1, '%'], '-5', [-5]]
    flatlist = _flattenNestedList(test_list)
    flatted_list = list(flatlist)
    print "flat list:", flatted_list
    integerlist = _extractIntList(flatted_list)
    print "integer list:", integerlist
    print "sum of integer list:", sum(integerlist)