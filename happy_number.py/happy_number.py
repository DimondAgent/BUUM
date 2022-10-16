def happy_number(a):
    a = [int(i) for i in input()]
    if sum(a[:3]) == sum(a[3:]):
        print('lucky ')
    else:
        print('unlucky')


def main():
    a = int

    return happy_number(a)


if __name__ == '__main__':
    main()
