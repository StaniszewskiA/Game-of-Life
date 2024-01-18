from dataclasses import dataclass

try:
    import tomllib
except ImportError:
    import tomli as tomlib

@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]

    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )

