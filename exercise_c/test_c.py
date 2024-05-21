def generate_Fibonanacci_sequence(initial_term,second_term, num):
    if num < 2:
        return [initial_term]
    else:    
        x = [initial_term, second_term]
        for i in range(num-2):
            initial_term, second_term = second_term, initial_term + second_term
            x.append(second_term)
    return x

if __name__ == '__main__':
    result = generate_Fibonanacci_sequence(initial_term=1,second_term=1, num=1)   
    print(result)
