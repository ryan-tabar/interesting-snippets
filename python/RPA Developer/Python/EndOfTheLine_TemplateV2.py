import itertools


def EndOfTheLine(wagons: int, outgoing: str) -> bool:

    # convert string numbers into list of ints
    permutation = [int(x) for x in list(outgoing)]

    # generate western branch of wagons
    western_branch = list(range(wagons, 0, -1))

    # create empty station
    station = []

    # create empty eastern branch
    eastern_branch = []

    # keep track of position in permutation (start with zeroth index)
    permutation_position = 0
    while len(western_branch) != 0:
        # move first wagon from western branch into station
        station.insert(0, western_branch.pop())

        # check if value at the top of station is equal to the corrospnding value in the permutation
        while len(station) != 0 and station[0] == permutation[permutation_position]:
            # move it into eastern_branchern branch
            eastern_branch.insert(0, station.pop(0))
            permutation_position += 1

        if len(eastern_branch) == wagons:
            # permutation is possible
            return True
    else:
        # western branch is empty and eastern branch does not have all the wagons
        # therefore, permutation is not possible
        return False


testCases = [
    # Discription, testCase, expectedResult
    ["Permutation", "132", True],
    ["Permutation", "312", False],
]

# perms = itertools.permutations(range(1, 4))
# testCases = [["Permutation", "".join(map(str,perm)), True] for perm in perms]

# Run each test and validate the result against the expected result
for testCase in testCases:
    actualResult = EndOfTheLine(len(testCase[1]), testCase[1])
    print(
        "{0}: Test {1} Sequence: {2}".format(
            testCase[0],
            "passed!  " if actualResult == testCase[2] else "failed...",
            testCase[1],
        )
    )
