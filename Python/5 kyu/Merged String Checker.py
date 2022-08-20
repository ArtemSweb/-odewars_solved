"""Merged String Checker"""


def is_merge(s, part1, part2):
    return \
        part1 and part1[0] == s[0] and is_merge(s[1:], part1[1:], part2) or \
        part2 and part2[0] == s[0] and is_merge(s[1:], part1, part2[1:]) or \
        False if s else not part1 and not part2



print(is_merge('codewars', 'code', 'wars')) # True
print(is_merge('codewars', 'code', 'wasr')) # False
print(is_merge('codewars', 'cdw', 'oears')) # True 
print(is_merge('codewars', 'cod', 'wars'))  # False