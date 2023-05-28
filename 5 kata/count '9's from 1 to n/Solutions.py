def count_nines(n):
    counter = len(str(n))-1
    nine_counter = 0
    if n % 10 == 9:
        nine_counter += 1
    for i in range(counter):
        first_num = n//10**counter
        nine_counter += counter*first_num*(10**(counter-1))
        if first_num == 9:
            nine_counter += n % 10**counter
            nine_counter += 1
        n %= 10**counter
        counter -= 1

    return nine_counter
