"""
Misc functions:
- io
- idk
"""

import pygame

import soragl as SORA
from soragl import scene

# ------------------------------------------------------------ #
# misc functions!
"""
General Misc Functions
"""
# ------------------------------------------------------------ #

def fread(path):
    """Read a file and return its content as a string"""
    with open(path, 'r') as f:
        return f.read()

def fwrite(path, data: str):
    """Write a string to a file"""
    with open(path, 'w') as f:
        f.write(data)


# ------------------------------------------------------------ #
# misc user input options
"""
User Input Options
- Mouse locking (lock mouse to center of screen)
- Mouse sensitivity (how fast the mouse moves)
- Keybinds (change keybinds)
"""
# ------------------------------------------------------------ #

class MouseLocking(scene.Aspect):
    def __init__(self, lockx:float, locky: float, locked: bool = True, hide_mouse: bool = True):
        super().__init__(None)
        self._priority = 100
        # private
        self._lock_position = (lockx, locky)
        self._hide_mouse = False
        self.hidden = hide_mouse

        # public
        self.locked = locked
        self.delta = [0, 0]
    
    @property
    def hidden(self):
        """Is the mouse hidden?"""
        return self._hide_mouse
    
    @hidden.setter
    def hidden(self, value: bool):
        """Set the mouse hidden"""
        self._hide_mouse = value
        pygame.mouse.set_visible(not self._hide_mouse)

    def update(self):
        """Update the mouse locking"""
        if self.locked:
            mpos = SORA.get_mouse_abs()
            self.delta = [(mpos[0] - self._lock_position[0] * SORA.WSIZE[0]) / SORA.WSIZE[0], 
                            (mpos[1] - self._lock_position[1] * SORA.WSIZE[1]) / SORA.WSIZE[1]]
            pygame.mouse.set_pos((self._lock_position[0] * SORA.WSIZE[0], self._lock_position[1] * SORA.WSIZE[1]))
        else:
            self.delta = [0, 0]


