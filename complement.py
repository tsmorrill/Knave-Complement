FIRST_TERM = [1]
ITERATIONS = 15


def complement(n):
    return 9 - n


def knave(term):
    if len(term) == 0:
        return [0]
    
    next_term = []
    current_digit = term[0]
    count = 0 
    while len(term) > 0:
        if term[0] == current_digit:
            term.pop(0)
            count += 1
        else:
            next_term.append(count)
            next_term.append(complement(current_digit))
            current_digit = term[0]
            count = 0 
    next_term.append(count)
    next_term.append(complement(current_digit))
    return next_term


def read(term):
    print_string = "".join(str(digit) for digit in term)
    print(print_string)


def main():
    read(FIRST_TERM)
    current_term = FIRST_TERM
    for _ in range(ITERATIONS):
        current_term = knave(current_term)
        read(current_term)
        
            
if __name__ == "__main__":
	main()
