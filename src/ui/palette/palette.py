from dataclasses import dataclass


@dataclass(frozen=True)
class Palette:
    FRAME_BG: str = "#333A40"
    HIGHLIGHT: str = "#00BFA5"
    TEXT_FG: str = "#EAEAEA"
    BUTTON_BG: str = "#4C545C"
    BUTTON_FG: str = "#181616"
    ENTRY_BG: str = "#2C3136"
    ENTRY_FG: str = TEXT_FG
