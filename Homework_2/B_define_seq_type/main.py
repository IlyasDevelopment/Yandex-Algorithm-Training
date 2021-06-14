def define_sequence_type(sequence):
    asc = True
    const = True
    desc = True
    weak = False
    previous_element = sequence[0]
    for element in sequence[1:]:
        const &= element == previous_element
        weak |= element == previous_element
        asc &= element >= previous_element
        desc &= element <= previous_element
        previous_element = element
    if const:
        return 'CONSTANT'
    elif asc:
        return 'WEAKLY ASCENDING' if weak else 'ASCENDING'
    elif desc:
        return 'WEAKLY DESCENDING' if weak else 'DESCENDING'
    else:
        return 'RANDOM'


numbers = []
while True:
    number = int(input())
    if number != -2000000000:
        numbers.append(number)
    else:
        break
print(define_sequence_type(numbers))
