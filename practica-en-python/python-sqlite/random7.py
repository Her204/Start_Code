  
# In this problem, we want to determine all possible combinations of k 
# numbers out of 1 ... n. We use backtracking to solve this problem.
# Time complexity: O(C(n,k)) which is O(n choose k) = O((n!/(k! * (n - k)!)))



def generate_all_combinations(n: int, k: int) -> [[int]]:
    """
    >>> generate_all_combinations(n=10, k=12)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """

    result = []
    create_all_state(1, n, k, [], result)
    return result


def create_all_state(increment, total_number, level, current_list, total_list):
    if level == 0:
        total_list.append(current_list[:])
        return

    for i in range(increment, total_number - level + 2):
        current_list.append(i)
        create_all_state(i + 1, total_number, level - 1, current_list, total_list)
        current_list.pop()


def print_all_state(total_list):
    a = 0
    for i in total_list:
        print(*i)
        a += 1
    print("The number of combinations are: ", a)


if __name__ == "__main__":
    n = int(input("Select a number: "))
    k = int(input("Select a number of boxes: "))
    total_list = generate_all_combinations(n, k)
    print_all_state(total_list)
