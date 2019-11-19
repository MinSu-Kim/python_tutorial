import random as rnd


def random_number():
    return rnd.randint(1, 46)


def bubble_sort(generate_list):
    for cnt in range(len(generate_list)):
        for i in range(len(generate_list) - 1):
            if generate_list[i] > generate_list[i + 1]:
                # generate_list[i], generate_list[i + 1] = generate_list[i + 1], generate_list[i]
                a = generate_list[i]
                generate_list[i] = generate_list[i+1]
                generate_list[i+1] = a
    return generate_list


def binary_search(sorted_list, search_key):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if search_key == sorted_list[mid]:
            return mid
        elif search_key > sorted_list[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return None


if __name__ == "__main__":
    random_list = []
    rnd.seed(1)
    for num in range(0, 10):
        random_list.append(random_number())

    print(random_list)

    sorted_list = bubble_sort(random_list)
    print(sorted_list)

    search_key = 5
    find_index = binary_search(sorted_list, search_key)
    print('key {} 는 {}'.format(search_key, str(find_index) + '번째 존재' if find_index != None else 'not found'))
