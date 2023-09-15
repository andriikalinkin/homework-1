from urllib.parse import urlparse, parse_qs


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


# def parse_cookie(query: str) -> dict:
#     return {}
#
#
# if __name__ == '__main__':
#     assert parse_cookie('name=Dima;') == {'name': 'Dima'}
#     assert parse_cookie('') == {}
#     assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
#     assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
