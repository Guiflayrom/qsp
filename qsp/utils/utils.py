def find_all_strings(nested_list) -> list:
    strings = []
    if isinstance(nested_list, str):
        return [nested_list]
    for item in nested_list:
        if isinstance(item, list):
            strings.extend(find_all_strings(item))
        elif isinstance(item, str):
            strings.append(item)
    return strings
