def generate_Fibonanacci_sequence(initial_term,second_term, num):
    if num < 2:
        return [initial_term]
    else:    
        x = [initial_term, second_term]
        for i in range(num-2):
            initial_term, second_term = second_term, initial_term + second_term
            x.append(second_term)
    return x


def calculate_Fibonacci_ratio(initial_term, second_term, num):
    if num < 2:
        print('number of terms < 2... Return 0')
        return 0
    seq = generate_Fibonanacci_sequence(initial_term,second_term, num)
    ratio = seq[num-1] / seq[num-2]
    return ratio


if __name__ == '__main__':
    ratio = calculate_Fibonacci_ratio(
        initial_term=1,
        second_term=1,
        num=10)   
    print(ratio)
