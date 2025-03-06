from pathlib import Path


def display_tree(path: Path, indent: str = "") -> None:
    print(indent + str(path.name))

    if path.is_dir():
        for child in path.iterdir():
            display_tree(child, indent + "    ")


if __name__ == "__main__":
    root = Path("goit-algorithms")
    display_tree(root)
