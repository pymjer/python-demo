import string


def Shift_Encrypt(puzzle, shift):
    shift_map = str.maketrans(string.ascii_letters, string.ascii_letters[
        shift:] + string.ascii_letters[:shift])
    return puzzle.translate(shift_map)

if __name__ == '__main__':
    puzzle = "map"
    print(Shift_Encrypt(puzzle, 2))
