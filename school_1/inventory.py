# inventory.py
_items = []

def add_item(item: str):
    if item not in _items:
        _items.append(item)

def remove_item(item: str):
    if item in _items:
        _items.remove(item)

def has_item(item: str) -> bool:
    return item in _items

def get_items() -> list:
    return _items