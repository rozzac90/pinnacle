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
