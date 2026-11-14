"""Orbiting third-person follow camera with mouse-look."""
from math import cos, radians, sin
from panda3d.core import WindowProperties, Vec3


class ThirdPersonCamera:
    """Follows a target while allowing mouse-controlled orbit."""

    def __init__(self, app, target, distance: float = 8.0,
                 height: float = 2.0, sensitivity: float = 110.0) -> None:
        self.app = app
        self.target = target
        self.distance = distance
        self.height = height
        self.sensitivity = sensitivity
        self.heading = 0.0
        self.pitch = 12.0
        self.min_pitch = -8.0
        self.max_pitch = 48.0
        self._center_pointer()

    def _center_pointer(self) -> None:
        if not self.app.win:
            return
        props = WindowProperties()
        props.setCursorHidden(True)
        self.app.win.requestProperties(props)
        self.app.win.movePointer(0, self.app.win.getXSize() // 2, self.app.win.getYSize() // 2)

    def update(self) -> None:
        win = self.app.win
        if win and self.app.mouseWatcherNode.hasMouse():
            pointer = win.getPointer(0)
            center_x, center_y = win.getXSize() // 2, win.getYSize() // 2
            dx = pointer.getX() - center_x
            dy = pointer.getY() - center_y
            self.heading -= dx * self.sensitivity * 0.001
            self.pitch = max(self.min_pitch, min(self.max_pitch,
                self.pitch + dy * self.sensitivity * 0.001))
            win.movePointer(0, center_x, center_y)

        h, p = radians(self.heading), radians(self.pitch)
        direction = Vec3(sin(h) * cos(p), -cos(h) * cos(p), sin(p))
        target_pos = self.target.getPos(self.app.render) + Vec3(0, 0, self.height)
        self.app.camera.setPos(target_pos - direction * self.distance)
        self.app.camera.lookAt(target_pos)
