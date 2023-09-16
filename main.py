from urllib.parse import urlparse, parse_qs, unquote


def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    query_params = parse_qs(parsed_url.query)
    result = {key: value[0] for key, value in query_params.items()}

    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    # New tests
    assert parse('https://example.com/?key=value&fruit=apple') == {'key': 'value', 'fruit': 'apple'}
    assert parse('http://example.com/?one=1&two=2&three=3') == {'one': '1', 'two': '2', 'three': '3'}
    assert parse('http://example.com/?a=1&a=2&a=3') == {'a': '1'}
    assert parse('http://example.com/?name=John%20Doe') == {'name': 'John Doe'}
    assert parse('http://example.com/?empty=') == {}
    
    
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