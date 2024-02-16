def meow(n: int) -> str:
    #for _ in range(n):
    return "meow\n" * n


number: int = int(input("Number : "))
meows: str = meow(number)
print(meows, end="")