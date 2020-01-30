from inspect import signature


def clip(text, max_len:'int >0'=80) -> str:
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
    print(clip.__annotations__)
    sig = signature(clip)
    print(sig.return_annotation)
    print()
    [print(repr(param.annotation).ljust(13), ":", param.name, '=', param.default) for param in sig.parameters.values()]