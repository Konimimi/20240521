def generate_geometric_progression(initial_term,common_ratio,num):
    ans = []
    for i in range(num):
        ans.append(initial_term * common_ratio ** i)
    return ans

if __name__ == '__main__':
    result = generate_geometric_progression(initial_term = 2,common_ratio = 3,num = 10)
    print(result)
