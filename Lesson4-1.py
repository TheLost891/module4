

"""def strcounter(s):   # O(n*n) O(N**2) = O(20)
    for el in set(s):
        counter = 0
        for sub_el in s:
            if sub_el == el:
                counter += 1
        print(el, counter)


strcounter('abbcd')"""


def strcounter(s):  # O(M+N) = O(9)
    el_counter = {}
    for el in s:
        el_counter[el] = el_counter.get(el, 0) + 1  # 5 operations
    for el, count in el_counter.items():  # 4 operations
        print(el, count)


strcounter('abbcd')
