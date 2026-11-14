"""Config-driven keyboard input state."""
from direct.showbase.DirectObject import DirectObject


class InputManager(DirectObject):
    """Tracks held and newly pressed actions without coupling input to gameplay."""

    def __init__(self, bindings: dict[str, str]) -> None:
        self.bindings = dict(bindings)
        self.held: set[str] = set()
        self.just_pressed: set[str] = set()
        for action, key in self.bindings.items():
            self.accept(key, self._press, [action])
            self.accept(f"{key}-up", self._release, [action])

    def _press(self, action: str) -> None:
        if action not in self.held:
            self.just_pressed.add(action)
        self.held.add(action)

    def _release(self, action: str) -> None:
        self.held.discard(action)

    def is_down(self, action: str) -> bool:
        return action in self.held

    def consume_press(self, action: str) -> bool:
        """Return True once for each fresh key press."""
        if action not in self.just_pressed:
            return False
        self.just_pressed.discard(action)
        return True

    def destroy(self) -> None:
        self.ignoreAll()
        self.held.clear()
        self.just_pressed.clear()
