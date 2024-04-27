class Number(Exception):
    def __str__(self):
        return f"you didn`t entered 5 nubers"


def check_num(num):
    if num == 13:
        raise Number
    else:
        return  num


for i in range(5):
    print(check_num(int(input(f"Enter Number{i+1}:"))))