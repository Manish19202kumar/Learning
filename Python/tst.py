def sum_of_divisors(n):
    divisors = [1]  # Start with 1 as a divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.extend([i, n // i])
    return sum(set(divisors))  # Use a set to eliminate duplicates
 
def find_amicable_numbers(start, end):
    amicable_pairs = []
    for num in range(start, end + 1):
        partner = sum_of_divisors(num)
        if num != partner and sum_of_divisors(partner) == num:
            amicable_pairs.append((num, partner))
    return amicable_pairs
 
start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))
 
amicable_numbers = find_amicable_numbers(start_range, end_range)
if amicable_numbers:
    print("Amicable Pairs:")
    for pair in amicable_numbers:
        print(pair[0], "-", pair[1])
else:
    print("No amicable numbers found in the specified range.")