#!/usr/bin/env python3
"""
task: 0. Simple helper function
condition: mandatory
required:
Write a function named index_range that takes two integer arguments page and
page_size.

The function should return a tuple of size two containing a start index and
an end index corresponding to the range of indexes to return in a list for
those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    calculates the start and end records for a page in: pagination

    Args:
        page: (int) page number
        page_size: (int) number of records in one page

    Returns:
        (tuble) the start and end index of records (start, end)
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
