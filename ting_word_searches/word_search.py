import re


def does_word_exist(word, setence):
    return re.match(
        r"\s?" + word + r"\s|\s" + word + r"\s?|" + word, setence
    ) is not None


def exists_word(word, queue):
    return [
        {
            "palavra": word,
            "arquivo": val["nome_do_arquivo"],
            "ocorrencias": [
                {
                    "line": line,
                }
                for line, setence in enumerate(val["content"])
                if does_word_exist(word, setence)
            ],
        }
        for val in queue.interavel()
    ]


def search_by_word(word, queue):
    return [
        {
            "palavra": word,
            "arquivo": val["nome_do_arquivo"],
            "ocorrencias": [
                {
                    "line": line,
                    "conteudo": setence,
                }
                for line, setence in enumerate(val["content"])
                if does_word_exist(word, setence)
            ],
        }
        for val in queue.interavel()
    ]
