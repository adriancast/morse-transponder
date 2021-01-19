from playsound import playsound
from .utils import translate_to_morse


class MorseTransponder:

    @staticmethod
    def play_morse_text(morse_text: str):
        for character in morse_text:
            if character == '-':
                playsound('sounds/long.wav')
            elif character == '.':
                playsound('sounds/short.wav')

    def translate_to_morse_and_play_audio(self, text: str) -> str:
        morse_text = translate_to_morse(text=text)
        self.play_morse_text(morse_text=morse_text)
        return morse_text
