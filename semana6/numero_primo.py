def primo(num):
    i = 2
    while i < num:
        if num % i == 0:
            break
        i += 1
    return i == num


print(primo(6))
print(primo(7))
print(primo(13))
