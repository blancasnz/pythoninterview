
def reconstruct_queue(people):
    """
    Input:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    Output:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    """
    sorted_people = sorted(people, key=lambda (h, k): (-h, k))
    q = []
    for person in sorted_people:
        q.insert(person[1], person)
    return q
