from random import randint


def half_search(temp_list, val):
    begin = 0
    end = len(temp_list) - 1
    while begin <= end:
        mid = (begin + end) // 2
        mid_num = temp_list[mid]
        if val > mid_num:
            begin = mid + 1
        elif val < mid_num:
            end = mid -1
        else:
            return mid
    return -1

def main():
    list1 = [randint(1, 100) for _ in range(100)]
    list1.sort()
    print(list1)
    result = half_search(list1, 50)
    print(result)

if __name__ == '__main__':
    main()