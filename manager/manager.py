class Manager:
    def __init__(self, s:float, extra: float):
        self.s = s
        self.extra = extra * self.s

    def salary(self, days):
        return (self.s + self.extra) * days * 8

    def tax(self, days):
        return (8 * int(days)) * (self.s * 0.13 + self.extra)


def main():
    s = float(input())
    e = float(input())

    a = Manager(s , e)
    print(a.salary(10))
    print(a.tax(10))

if __name__ == '__main__':
    main()