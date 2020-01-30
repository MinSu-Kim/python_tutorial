def tag(name, *content, cls=None, **attrs):
    """하나 이상의 HTML테그를 생성한다."""

    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == "__main__":
    print(tag('br'))                            #tag(name)
    print(tag('p', 'hello'))                    # tag(name, *content)
    print(tag('p', 'hello', 'world'))           # tag(name, *content)
    print(tag('p', 'hello', id=33))             # tag(name, *content, **attrs)
    print(tag('p', 'hello', cls='sidebar'))     # tag(name, *content, cls)
    print(tag(content='testing', name='img'))   # tag(name, **attrs)

    """
    my_tag 딕셔너리 앞에 **를 붙이면 딕셔너리 안의 모든 항목을 별도의 인수로 전달하고, 
    명명된 매개변수(name, cls) 및 나머지는 **attrs에 전달
    """
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sungset.jpg', 'cls': 'framed'}
    print(tag(**my_tag))
