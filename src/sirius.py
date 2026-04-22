from commands.registry import create_default_registry
from context.context_manager import ContextManager


class SiriusAI:
    """
    Hlavný vstupný bod pre SIRIUS LOCAL AI ALFA.
    Spracováva vstup, vyhľadáva príkazy, vykonáva ich
    a ukladá kontext.
    """

    def __init__(self):
        self.registry = create_default_registry()
        self.context = ContextManager()  # prepojený context manager

    def handle_input(self, text: str) -> str:
        """
        Spracuje textový vstup používateľa.
        """
        if not text.strip():
            return ""

        # uloženie do krátkodobej pamäte
        self.context.remember(text)

        parts = text.split()
        command_name = parts[0]
        args = parts[1:]

        command = self.registry.get(command_name)

        if command is None:
            return f"Neznámy príkaz: {command_name}"

        try:
            result = command.execute(*args)
            return result
        except Exception as e:
            return f"Chyba pri vykonávaní príkazu: {e}"


def main():
    ai = SiriusAI()

    print("SIRIUS LOCAL AI ALFA — konzolový režim")
    print("Napíš 'help' pre zoznam príkazov, 'exit' pre ukončenie.\n")

    while True:
        user_input = input(">>> ").strip()

        if user_input.lower() == "exit":
            print("Ukončujem SIRIUS AI.")
            break

        output = ai.handle_input(user_input)
        if output:
            print(output)


if __name__ == "__main__":
    main()
