#!/usr/bin/env python3
"""
task:2. Hypermedia pagination
ocndition: mandatory
required:
Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments (and defaults)
as get_page and returns a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

You can use the math module if necessary.
"""

import csv
import math
from typing import List, Tuple, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[List, int]:
        """
        find the correct indexes to paginate the dataset correctly
        Args:
            page: (int) page number
            page_size: (int) number of records in one page
        Returns:
            a dictionary containing the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        assert isinstance(page, int) and isinstance(page_size, int), "!int"
        assert page > 0 and page_size > 0, "must be greater than 0"
        data = self.dataset()
        data_size = len(data)
        total_pages_number = (data_size + page_size - 1) // page_size
        try:
            start_index, end_index = index_range(page, page_size)
            p_data = data[start_index: end_index]

            if page < total_pages_number:
                next_page = page + 1
            else:
                next_page = None
            if page > 1:
                prev_page = page - 1
            else:
                prev_page = None
            response = {
                'page_size': len(p_data),
                'page': page,
                'data': p_data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages_number
            }

            return response

        except Exception:
            return {}
