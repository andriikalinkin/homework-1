from urllib.parse import unquote


# def parse(query: str) -> dict:
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
#     assert parse('http://example.com/') == {}
#     assert parse('http://example.com/?') == {}
#     assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    cookie_parts = query.split(';')
    result = {}

    for part in cookie_parts:
        key_value = part.split('=', 1)

        if len(key_value) == 2:
            key, value = key_value
            key = unquote(key.strip())
            value = unquote(value.strip())
            result[key] = value

    return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    # New tests
    assert parse_cookie('color=red;size=large;shape=circle;') == {'color': 'red', 'size': 'large', 'shape': 'circle'}
    assert parse_cookie('name=Dima;age=28;city=New%20York;') == {'name': 'Dima', 'age': '28', 'city': 'New York'}
    assert parse_cookie('name=Dima;name=John;name=Jane;') == {'name': 'Jane'}
    assert parse_cookie('value=123;') == {'value': '123'}
    assert parse_cookie('name=;age=;') == {'name': '', 'age': ''}
    assert parse_cookie('name=Dima') == {'name': 'Dima'}
    assert parse_cookie('key=%21%40%23%24%25%5E%26%2A%28%29%7B%7D%5B%5D%3A%3B%2C%3C%3E%2F%3D%2B%20-') == {
        'key': '!@#$%^&*(){}[]:;,<>/=+ -'}
