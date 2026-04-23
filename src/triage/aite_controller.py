from .input_classifier import InputClassifier
from .input_router import InputRouter
from .metadata_builder import MetadataBuilder


class AITEController:
    """
    Automatic Input Triage Engine (AITE)
    Rozpoznáva typ vstupu, určuje cieľové úložisko a vytvára metadáta.
    """

    def __init__(self):
        self.classifier = InputClassifier()
        self.router = InputRouter()
        self.metadata = MetadataBuilder()

    def process(self, input_path: str) -> dict:
        """
        Spracuje vstupný súbor:
        - rozpozná typ
        - určí cieľovú cestu
        - vytvorí metadáta
        (FS-AGENT presun vykoná neskôr)
        """

        input_type = self.classifier.classify(input_path)
        target = self.router.route(input_type)
        meta = self.metadata.build(input_path, input_type)

        return {
            "input": input_path,
            "type": input_type,
            "target": target,
            "metadata": meta
        }

