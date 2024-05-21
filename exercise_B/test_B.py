import argparse


def generate_geometric_progression(initial_term, common_ratio, num):
    ans = []
    for i in range(num):
        ans.append(initial_term * common_ratio ** i)
    return ans


def calculate_arithmetic_series(initial_term, common_ratio, num):
    t = sum(generate_geometric_progression(initial_term, common_ratio, num))
    return t


def argument_parser():
    parser = argparse.ArgumentParser(
        description='Geometric series')
    parser.add_argument(
        '-it', '--initial_term',
        dest='it',
        help='initial term : default 2',
        type=str, default='2')
    parser.add_argument(
        '-cr', '--common_ratio',
        dest='cr',
        help='common ratio : default 2',
        type=str, default='2')
    parser.add_argument(
        '-num', '--number_of_terms',
        dest='num',
        help='number or terms : default 5',
        type=str, default='5')
    return parser.parse_args()


def main():
    args = argument_parser()
    initial_term = float(args.it)
    common_ratio = float(args.cr)
    num = int(args.num)
    geometric_progression = generate_geometric_progression(
        initial_term=initial_term,
        common_ratio=common_ratio,
        num=num)
    arith_sum = calculate_arithmetic_series(
        initial_term=initial_term,
        common_ratio=common_ratio,
        num=num)
    print(f'geometric progression:\n{geometric_progression}\n')
    print(f'arithmetric sum:\n{arith_sum}')


if __name__ == '__main__':
    main()
