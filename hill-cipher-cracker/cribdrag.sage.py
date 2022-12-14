'''
A general purpose Hill Cipher cracker using crib dragging of a known
plaintext. Supports 3x3 key matrices.
'''


# This file was *autogenerated* from the file /workspace/cribdrag.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_22 = Integer(22); _sage_const_23 = Integer(23); _sage_const_20 = Integer(20); _sage_const_21 = Integer(21); _sage_const_24 = Integer(24); _sage_const_25 = Integer(25); _sage_const_13 = Integer(13); _sage_const_12 = Integer(12); _sage_const_11 = Integer(11); _sage_const_10 = Integer(10); _sage_const_17 = Integer(17); _sage_const_16 = Integer(16); _sage_const_15 = Integer(15); _sage_const_14 = Integer(14); _sage_const_19 = Integer(19); _sage_const_18 = Integer(18)
import sys

KPT = "EPLANETTT"
# Proof of Concept
ciphertext = "TQRLJVSCDWHEZVFHXGXFNDFJQMWODOMWSEDJCTFQHUBLSXEPUFYJBMFQKHCBVBZSWCCHZPHK"

trans_letter_to_num = {
        'A' : _sage_const_0 ,
        'B' : _sage_const_1 ,
        'C' : _sage_const_2 ,
        'D' : _sage_const_3 ,
        'E' : _sage_const_4 ,
        'F' : _sage_const_5 ,
        'G' : _sage_const_6 ,
        'H' : _sage_const_7 ,
        'I' : _sage_const_8 ,
        'J' : _sage_const_9 ,
        'K' : _sage_const_10 ,
        'L' : _sage_const_11 ,
        'M' : _sage_const_12 ,
        'N' : _sage_const_13 ,
        'O' : _sage_const_14 ,
        'P' : _sage_const_15 ,
        'Q' : _sage_const_16 ,
        'R' : _sage_const_17 ,
        'S' : _sage_const_18 ,
        'T' : _sage_const_19 ,
        'U' : _sage_const_20 ,
        'V' : _sage_const_21 ,
        'W' : _sage_const_22 ,
        'X' : _sage_const_23 ,
        'Y' : _sage_const_24 ,
        'Z' : _sage_const_25 ,
            }

trans_num_to_letter = {v: k for k, v in trans_letter_to_num.items()}

modulo = len(trans_num_to_letter)
print "Modulo: " + str(modulo)

print "Cipher Alphabet: "
print trans_num_to_letter

def letter_to_num(c):
    return trans_letter_to_num[c]

def num_to_letter(n):
    return trans_num_to_letter[n]

def generate_keys(system1_solution, system2_solution, system3_solution):
    keys = []
    for (a, b, c) in system1_solution:
        for (d, e, f) in system2_solution:
            for (g, h, i) in system3_solution:
                keys.append([[a, b, c], [d, e, f], [g, h, i]])
    return keys

def text_mat_to_str(m):
    text = ""
    for c in range(len(m[_sage_const_0 ])):
        for r in range(len(m)):
            text += num_to_letter(int(m[r][c]))
    return text

