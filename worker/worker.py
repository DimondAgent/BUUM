class Worker:
    def __init__(self, s):
        self.s = s


    def salary(self, days):
        return (self.s * 8) * days


    def tax(self, days):
        return ((self.s * 8) * days)* 0.13


def main():
    s = int(input())

    a = Worker(s)
    print(a.salary(10))
    print(a.tax(10))


if __name__ == '__main__':
    main()
