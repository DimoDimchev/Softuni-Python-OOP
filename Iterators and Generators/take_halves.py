def solution():
    def integers():
        integer = 0
        while True:
            integer += 1
            yield integer

    def halves():
        for i in integers():
            half = i / 2
            yield half

    def take(n, seq):
        halves_list = []
        for i in seq:
            if len(halves_list) == n:
                return halves_list
            halves_list.append(i)


    return (take, halves, integers)


# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))