def decrypt(trans_letter_to_num, ciphertext, KPT):
    if len(KPT) < _sage_const_9 :
        raise Exception, "Known plaintext is too short. If you don't have enough "\
                        "characters to meet the required length, please input a guess."

    ciphertext = list(ciphertext)
    ciphertext = [letter_to_num(x) for x in ciphertext]

    ciphertext_blocks = []
    for x in xrange(_sage_const_0 , len(ciphertext) - _sage_const_2 , _sage_const_3 ):
        ciphertext_blocks.append([ciphertext[x], ciphertext[x+_sage_const_1 ], ciphertext[x+_sage_const_2 ]])
    #print ciphertext
    print "Ciphertext: "
    print ciphertext_blocks

    ciphertext_blocks_mat = Matrix(IntegerModRing(modulo), ciphertext_blocks).transpose()

    #                   |a  b  c|
    # Solve for the key |d  e  f| such that (key * known plaintext = known ciphertext)
    #                   |g  h  i|
    # After the key is found, attempt to invert it. The original encryption key
    # must have been invertible. If the key is invertible, then invert it, and
    # right-multiply it by the ciphertext to get the decrypted plaintext.
    #   (key inverse * known ciphertext) 
    # = (key inverse * key * known plaintext)
    # = (identity * known plaintext)
    # = known plaintext
    for offset in range(len(ciphertext)-len(KPT)+_sage_const_1 ):
        mapping = []
        if offset % _sage_const_3  == _sage_const_0 :
            mapping.append((letter_to_num(KPT[_sage_const_0 ]), ciphertext[offset]))
            mapping.append((letter_to_num(KPT[_sage_const_1 ]), ciphertext[offset+_sage_const_1 ]))
            mapping.append((letter_to_num(KPT[_sage_const_2 ]), ciphertext[offset+_sage_const_2 ]))
            mapping.append((letter_to_num(KPT[_sage_const_3 ]), ciphertext[offset+_sage_const_3 ]))
            mapping.append((letter_to_num(KPT[_sage_const_4 ]), ciphertext[offset+_sage_const_4 ]))
            mapping.append((letter_to_num(KPT[_sage_const_5 ]), ciphertext[offset+_sage_const_5 ]))
            mapping.append((letter_to_num(KPT[_sage_const_6 ]), ciphertext[offset+_sage_const_6 ]))
            mapping.append((letter_to_num(KPT[_sage_const_7 ]), ciphertext[offset+_sage_const_7 ]))
            mapping.append((letter_to_num(KPT[_sage_const_8 ]), ciphertext[offset+_sage_const_8 ]))
        elif offset % _sage_const_3  == _sage_const_2 :
            mapping.append((letter_to_num(KPT[_sage_const_1 ]), ciphertext[offset+_sage_const_1 ]))
            mapping.append((letter_to_num(KPT[_sage_const_2 ]), ciphertext[offset+_sage_const_2 ]))
            mapping.append((letter_to_num(KPT[_sage_const_3 ]), ciphertext[offset+_sage_const_3 ]))
            mapping.append((letter_to_num(KPT[_sage_const_4 ]), ciphertext[offset+_sage_const_4 ]))
            mapping.append((letter_to_num(KPT[_sage_const_5 ]), ciphertext[offset+_sage_const_5 ]))
            mapping.append((letter_to_num(KPT[_sage_const_6 ]), ciphertext[offset+_sage_const_6 ]))
            mapping.append((letter_to_num(KPT[_sage_const_7 ]), ciphertext[offset+_sage_const_7 ]))
            mapping.append((letter_to_num(KPT[_sage_const_8 ]), ciphertext[offset+_sage_const_8 ]))
            mapping.append((letter_to_num(KPT[_sage_const_9 ]), ciphertext[offset+_sage_const_9 ]))
        else:
            mapping.append((letter_to_num(KPT[_sage_const_2 ]), ciphertext[offset+_sage_const_2 ]))
            mapping.append((letter_to_num(KPT[_sage_const_3 ]), ciphertext[offset+_sage_const_3 ]))
            mapping.append((letter_to_num(KPT[_sage_const_4 ]), ciphertext[offset+_sage_const_4 ]))
            mapping.append((letter_to_num(KPT[_sage_const_5 ]), ciphertext[offset+_sage_const_5 ]))
            mapping.append((letter_to_num(KPT[_sage_const_6 ]), ciphertext[offset+_sage_const_6 ]))
            mapping.append((letter_to_num(KPT[_sage_const_7 ]), ciphertext[offset+_sage_const_7 ]))
            mapping.append((letter_to_num(KPT[_sage_const_8 ]), ciphertext[offset+_sage_const_8 ]))
            mapping.append((letter_to_num(KPT[_sage_const_9 ]), ciphertext[offset+_sage_const_9 ]))
            mapping.append((letter_to_num(KPT[_sage_const_10 ]), ciphertext[offset+_sage_const_10 ]))

        var('a', 'b', 'c')
        system1_solution = solve_mod([
                mapping[_sage_const_0 ][_sage_const_0 ]*a + mapping[_sage_const_1 ][_sage_const_0 ]*b + mapping[_sage_const_2 ][_sage_const_0 ]*c == mapping[_sage_const_0 ][_sage_const_1 ],
                mapping[_sage_const_3 ][_sage_const_0 ]*a + mapping[_sage_const_4 ][_sage_const_0 ]*b + mapping[_sage_const_5 ][_sage_const_0 ]*c == mapping[_sage_const_3 ][_sage_const_1 ],
                mapping[_sage_const_6 ][_sage_const_0 ]*a + mapping[_sage_const_7 ][_sage_const_0 ]*b + mapping[_sage_const_8 ][_sage_const_0 ]*c == mapping[_sage_const_6 ][_sage_const_1 ],
                ], modulo)
        if len(system1_solution) == _sage_const_0 :
            continue
        var('d', 'e', 'f')
        system2_solution = solve_mod([
                mapping[_sage_const_0 ][_sage_const_0 ]*d + mapping[_sage_const_1 ][_sage_const_0 ]*e + mapping[_sage_const_2 ][_sage_const_0 ]*f == mapping[_sage_const_1 ][_sage_const_1 ],
                mapping[_sage_const_3 ][_sage_const_0 ]*d + mapping[_sage_const_4 ][_sage_const_0 ]*e + mapping[_sage_const_5 ][_sage_const_0 ]*f == mapping[_sage_const_4 ][_sage_const_1 ],
                mapping[_sage_const_6 ][_sage_const_0 ]*d + mapping[_sage_const_7 ][_sage_const_0 ]*e + mapping[_sage_const_8 ][_sage_const_0 ]*f == mapping[_sage_const_7 ][_sage_const_1 ],
                ], modulo)
        if len(system2_solution) == _sage_const_0 :
            continue
        var('g', 'h', 'i')
        system3_solution = solve_mod([
                mapping[_sage_const_0 ][_sage_const_0 ]*g + mapping[_sage_const_1 ][_sage_const_0 ]*h + mapping[_sage_const_2 ][_sage_const_0 ]*i == mapping[_sage_const_2 ][_sage_const_1 ],
                mapping[_sage_const_3 ][_sage_const_0 ]*g + mapping[_sage_const_4 ][_sage_const_0 ]*h + mapping[_sage_const_5 ][_sage_const_0 ]*i == mapping[_sage_const_5 ][_sage_const_1 ],
                mapping[_sage_const_6 ][_sage_const_0 ]*g + mapping[_sage_const_7 ][_sage_const_0 ]*h + mapping[_sage_const_8 ][_sage_const_0 ]*i == mapping[_sage_const_8 ][_sage_const_1 ],
                ], modulo)
        if len(system3_solution) == _sage_const_0 :
            continue
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        #print "Possible solutions: "
        #print "(a, b, c): " + str(system1_solution)
        #print "(d, e, f): " + str(system2_solution)
        #print "(g, h, i): " + str(system3_solution)
        print "Offset: " + str(offset)
        for key in generate_keys(system1_solution, system2_solution, system3_solution):
            key_mat = Matrix(IntegerModRing(modulo), key)
            if key_mat.is_invertible():
                inv_key = key_mat.inverse()
                print "Key: "
                print key_mat.numpy()
                print "Key inverse: "
                print inv_key.numpy()
                print text_mat_to_str((inv_key * ciphertext_blocks_mat).numpy())
            else:
                #print "Key not invertible!"
                pass

if __name__ == '__main__':
    decrypt(trans_letter_to_num, ciphertext, KPT)

