m_keys: list[str] = []
m_values: list[str] = []


def keys() -> list[str]:
    return m_keys;


def values() -> list[str]:
    return m_values


def items() -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    return list(zip(m_keys, m_values))


def update(added_dict1: dict[str, str]) -> None:
    for k, v in added_dict1.items():
        if not k in m_keys:
            setdefault(k, v)
            continue
        index = m_keys.index(k)
        m_values[index] = v


def pop(key: str) -> str:
    if not key in m_keys:
        raise KeyError(f"KeyError: '{key}'")
    i_k = m_keys.index(key)
    del m_keys[i_k]
    return m_values.pop(i_k)


def get(key: str, message: str) -> str:
    if not key in m_keys:
        return message
    i_k = m_keys.index(key)
    return m_values[i_k]


def clear() -> None:
    global m_keys
    global m_values
    m_values = []
    m_keys = []


# if key not exist add,if key exist do nothing
def setdefault(key, value) -> None:
    if not key in m_keys:
        m_keys.append(key)
        m_values.append(value)
    return value


# update({'name': 'sharon'})
setdefault('name', 'sharon')
setdefault('city', 'Tel aviv')
setdefault('city', 'Tel aviv')
print(items())  # [('name', 'sharon'), ('city', 'Tel aviv')]
print(get('name', 'not exist'))  # sharon
print(get('age', 'not exist'))  # not exist
print(keys())  # ['name', 'city']
print(values())  # ['sharon', 'tel Aviv']
print(pop('name'))  # sharon
print(items())  # [('city', 'Tel aviv')]
clear()
print(items())  # []
