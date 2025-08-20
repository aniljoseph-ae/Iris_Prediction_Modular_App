from pathlib import Path

project_structure = {
    "config": {
        "__init__.py": None,
        "config.yaml": None,
        "config.py": None,
        "schema.py": None
    },
    "data": {},
    "model": {},
    "src": {
        "__init__.py": None,
        "data_loader.py": None,
        "preprocessing.py": None,
        "pipeline.py": None,
        "model.py": None,
        "inference.py": None,
    },
    "train": {
        "__init__.py": None,
        "training.py": None,
        "evaluating.py": None,
    },
    "utils": {
        "__init__.py": None,
        "eval_utils.py": None,
        "io_utils.py": None,
        "setup_project.py": None
    },
    "requirements.txt": None,
    "main.py": None,
    "README.md": None,
    ".gitignore": None
}


def create_structure(base_path: Path, project_structure: dict):
    for name, content in project_structure.items():
        path = base_path / name
    
        if content is None:
            path.parent.mkdir(parents = True, exist_ok = True)
            path.touch(exist_ok = True)
            print(f"Created file: {path}")
        else:
            path.mkdir(parents = True, exist_ok = True)
            print(f"Create directory: {path}")
            create_structure(path, content)


def find_root_dir_git(path):
    while path.parent != path:
        if (path / ".git").exists() or (path / ".project_root").exists():
            return path
        path = path.parent
    return path

if __name__ == "__main__":
    CURRENT_DIR = Path(__file__).resolve().parent
    ROOT_DIR = find_root_dir_git(CURRENT_DIR)
    print(f"Creating projectstructure in : {ROOT_DIR}")
    create_structure(ROOT_DIR, project_structure)
