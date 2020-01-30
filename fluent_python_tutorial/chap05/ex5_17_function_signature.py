from inspect import signature

from fluent_python_tutorial.chap05.ex5_10_keyword_only_argument import tag


def clip(text, max_len=80):
    """max_len 앞이나 뒤에 마지막 공백에서 잘라낸 텍스트를 반환한다
    """

    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None: # 공백이 없음
        end = len(text)
    return text[:end].rstrip()


if __name__ == "__main__":
    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_varnames, clip.__code__.co_argcount)

    sig = signature(clip)
    print(sig)
    [print(param.kind, ":", name, '=', param.default) for name, param in sig.parameters.items()]

    sig = signature(tag)
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sungset.jpg', 'cls': 'framed'}
    bound_args = sig.bind(**my_tag)
    print(bound_args)

    del my_tag['name']
    bound_args = sig.bind(**my_tag)  # TypeError: missing a required argument: 'name'
    print(bound_args)