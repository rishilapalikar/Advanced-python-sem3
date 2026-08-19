# Program to find the Longest Common Subsequence (LCS)
# using Dynamic Programming

def lcs(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create a table to store LCS lengths
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Find the LCS string
    i = m
    j = n
    lcs_sequence = ""

    while i > 0 and j > 0:

        if seq1[i - 1] == seq2[j - 1]:
            lcs_sequence = seq1[i - 1] + lcs_sequence
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return lcs_sequence


# Input from the user
sequence1 = input("Enter the first sequence: ")
sequence2 = input("Enter the second sequence: ")

result = lcs(sequence1, sequence2)

print("Longest Common Subsequence:", result)
print("Length of LCS:", len(result))