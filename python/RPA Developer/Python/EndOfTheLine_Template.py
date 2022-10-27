def EndOfTheLine(wagons: int, outgoing: str) -> bool:

    # convert string numbers into list of ints
    permutation = [int(x) for x in list(outgoing)]

    # generate western branch of wagons
    west = list(range(wagons, 0, -1))

    # create empty station
    station = []

    # create empty eastern branch
    east = []

    # keep track of position in permutation (start with zeroth index)
    permutation_position = 0

    while 1:

        if len(west) != 0:
            # move first wagon from western branch into station
            station.insert(0, west.pop())

        try:
            # check if value in top of list in station is equal to the corrospnding value in the permutation
            if station[0] == permutation[permutation_position]:
                # move it into eastern branch
                east.insert(0, station.pop(0))
                permutation_position += 1

            elif len(west) == 0:
                # else if the western branch is empty, we couldn't move into eastern branch
                return False
        except IndexError:
            # if we moved onto an invalid permutation position, we've succeded
            # since all the wagons have moved to the east
            return True


testCases = [
    # Discription, testCase, expectedResult
    ["From the interview", "132", True],
    ["My own test 1", "1324", False],
]

# Run each test and validate the result against the expected result
for testCase in testCases:
    actualResult = EndOfTheLine(len(testCase[1]), testCase[1])
    print(
        "{0}: Test {1}".format(
            testCase[0], "passed!" if actualResult == testCase[2] else "failed..."
        )
    )

