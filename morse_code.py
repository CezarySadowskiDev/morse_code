from morse_code_data import to_morse_code_mapping, from_morse_code_mapping


class MorseCode:
    def __init__(self, text: str):
        self.text = text

    def code_to_morse(self) -> str:
        output_text = ''

        try:
            for sign in self.text:
                output_text += to_morse_code_mapping[sign] + ' '
        except KeyError as e:
            return f"Unable to convert {e} sign to Morse code."

        return output_text.strip()

    def decode_from_morse(self) -> str:
        output_text = ''

        code_sections = self.text.split()

        try:
            for section in code_sections:
                output_text += from_morse_code_mapping[section]
        except KeyError as e:
            return f"Unknown Morse code sign: {e}"

        return output_text.strip()
