def euler_9():
    squares = {x ** 2 for x in range(1,1000+1)}
    for a in range(1,1001):
        for b in range(1,1001):
            if a**2 + b**2 in squares:
                c = int((a**2+b**2) ** (1/2))

                
                if a+b+c == 1000:
                    print(f"a,b: {a,b}, {c}: {a**2+b**2}")
                    print(a*b*c)
                    break