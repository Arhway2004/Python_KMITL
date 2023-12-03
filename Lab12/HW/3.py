from itertools import product as cartesian_product

def product(*sets):
    # Check if there are no sets provided
    if not sets:
        return {()}  # Return an empty set for the base case

    # Use the Cartesian product function from itertools to combine the sets
    product_result = set(cartesian_product(*sets))

    return product_result

# Example usage:
s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

result = product(s1, s2)
print(result)

result = product(s1, s2, s3)
print(result)

result = product(s1)
print(result)
