"""
Lab 2.

Text retrieval with BM25
"""
import copy
import math

# pylint:disable=too-many-arguments, unused-argument


def tokenize(text: str) -> list[str] | None:
    """
    Tokenize the input text into lowercase words without punctuation, digits and other symbols.

    Args:
        text (str): The input text to tokenize.

    Returns:
        list[str] | None: A list of words from the text.

    In case of corrupt input arguments, None is returned.
    """
    if not isinstance(text, str):
        return None
    tokenized_text = ''
    for element in text.lower():
        if element.isalpha() or element == ' ':
            tokenized_text += element
        else:
            tokenized_text += ' '
    return tokenized_text.split()


def remove_stopwords(tokens: list[str], stopwords: list[str]) -> list[str] | None:
    """
    Remove stopwords from the list of tokens.

    Args:
        tokens (list[str]): List of tokens.
        stopwords (list[str]): List of stopwords.

    Returns:
        list[str] | None: Tokens after removing stopwords.

    In case of corrupt input arguments, None is returned.
    """
    if (not isinstance(tokens, list) or not all(isinstance(token, str) for token in tokens)
            or not tokens):
        return None
    if (not isinstance(stopwords, list) or not all(isinstance(words, str) for words in stopwords)
            or not stopwords):
        return None
    new_tokens = copy.deepcopy(tokens)
    for token in tokens:
        if token in stopwords:
            new_tokens.remove(token)
    return new_tokens


def build_vocabulary(documents: list[list[str]]) -> list[str] | None:
    """
    Build a vocabulary from the documents.

    Args:
        documents (list[list[str]]): List of tokenized documents.

    Returns:
        list[str] | None: List with unique words from the documents.

    In case of corrupt input arguments, None is returned.
    """
    if (not isinstance(documents, list) or not all(isinstance(text, list) for text in documents)
            or not documents):
        return None
    for text in documents:
        for word in text:
            if not isinstance(word, str):
                return None
    unique_words = []
    for text in documents:
        for word in text:
            if word not in unique_words:
                unique_words.append(word)
    return unique_words


def calculate_tf(vocab: list[str], document_tokens: list[str]) -> dict[str, float] | None:
    """
    Calculate term frequency for the given tokens based on the vocabulary.

    Args:
        vocab (list[str]): Vocabulary list.
        document_tokens (list[str]): Tokenized document.

    Returns:
        dict[str, float] | None: Mapping from vocabulary terms to their term frequency.

    In case of corrupt input arguments, None is returned.
    """
    if (not isinstance(vocab, list) or not all(isinstance(word, str) for word in vocab)
            or not vocab):
        return None
    if (not isinstance(document_tokens, list) or not all(isinstance(token, str) for token in document_tokens)
            or not document_tokens):
        return None
    term_frequency = {}
    for word in document_tokens:
        if word not in vocab:
            vocab.append(word)
    for word in vocab:
        term_frequency[word] = document_tokens.count(word) / len(document_tokens)
    return term_frequency


def calculate_idf(vocab: list[str], documents: list[list[str]]) -> dict[str, float] | None:
    """
    Calculate inverse document frequency for each term in the vocabulary.

    Args:
        vocab (list[str]): Vocabulary list.
        documents (list[list[str]]): List of tokenized documents.

    Returns:
        dict[str, float] | None: Mapping from vocabulary terms to its IDF scores.

    In case of corrupt input arguments, None is returned.
    """
    if (not isinstance(vocab, list) or not all(isinstance(word, str) for word in vocab)
            or not vocab):
        return None
    if (not isinstance(documents, list) or not all(isinstance(token, list) for token in documents)
            or not documents):
        return None
    for text in documents:
        for word in text:
            if not isinstance(word, str):
                return None
    inverse_document_frequency = {}
    n = len(documents)
    for word in vocab:
        docs_with_word = 0
        for text in documents:
            if word in text:
                docs_with_word += 1
        idf = math.log((n - docs_with_word + 0.5)/(docs_with_word + 0.5))
        inverse_document_frequency[word] = idf
    return inverse_document_frequency


