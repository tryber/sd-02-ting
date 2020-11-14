def get_frequency_simple_report(word, Lines):
    return [
        {"linha": index + 1}
        for index, content in enumerate(Lines.get_list())
        if word.lower() in content.lower()
    ]


def get_frequency_complete_report(word, Lines):
    return [
        {"linha": index + 1, "content": content}
        for index, content in enumerate(Lines.get_list())
        if word.lower() in content.lower()
    ]
