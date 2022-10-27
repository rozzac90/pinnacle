## About this fork

Original repo seems dead, no commits and merges for years.
Cleaned up requirements, fixed tests and bumped docker python image version to nice and fast 3.11


## Original repo README

# pinnacle
Python Wrapper for Pinnacle Sports API

[Pinnacle Documentation](https://www.pinnacle.com/en/api/manual)

# Installation

```
$ pip install pinnacle
```

# Usage

```python
>>> from pinnacle.apiclient import APIClient
>>> api = APIClient('username', 'password')
>>> sport_ids = api.reference_data.get_sports()
>>> tennis_events = api.market_data.get_fixtures(33)
```