def calculate_tf_idf(tf: dict[str, float], idf: dict[str, float]) -> dict[str, float] | None:
    """
    Calculate TF-IDF scores for a document.

    Args:
        tf (dict[str, float]): Term frequencies for the document.
        idf (dict[str, float]): Inverse document frequencies.

    Returns:
        dict[str, float] | None: Mapping from terms to their TF-IDF scores.

    In case of corrupt input arguments, None is returned.
    """
    if not isinstance(tf, dict) or not isinstance(idf, dict) or not tf or not idf:
        return None
    if (not all(isinstance(key, str) and isinstance(value, float) for key, value in tf.items())
            or not all(isinstance(key, str) and isinstance(value, float) for key, value in idf.items())):
        return None
    tf_idf = {}
    for k, v in tf.items():
        tf_idf[k] = v * idf[k]
    return tf_idf


def calculate_bm25(
    vocab: list[str],
    document: list[str],
    idf_document: dict[str, float],
    k1: float = 1.5,
    b: float = 0.75,
    avg_doc_len: float | None = None,
    doc_len: int | None = None,
) -> dict[str, float] | None:
    """
    Calculate BM25 scores for a document.

    Args:
        vocab (list[str]): Vocabulary list.
        document (list[str]): Tokenized document.
        idf_document (dict[str, float]): Inverse document frequencies.
        k1 (float): BM25 parameter.
        b (float): BM25 parameter.
        avg_doc_len (float | None): Average document length.
        doc_len (int | None): Length of the document.

    Returns:
        dict[str, float] | None: Mapping from terms to their BM25 scores.

    In case of corrupt input arguments, None is returned.
    """
    if (not isinstance(doc_len, int) or not isinstance(avg_doc_len, float)
            or not isinstance(k1, float) or not isinstance(b, float)
            or isinstance(doc_len, bool)):
        return None
    if not vocab or not document or not idf_document:
        return None
    if (not isinstance(vocab, list) or not isinstance(document, list)
            or not isinstance(idf_document, dict)):
        return None
    if (not all(isinstance(word, str) for word in vocab)
            or not all(isinstance(word, str) for word in document)
            or not all(isinstance(k, str) and isinstance(v, float) for k, v in idf_document.items())):
        return None
    bm25 = {}
    for word in document:
        if word not in vocab:
            bm25[word] = 0.0
    for token, idf in idf_document.items():
        n_t = document.count(token)
        bm25[token] = idf * ((n_t * (k1 + 1))/(n_t + k1 * (1 - b + b * (doc_len/avg_doc_len))))
    return bm25


def rank_documents(
    indexes: list[dict[str, float]], query: str, stopwords: list[str]
) -> list[tuple[int, float]] | None:
    """
    Rank documents for the given query.

    Args:
        indexes (list[dict[str, float]]): List of BM25 or TF-IDF indexes for the documents.
        query (str): The query string.
        stopwords (list[str]): List of stopwords.

    Returns:
        list[tuple[int, float]] | None: Tuples of document index and its score in the ranking.

    In case of corrupt input arguments, None is returned.
    """


def calculate_bm25_with_cutoff(
    vocab: list[str],
    document: list[str],
    idf_document: dict[str, float],
    alpha: float,
    k1: float = 1.5,
    b: float = 0.75,
    avg_doc_len: float | None = None,
    doc_len: int | None = None,
) -> dict[str, float] | None:
    """
    Calculate BM25 scores for a document with IDF cutoff.

    Args:
        vocab (list[str]): Vocabulary list.
        document (list[str]): Tokenized document.
        idf_document (dict[str, float]): Inverse document frequencies.
        alpha (float): IDF cutoff threshold.
        k1 (float): BM25 parameter.
        b (float): BM25 parameter.
        avg_doc_len (float | None): Average document length.
        doc_len (int | None): Length of the document.

    Returns:
        dict[str, float] | None: Mapping from terms to their BM25 scores with cutoff applied.

    In case of corrupt input arguments, None is returned.
    """


def save_index(index: list[dict[str, float]], file_path: str) -> None:
    """
    Save the index to a file.

    Args:
        index (list[dict[str, float]]): The index to save.
        file_path (str): The path to the file where the index will be saved.
    """


def load_index(file_path: str) -> list[dict[str, float]] | None:
    """
    Load the index from a file.

    Args:
        file_path (str): The path to the file from which to load the index.

    Returns:
        list[dict[str, float]] | None: The loaded index.

    In case of corrupt input arguments, None is returned.
    """


def calculate_spearman(rank: list[int], golden_rank: list[int]) -> float | None:
    """
    Calculate Spearman's rank correlation coefficient between two rankings.

    Args:
        rank (list[int]): Ranked list of document indices.
        golden_rank (list[int]): Golden ranked list of document indices.

    Returns:
        float | None: Spearman's rank correlation coefficient.

    In case of corrupt input arguments, None is returned.
    """
