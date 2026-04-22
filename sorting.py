import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(sekvence):
    sekvence = sekvence[:]
    n = len(sekvence)
    for i in range(n):
        index_nejmensi = i
        for j in range(i + 1, n):
            if sekvence[j] < sekvence[index_nejmensi]:
                index_nejmensi = j
        sekvence[i], sekvence[index_nejmensi] = sekvence[index_nejmensi], sekvence[i]
    return sekvence




    return  sekvence


def main():
    sekvence = random_numbers(count = 20, low = 0, high=100)
    sorted_sekvence = selection_sort(sekvence)
    print(sorted_sekvence)
if __name__ == "__main__":
    main()
