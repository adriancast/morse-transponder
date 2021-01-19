
from .constants import ALPHABET_MAPPER, MORSE_MAPPER


def translate_to_alphabet(morse_text: str) -> str:
    translation_chars = []
    for character in morse_text.split():
        if character in MORSE_MAPPER:
            translation_chars.append(MORSE_MAPPER[character])
    return ''.join(translation_chars)

def translate_to_morse(text: str) -> str:
    translation_chars = []
    for character in text:
        if character in ALPHABET_MAPPER:
            translation_chars.append(ALPHABET_MAPPER[character])
    return ' '.join(translation_chars)
