def sorting(value):
    for i in range(len(value)):
        for j in range(len(value)):
            if value[i] < value[j]:                      # check if the j value is greater than i value
                value[i], value[j] = value[j], value[i]  # if condition get true swapping the values
    return value


sort_list = [34, 12, 78, 455, 29, 23, 22]
print(f"sorted List:{sorting(sort_list)}")

