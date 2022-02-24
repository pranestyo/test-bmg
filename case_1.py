
def get_value(n):
    temp_value = []
    count = 1
    for i in range(n):
        to_teks = str(count)
        if count % 3 == 0 and count % 5 == 0:
            to_teks = 'Frontend Backend'
        elif count % 3 == 0:
            to_teks = 'Frontend'
        elif count % 5 == 0:
            to_teks = 'Backend'
        else:
            to_teks = to_teks

        count += 1
        temp_value.append(to_teks)

    print(str(temp_value).replace('[', '').replace(']', ''))


if __name__ == '__main__':
    print('Please input value:')
    n = input()
    get_value(int(n))
