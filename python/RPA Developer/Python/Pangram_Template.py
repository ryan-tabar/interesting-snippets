import string


def Pangram(input_text: str) -> str:
    # A function that returns any letters missing from the alphabet in the input string
    # (in alphabetical order)

    # remove duplicates by using sets
    text_set = set(input_text)

    # create alphabet set
    alphabet_set = set(string.ascii_lowercase)

    # find missing letters
    missing = list(sorted(alphabet_set - text_set))

    # join missing letters into a string and return it
    return "".join(missing)


testCases = [
    # Discription, testCase, expectedResult
    ["pangram", "The quick brown fox jumps over the lazy dog.", ""],
    ["pangram", "The quick brown fox jumps the lazy dog.", "v"],
]

# Run each test and validate the result against the expected result
for testCase in testCases:
    actualResult = Pangram(testCase[1])
    print(
        "{0}: Test {1}".format(
            testCase[0], "passed!" if actualResult == testCase[2] else "failed..."
        )
    )
