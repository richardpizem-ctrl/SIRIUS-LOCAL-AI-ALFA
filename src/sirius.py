from commands.registry import create_default_registry


class SiriusAI:
    """
    Hlavný vstupný bod pre SIRIUS LOCAL AI ALFA.
    Spracováva vstup, vyhľadáva príkazy a vykonáva ich.
    """

    def __init__(self):
        self.registry = create_default_registry()

    def handle_input(self, text: str) -> str:
        """
        Spracuje textový vstup používateľa.
        """
        if not text.strip():
            return ""

        parts = text.split()
        command_name = parts[0]
        args = parts[1:]

        command = self.registry.get(command_name)

        if command is None:
            return f"Neznámy príkaz: {command_name}"

        try:
            return command.execute(*args)
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
