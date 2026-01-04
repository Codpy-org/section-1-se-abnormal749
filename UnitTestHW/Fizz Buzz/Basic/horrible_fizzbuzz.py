def fizzBuzz(n: int) -> str:
    if n%15==0:
        return "Fizz" + "Buzz"
    if n%3==0:
        return "Fizz"
    if n%5==0:
        return "Buzz"
    elif n%1==0:
        return f"{str(n)}"
    return "OwO"
