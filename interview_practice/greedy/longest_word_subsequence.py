import collections

def solution(S, D):
    letter_positions = collections.defaultdict(list)

    for index, letter in enumerate(letters):
        letter_positions[letter].append(index)

    for word in sorted(words, key=lambda w: len(w), reverse=True):
        pos = 0
        for letter in word:
            if letter not in letter_positions:
                break

        possible_positions = [p for p in letter_positions[letter] if p >= pos]
        if not possible_positions:
            break
        pos = possible_positions[0] + 1
        else:
            return word


