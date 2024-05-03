#!/usr/bin/env python3
"""
task: 1. Simple pagination
coindition: mandatory
required:
Copy index_range from the previous task and the following class into your code
Implement a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10.
Use assert to verify that both arguments are integers greater than 0.
Use index_range to find the correct indexes to paginate the dataset correctly
and return the appropriate page of the dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset, an empty list should
be returned.
"""

import csv
import math
from typing import List
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        find the correct indexes to paginate the dataset correctly
        Args:
            page: (int) page number
            page_size: (int) number of records in one page
        Returns:
            the appropriate page of the dataset
            (i.e. the correct list of rows).
            If the input arguments are out of range for the dataset,
            an empty list should be returned.
        """
        assert isinstance(page, int) and isinstance(page_size, int), "!int"
        assert page > 0 and page_size > 0, "must be greater than 0"
        data = self.dataset()
        # print(self.__dataset[1:5])
        try:
            start_index, end_index = index_range(page, page_size)
            # print(start_index, end_index)
            return data[start_index: end_index]
        except Exception:
            return []
