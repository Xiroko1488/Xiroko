def raise_to_the_deg(numder, max_degree):
    i = 0
    for _ in range(max_degree):
        yield numder**i
        i += 1


res = raise_to_the_deg(122345, 500)
print(res)
for _ in res:
    print(_)

