class Element:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Hago mi ej favorito de toda la materia, por backtracking, the fucking knapsack problem (problema de la mochila para los que no hablan frances)

def weight_is_passed(current_solution, w):
    return sum(e.weight for e in current_solution) > w


def is_best_solution(current_solution, best_solution):
    return sum(e.value for e in current_solution) > sum(e.value for e in best_solution)

def trivial_solution(elements, w):
    for e in elements:
        if e.weight < w:
            return [e]
    return []

def knapsack_bt(elements, w):
    current_solution, best_solution = [], trivial_solution(elements, w)

    if best_solution == []:
        return "All weights of the elements are greater than the capacity of the back"

    def backtrack(elements, actual, w, current_solution):
        nonlocal best_solution

        if weight_is_passed(current_solution, w):
            return

        if is_best_solution(current_solution, best_solution):
            best_solution = current_solution[:]

        for i in range(actual, len(elements)):
            current_solution.append(elements[i])
            backtrack(elements, i + 1, w, current_solution)
            current_solution.pop()

    backtrack(elements, 0, w, current_solution)
    return best_solution


# knapsack_bt([Element(5, 10), Element(5, 50), Element(10, 40)], 10)