import html


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


if __name__ == "__main__":
    print(htmlize({1, 2, 3}))
    print(htmlize(abs))
    print(htmlize('Heimlich & co.\n- a game'))
    print(htmlize(42))
    print(htmlize(['alpha', 66, {3, 2, 1}]))