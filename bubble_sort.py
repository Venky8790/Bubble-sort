import copy


def bubble_sort_v_one(container: object) -> object:
    """
        Bubble sort with first optimization.

        Description
        ----------
        From wikipedia: inner loop can avoid looking
        at the last (length − 1) items when running for the n-th time.
        Performance cases:
        Worst      : O(n^2)
        Average    : O(n^2)
        Best case  : O(n)

        Parameters
        ----------
        container : Mutable container with comparable objects and structure
                         which has implemented __len__, __getitem__ and __setitem__.

        Returns
        -------
        container : Sorted container

        Examples
        ----------
        >>> bubble_sort_v_one([7,1,2,6,4,2,3])
        [1, 2, 2, 3, 4, 6, 7]

        >>> bubble_sort_v_one(['a', 'c', 'b'])
        ['a', 'b', 'c']

    """

    # setting up variables
    container = copy.copy(container)
    length = len(container)
    changed = True

    while changed:
        changed = False
        for i in range(length - 1):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
                changed = True
        length -= 1
    return container


def bubble_sort_v_two(container: object) -> object:
    """
        Bubble sort with second optimization.

        Description
        ----------
        From wikipedia: This allows us to skip over a lot of the elements,
        resulting in about a worst case 50% improvement in comparison count.
        Performance cases:
        Worst      : O(n^2) - 50%
        Average    : O(n^2)
        Best case  : O(n)

        Parameters
        ----------
        container : Mutable container with comparable objects and structure
                         which has implemented __len__, __getitem__ and __setitem__.

        Returns
        -------
        container : Sorted container

        Examples
        ----------
        >>> bubble_sort_v_two([7,1,2,6,4,2,3])
        [1, 2, 2, 3, 4, 6, 7]

        >>> bubble_sort_v_two(['a', 'c', 'b'])
        ['a', 'b', 'c']

    """

    # setting up variables
    container = copy.copy(container)
    length = len(container)

    while length >= 1:
        changed_times = 0
        for i in range(1, length):
            if container[i - 1] > container[i]:
                container[i - 1], container[i] = container[i], container[i - 1]
                changed_times = i
        length = changed_times
    return container