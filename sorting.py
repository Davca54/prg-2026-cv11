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


def bubble_sort(sekvence):
    sekvence = sekvence[:]
    n = len(sekvence)
    for it in range(n - 1):
        for idx in range(n - 1 - it):
            if sekvence[idx] > sekvence[idx + 1]:
                sekvence[idx], sekvence[idx + 1] = sekvence[idx + 1], sekvence[idx]
    return sekvence




def main():
    sekvence = random_numbers(count = 20, low = 0, high=100)
    sorted_sekvence_selection = selection_sort(sekvence)
    bubble_sorted = bubble_sort(sekvence)
    print(sorted_sekvence_selection)
    print(bubble_sorted)
if __name__ == "__main__":
    main()
