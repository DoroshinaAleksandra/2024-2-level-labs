"""
Lab 1.

Language detection
"""
# pylint:disable=too-many-locals, unused-argument, unused-variable


def tokenize(text: str) -> list[str] | None:
    """
    Split a text into tokens.

    Convert the tokens into lowercase, remove punctuation, digits and other symbols

    Args:
        text (str): A text

    Returns:
        list[str] | None: A list of lower-cased tokens without punctuation

    In case of corrupt input arguments, None is returned
    """
    tokenized_text = []
    if not isinstance(text, str):
        return None
    text = text.lower()
    for element in text:
        if element.isalpha():
            tokenized_text += element
    return tokenized_text


def calculate_frequencies(tokens: list[str] | None) -> dict[str, float] | None:
    """
    Calculate frequencies of given tokens.

    Args:
        tokens (list[str] | None): A list of tokens

    Returns:
        dict[str, float] | None: A dictionary with frequencies

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(tokens, list):
        return None
    for element in tokens:
        if not isinstance(element, str):
            return None
    number_of_tokens = len(tokens)
    tokens_quantity = {}
    for letter in tokens:
        if letter not in tokens_quantity:
            tokens_quantity[letter] = 0
        tokens_quantity[letter] += 1
    tokens_frequency = {}
    for symbol, value in tokens_quantity.items():
        tokens_frequency[symbol] = value/number_of_tokens
    return tokens_frequency


def create_language_profile(language: str, text: str) -> dict[str, str | dict[str, float]] | None:
    """
    Create a language profile.

    Args:
        language (str): A language
        text (str): A text

    Returns:
        dict[str, str | dict[str, float]] | None: A dictionary with two keys – name, freq

    In case of corrupt input arguments, None is returned
    """
    if not isinstance(language, str):
        return None
    if not isinstance(text, str):
        return None
    language_profile = {'name': language, 'freq': calculate_frequencies(tokenize(text))}
    return language_profile


def calculate_mse(predicted: list, actual: list) -> float | None:
    """
    Calculate mean squared error between predicted and actual values.

    Args:
        predicted (list): A list of predicted values
        actual (list): A list of actual values

    Returns:
        float | None: The score

    In case of corrupt input arguments, None is returned
    """
    """
    if not isinstance(predicted, list):
        return None
    if not isinstance(actual, list):
        return None
    if len(predicted) != len(actual):
        return None
    summa = 0
    for i in range(len(actual)):
        part_of_summa = (actual[i] - predicted[i])**2
        summa += part_of_summa
    mse = 1/len(actual)*summa
    rounded_mse = round(mse, 3)
    return rounded_mse
    """


def compare_profiles(
    unknown_profile: dict[str, str | dict[str, float]],
    profile_to_compare: dict[str, str | dict[str, float]],
) -> float | None:
    """
    Compare profiles and calculate the distance using symbols.

    Args:
        unknown_profile (dict[str, str | dict[str, float]]): A dictionary of an unknown profile
        profile_to_compare (dict[str, str | dict[str, float]]): A dictionary of a profile
            to compare the unknown profile to

    Returns:
        float | None: The distance between the profiles

    In case of corrupt input arguments or lack of keys 'name' and
    'freq' in arguments, None is returned
    """
    """
    if not isinstance(unknown_profile, dict):
        return None
    for i in unknown_profile.keys():
        if i != 'name' or i != 'freq':
            return None
    for i in unknown_profile.values():
        if not isinstance(i, str) or not isinstance(i, dict):
            return None
        if i is dict:
            for k in i.keys():
                if not isinstance(k, str):
                    return None
            for v in i.values():
                if not isinstance(v, float):
                    return None
    unknown_freq = unknown_profile.get('freq')
    compared_freq = profile_to_compare.get('freq')
    for letter in unknown_freq:
        if letter not in compared_freq:
            compared_freq[letter] = 0
    for letter in compared_freq:
        if letter not in unknown_freq:
            unknown_freq[letter] = 0
    unknown_list = []
    for element in unknown_freq.values():
        unknown_list.append(element)
    compared_list = []
    for element in compared_freq.values():
        compared_list.append(element)
    mse = calculate_mse(unknown_list, compared_list)
    return mse
    """


def detect_language(
    unknown_profile: dict[str, str | dict[str, float]],
    profile_1: dict[str, str | dict[str, float]],
    profile_2: dict[str, str | dict[str, float]],
) -> str | None:
    """
    Detect the language of an unknown profile.

    Args:
        unknown_profile (dict[str, str | dict[str, float]]): A dictionary of a profile
            to determine the language of
        profile_1 (dict[str, str | dict[str, float]]): A dictionary of a known profile
        profile_2 (dict[str, str | dict[str, float]]): A dictionary of a known profile

    Returns:
        str | None: A language

    In case of corrupt input arguments, None is returned
    """
    """
    mse_1 = compare_profiles(unknown_profile, profile_1)
    mse_2 = compare_profiles(unknown_profile, profile_2)
    if mse_1 < mse_2:
        return profile_1['name']
    if mse_2 < mse_1:
        return profile_2['name']
    if mse_1 == mse_2:
        names = [profile_1['name'], profile_2['name']]
        names.sort()
        return names[0]
        """


def load_profile(path_to_file: str) -> dict | None:
    """
    Load a language profile.

    Args:
        path_to_file (str): A path to the language profile

    Returns:
        dict | None: A dictionary with at least two keys – name, freq

    In case of corrupt input arguments, None is returned
    """


def preprocess_profile(profile: dict) -> dict[str, str | dict] | None:
    """
    Preprocess profile for a loaded language.

    Args:
        profile (dict): A loaded profile

    Returns:
        dict[str, str | dict] | None: A dict with a lower-cased loaded profile
            with relative frequencies without unnecessary n-grams

    In case of corrupt input arguments or lack of keys 'name', 'n_words' and
    'freq' in arguments, None is returned
    """


def collect_profiles(paths_to_profiles: list) -> list[dict[str, str | dict[str, float]]] | None:
    """
    Collect profiles for a given path.

    Args:
        paths_to_profiles (list): A list of strings to the profiles

    Returns:
        list[dict[str, str | dict[str, float]]] | None: A list of loaded profiles

    In case of corrupt input arguments, None is returned
    """


def detect_language_advanced(
    unknown_profile: dict[str, str | dict[str, float]], known_profiles: list
) -> list | None:
    """
    Detect the language of an unknown profile.

    Args:
        unknown_profile (dict[str, str | dict[str, float]]): A dictionary of a profile
            to determine the language of
        known_profiles (list): A list of known profiles

    Returns:
        list | None: A sorted list of tuples containing a language and a distance

    In case of corrupt input arguments, None is returned
    """


def print_report(detections: list[tuple[str, float]]) -> None:
    """
    Print report for detection of language.

    Args:
        detections (list[tuple[str, float]]): A list with distances for each available language

    In case of corrupt input arguments, None is returned
    """
