# basically sorting all elements of a list in increasing order

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor

def get_median(elements):
    if len(elements) % 2 == 0:
        insertion_sort(elements)
        print('sorted list is:', elements)
        median_index = len(elements) // 2
        #median_index2 = median_index1 - 1
        median = (elements[median_index] + elements[median_index - 1]) / 2

    else:
        insertion_sort(elements)
        median_index = len(elements) // 2
        print(elements)
        median = elements[median_index]
    return median




if __name__ == '__main__':
    elements = [21,36,14,19,26,32,11,24,30,20]
    #insertion_sort(elements)
    print(elements)
    print(get_median(elements))
    # passing an array of list
    # test_list = [
    #     [11,22,10,19,15],
    #     [],
    #     [6],
    #     [25, 22, 21, 10],
    # ]
    # for i in test_list:
    #     insertion_sort(i)
    #     print(i)
