import speech_recognition as sr
from runtime.runtime_manager import RuntimeManager


class SiriusVoice:
    """
    Hlasové ovládanie pre SIRIUS-LOCAL-AI
    - počúva mikrofón
    - rozpoznáva hlas
    - posiela text do NL Routera
    """

    def __init__(self):
        self.rm = RuntimeManager()
        self.rm.initialize()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    # --------------------------------------------------------
    # ROZPOZNÁVANIE HLASU
    # --------------------------------------------------------
    def listen(self):
        """
        Počúva mikrofón a vracia rozpoznaný text.
        """
        with self.microphone as source:
            print("🎤 Počúvam...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="sk-SK")
            print(f"➡ Rozpoznané: {text}")
            return text
        except sr.UnknownValueError:
            print("❗ Nerozumel som.")
            return None
        except sr.RequestError:
            print("❗ Chyba pri komunikácii so službou rozpoznávania.")
            return None

    # --------------------------------------------------------
    # SPRACOVANIE PRÍKAZU
    # --------------------------------------------------------
    def process(self, text):
        """
        Pošle rozpoznaný text do NL Routera.
        """
        if not text:
            return

        result = self.rm.handle_nl(text)
        print("➡ Výsledok:", result)

    # --------------------------------------------------------
    # HLAVNÁ SLUČKA
    # --------------------------------------------------------
    def run(self):
        """
        Nekonečná slučka – počúva hlas a spracováva príkazy.
        """
        print("🎙️ SIRIUS Voice Control – aktívne")
        print("Povedz príkaz...")

        while True:
            text = self.listen()
            self.process(text)


# ------------------------------------------------------------
# SPÚŠŤACÍ BOD
# ------------------------------------------------------------
if __name__ == "__main__":
    voice = SiriusVoice()
    voice.run()
