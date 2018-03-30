

def dot_product_lite(a, b):
    sum = 0
    for a_num, b_num in zip(a, b):
        sum = sum + a_num * b_num
    return sum


def compress_sparse_matrix(a):
    index = 0
    output = []
    while index < len(a):
        if a[index] != 0:
            output.append(str(a[index]))
            index += 1
            continue

        count = 0
        while index < len(a) and a[index] == 0:
            index += 1
            count += 1
        output.append("0" + str(count))

    return output


def sparse_dot_product(a, b):
    index_a = 0
    index_b = 0
    virtual_index_a = 0
    virtual_index_b = 0
    total = 0
    while index_a < len(a) and index_b < len(b):
        while index_a < len(a) and a[index_a].startswith("0"):
            virtual_index_a += int(a[index_a][1:])
            index_a += 1
        while index_b < len(a) and a[index_b].startswith("0"):
            virtual_index_b += int(b[index_b][1:])
            index_b += 1

        if index_a == len(a) or index_b == len(b):
            return total

        if virtual_index_a < virtual_index_b:
            index_a += 1
            virtual_index_a += 1
        elif virtual_index_a > virtual_index_b:
            index_b += 1
            virtual_index_b += 1
        else:
            product = float(a[index_a]) * float(b[index_b])
            total += total + product
            index_a += 1
            index_b += 1
            virtual_index_a += 1
            virtual_index_b += 1

    return product


def dot_product(a, b):
    compressed_a = compress_sparse_matrix(a)
    compressed_b = compress_sparse_matrix(b)

    product = sparse_dot_product(compressed_a, compressed_b)

    return product
