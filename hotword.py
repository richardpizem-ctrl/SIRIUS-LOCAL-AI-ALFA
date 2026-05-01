import speech_recognition as sr
from runtime.runtime_manager import RuntimeManager


class SiriusHotword:
    """
    HOTWORD režim pre SIRIUS-LOCAL-AI
    - čaká na vyslovenie "sirius"
    - po aktivácii počúva príkaz
    - príkaz pošle do NL Routera
    """

    def __init__(self):
        self.rm = RuntimeManager()
        self.rm.initialize()

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.hotword = "sirius"

    # --------------------------------------------------------
    # ROZPOZNÁVANIE HLASU
    # --------------------------------------------------------
    def listen(self):
        with self.microphone as source:
            print("🎤 Počúvam hotword...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="sk-SK").lower()
            print(f"➡ Rozpoznané: {text}")
            return text
        except:
            return ""

    # --------------------------------------------------------
    # POČÚVANIE PRÍKAZU PO HOTWORDE
    # --------------------------------------------------------
    def listen_command(self):
        with self.microphone as source:
            print("🎤 Počúvam príkaz...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="sk-SK")
            print(f"➡ Príkaz: {text}")
            return text
        except:
            print("❗ Nerozumel som príkazu.")
            return None

    # --------------------------------------------------------
    # SPRACOVANIE PRÍKAZU
    # --------------------------------------------------------
    def process(self, text):
        if not text:
            return

        result = self.rm.handle_nl(text)
        print("➡ Výsledok:", result)

    # --------------------------------------------------------
    # HLAVNÁ SLUČKA
    # --------------------------------------------------------
    def run(self):
        print("🟢 SIRIUS HOTWORD MODE – aktívne")
        print("Povedz: 'Sirius'")

        while True:
            text = self.listen()

            if self.hotword in text:
                print("🟡 Hotword detegovaný → čakám na príkaz...")
                command = self.listen_command()
                self.process(command)


# ------------------------------------------------------------
# SPÚŠŤACÍ BOD
# ------------------------------------------------------------
if __name__ == "__main__":
    hw = SiriusHotword()
    hw.run()
