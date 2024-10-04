"""
Language detection starter
"""
# pylint:disable=too-many-locals, unused-argument, unused-variable
from lab_1_classify_by_unigrams.main import create_language_profile
from lab_1_classify_by_unigrams.main import detect_language


def main() -> None:
    """
    Launches an implementation
    """

    with open("assets/texts/en.txt", "r", encoding="utf-8") as file_to_read_en:
        en_text = file_to_read_en.read()
    with open("assets/texts/de.txt", "r", encoding="utf-8") as file_to_read_de:
        de_text = file_to_read_de.read()
    with open("assets/texts/unknown.txt", "r", encoding="utf-8") as file_to_read_unk:
        unknown_text = file_to_read_unk.read()
    english = create_language_profile('english', en_text)
    if not isinstance(english, dict):
        return None
    german = create_language_profile('german', de_text)
    if not isinstance(german, dict):
        return None
    unknown = create_language_profile('unknown', unknown_text)
    if not isinstance(unknown, dict):
        return None
    result = detect_language(unknown, english, german)
    print(result)
    assert result, "Detection result is None"


if __name__ == "__main__":
    main()
