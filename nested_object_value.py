def get_value_from_nested_object(obj, key):
    keys = key.split('/')
    value = obj
    try:
        for k in keys:
            value = value[k]
        return value
    except (KeyError, TypeError):
        return None

# Test Cases
def test_get_value_from_nested_object():
    # Test case 1
    object1 = {"a": {"b": {"c": "d"}}}
    key1 = "a/b/c"
    assert get_value_from_nested_object(object1, key1) == "d"

    # Test case 2
    object2 = {"x": {"y": {"z": "a"}}}
    key2 = "x/y/z"
    assert get_value_from_nested_object(object2, key2) == "a"

    # Test case 3: Nested object with more levels
    object3 = {"a": {"b": {"c": {"d": {"e": "f"}}}}}
    key3 = "a/b/c/d/e"
    assert get_value_from_nested_object(object3, key3) == "f"

    # Test case 4: Key not found
    object4 = {"a": {"b": {"c": "d"}}}
    key4 = "x/y/z"
    assert get_value_from_nested_object(object4, key4) is None

    # Test case 5: Empty key
    object5 = {"x": "y"}
    key5 = ""
    assert get_value_from_nested_object(object5, key5) == object5

    # Test case 6: Non-dictionary object
    object6 = "This is a string"
    key6 = "a/b/c"
    assert get_value_from_nested_object(object6, key6) is None

    print("All test cases passed successfully.")

if __name__ == "__main__":
    test_get_value_from_nested_object()
