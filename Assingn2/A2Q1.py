import math

def add_vectors(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

def subtract_vectors(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]

def multiply_vector(v, scalar):
    return [scalar * v[i] for i in range(len(v))]

def dot_product(v1, v2):
    return sum([v1[i] * v2[i] for i in range(len(v1))])

def vector_length(v):
    return math.sqrt(sum([v[i] ** 2 for i in range(len(v))]))

def main():
    while True:
        print("\n1. Add vectors")
        print("2. Subtract vectors")
        print("3. Multiply vector by scalar")
        print("4. Calculate dot product")
        print("5. Calculate vector length")
        print("6. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            v1 = [int(x) for x in input("Enter first vector: ").split()]
            v2 = [int(x) for x in input("Enter second vector: ").split()]
            assert len(v1) == len(v2) , "length of two vectors must be same"
            print("Result: ", add_vectors(v1, v2))
        elif choice == 2:
            v1 = [int(x) for x in input("Enter first vector: ").split()]
            v2 = [int(x) for x in input("Enter second vector: ").split()]
            assert len(v1)== len(v2) , "length of two vectors must be same"
            print("Result: ", subtract_vectors(v1, v2))
        elif choice == 3:
            v = [int(x) for x in input("Enter vector: ").split()]
            scalar = int(input("Enter scalar: "))
            print("Result: ", multiply_vector(v, scalar))
        elif choice == 4:
            v1 = [int(x) for x in input("Enter first vector: ").split()]
            v2 = [int(x) for x in input("Enter second vector: ").split()]
            assert len(v1)== len(v2) , "length of two vectors must be same"
            print("Result: ", dot_product(v1, v2))
        elif choice == 5:
            v = [int(x) for x in input("Enter vector: ").split()]
            print("Result: ", vector_length(v))
        elif choice == 6:
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
