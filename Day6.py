# ***Task***
# Given a string,S , of length N that is indexed from 0 to N -1 , print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
#
# Note: 0 is considered to be an even index.
#
# Example
# s = abcdef
#
# Print abc def



T = int(input())
#S ='Hacker'
for i in range(0, T):
    S = input()
    print(S[0::2] + " " + S[1::2])