import argparse

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

def argument_parser():
    parser = argparse.ArgumentParser(description="Fibo")
    parser.add_argument(
        '-i', '--ini', dest='ini', type=float,
        help='initial_term', required=True)
    parser.add_argument(
        '-s', '--sec', dest='sec', type=float,
        help='second_term', required=True)
    parser.add_argument(
        '-n', '--num', dest='num', type=int,
        help='number_of_terms', required=True)
    return parser.parse_args()


def main():
    args = argument_parser()
    initial_term = args.ini
    second_term = args.sec
    num = args.num
    generate_fibo = generate_Fibonanacci_sequence(
        initial_term = initial_term,
        second_term = second_term,
        num = num)
    calcurate_fibo = calculate_Fibonacci_ratio(
        initial_term = initial_term,
        second_term = second_term,
        num = num)
    print(f'fibonacci progression:\n{generate_fibo}\n')
    print(f'fibonacci ratio:\n{calcurate_fibo}\n')


if __name__ == '__main__':
    main()
