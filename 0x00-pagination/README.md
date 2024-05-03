# Pagination Techniques

This README provides an overview of different pagination techniques, including pagination with simple parameters, pagination with hypermedia metadata, and pagination in a deletion-resilient manner.

## Table of Contents
1. [Pagination with Simple Parameters](#pagination-with-simple-parameters)
2. [Pagination with Hypermedia Metadata](#pagination-with-hypermedia-metadata)
3. [Pagination in a Deletion-Resilient Manner](#pagination-in-a-deletion-resilient-manner)

---

## Pagination with Simple Parameters

Pagination with simple parameters involves using basic page and page size parameters to navigate through a dataset.

### How It Works
- Use `page` parameter to specify the page number.
- Use `page_size` parameter to specify the number of items per page.
- Fetch data from the dataset based on the specified page and page size.

### Example
"""python
# Fetch page 2 with 10 items per page
page_number = 2
page_size = 10
results = fetch_data(page=page_number, page_size=page_size)
"""

## Pagination with Hypermedia Metadata

Pagination with hypermedia metadata involves providing additional metadata along with the paginated dataset to facilitate navigation and discovery.

### How It Works
- Include hypermedia links in the paginated response to navigate to the next, previous, first, and last pages.
- Provide metadata such as total number of items, current page number, total number of pages, etc.

### Example
```json
{
  "data": [...],
  "metadata": {
    "total_items": 1000,
    "page": 2,
    "page_size": 10,
    "total_pages": 100,
    "links": {
      "first": "/api/data?page=1&page_size=10",
      "prev": "/api/data?page=1&page_size=10",
      "next": "/api/data?page=3&page_size=10",
      "last": "/api/data?page=100&page_size=10"
    }
  }
}
```

## Pagination in a Deletion-Resilient Manner

Pagination in a deletion-resilient manner ensures consistent pagination even when items are deleted from the dataset.

### How It Works
- Use stable identifiers or timestamps for pagination instead of sequential indices.
- Handle deleted items gracefully to avoid skipping or duplicating items during pagination.

### Example
```python
# Fetch items newer than a specified timestamp
timestamp = get_latest_timestamp()
results = fetch_data_newer_than(timestamp)
```

---

These pagination techniques offer different approaches to navigating through large datasets effectively. Choose the one that best fits your application's requirements.
