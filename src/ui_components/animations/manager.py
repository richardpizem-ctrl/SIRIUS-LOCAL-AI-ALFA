from .animation_scenes import (
    MoveScene,
    CopyScene,
    DeleteScene,
    CreateFolderScene
)


class AnimationManager:
    """Riadič animácií – prepína scény podľa typu operácie."""

    def __init__(self):
        self.current_scene = None

        # Predpripravené scény
        self.scenes = {
            "move": MoveScene(),
            "copy": CopyScene(),
            "delete": DeleteScene(),
            "create_folder": CreateFolderScene()
        }

    def play(self, scene_name: str):
        """Spustí požadovanú scénu podľa názvu."""
        if self.current_scene:
            self.current_scene.stop()

        scene = self.scenes.get(scene_name)
        if scene:
            self.current_scene = scene
            self.current_scene.start()

    def update(self, delta_time: float):
        """Aktualizuje aktívnu scénu."""
        if self.current_scene and self.current_scene.active:
            self.current_scene.update(delta_time)
