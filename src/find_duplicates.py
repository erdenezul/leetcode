def find_cycle(nums):
    """
    Find duplicate number in array using O(1) space

    >>> find_cycle([1, 3, 4, 2, 2])
    2
    """
    tortoise, hare = nums[0], nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    pt1 = nums[0]
    pt2 = tortoise
    while pt1 != pt2:
        pt1 = nums[pt1]
        pt2 = nums[pt2]
    return pt1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
