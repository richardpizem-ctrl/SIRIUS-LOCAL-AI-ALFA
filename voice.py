import speech_recognition as sr

from runtime.runtime_manager import RuntimeManager
from runtime.plugin_loader import PluginLoader
from runtime.nl_router import NaturalLanguageRouter


class SiriusVoice:
    """
    Hlasové ovládanie pre SIRIUS LOCAL AI – v2.0.0
    - počúva mikrofón
    - rozpoznáva hlas
    - posiela text do NL Routera 2.0
    """

    def __init__(self):
        # --- BOOTSTRAP RUNTIME 2.0 ---
        self.runtime = RuntimeManager()
        self.runtime.initialize()

        # Pluginy
        self.plugins = PluginLoader(self.runtime)
        self.plugins.load_all()

        # NL Router 2.0
        self.router = NaturalLanguageRouter(self.runtime, self.plugins)
        self.router.initialize()

        # Speech Recognition
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
        Pošle rozpoznaný text do NL Routera 2.0.
        """
        if not text:
            return

        try:
            result = self.router.route(text)
        except Exception as e:
            result = f"Error: {e}"

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
