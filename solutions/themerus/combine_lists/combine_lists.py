from unittest import result


def combine_lists(list1, list2):
    lists_combined = []
    i = 0
    while i < len(list1) and i < len(list2):
        lists_combined.append(list1[i])
        lists_combined.append(list2[i])
        i += 1

    if len(list1) > len(list2):
        for x in range(len(list2), len(list1)):
            lists_combined.append(list1[x])
        return lists_combined

    elif len(list1) < len(list2):
        for x in range(len(list1), len(list2)):
            lists_combined.append(list2[x])
        return lists_combined
    else:
        return lists_combined
