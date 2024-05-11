def raise_to_the_deg(numder, max_degree):
    i = 0
    while True:
        yield numder**i
        i += 1


res = raise_to_the_deg(12)
print(res)
for _ in res:
    print(_)

