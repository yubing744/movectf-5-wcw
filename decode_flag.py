
trans_letter_to_num = {
        'A' : 0,
        'B' : 1,
        'C' : 2,
        'D' : 3,
        'E' : 4,
        'F' : 5,
        'G' : 6,
        'H' : 7,
        'I' : 8,
        'J' : 9,
        'K' : 10,
        'L' : 11,
        'M' : 12,
        'N' : 13,
        'O' : 14,
        'P' : 15,
        'Q' : 16,
        'R' : 17,
        'S' : 18,
        'T' : 19,
        'U' : 20,
        'V' : 21,
        'W' : 22,
        'X' : 23,
        'Y' : 24,
        'Z' : 25,
        ' ' : 26,
        ',' : 27,
        '.' : 28,
        '?' : 29,
        '!' : 30,
            }

trans_num_to_letter = {v: k for k, v in trans_letter_to_num.items()}

def letter_to_num(c):
    return trans_letter_to_num[c]

def num_to_letter(n):
    return trans_num_to_letter[n]

Key = [25, 11, 6, 10, 13, 25, 12, 19, 2]
Key_inverse = [3, 20, 1, 10, 2, 23, 4, 17, 23]
plattext = "EPLANETTTCONGRATULATIONSYOUMANAGEDTOBREAKTHEHILLCIPHERHACKTHEHACKYPLANET"

if __name__ == '__main__':
  print("plattext:", [letter_to_num(x) for x in plattext])

# plattext: [4, 15, 11, 0, 13, 4, 19, 19, 19, 2, 14, 13, 6, 17, 0, 19, 20, 11, 0, 19, 8, 14, 13, 18, 24, 14, 20, 12, 0, 13, 0, 6, 4, 3, 19, 14, 1, 17, 4, 0, 10, 19, 7, 4, 7, 8, 11, 11, 2, 8, 15, 7, 4, 17, 7, 0, 2, 10, 19, 7, 4, 7, 0, 2, 10, 24, 15, 11, 0, 13, 4, 19]