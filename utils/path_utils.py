# ./utils/path_utils

import sys, os
from pathlib import Path
from functools import lru_cache


@lru_cache(max_size=1)
def find_root_dir(start: Path | None = None) -> Path:
    """
    find the project root based on the manin .git file(s) or .project_root file
    - it uses lru_cache decoorator for caching the root dir
    """
    if start is None:
        start = Path(__file__).resolve().parent

    for parent in [start, *start.parents]:
        if (parent / ".git" / "HEAD").exists() or (parent / ".project_root").exists():
            return parent
    raise RuntimeError("No project root found (.git or .project_root missing).")


def resolve_root() -> Path:
    """ to add root to syestem path and changing cwd to root"""
    root = find_root_dir()
    if str(root) not in sys.path:
        # add root to system path
        sys.path.append(str(root))
    # change cwd to root
    os.chdir(root)

    return root

def get_path(*subdir: str) -> Path:
    return find_root_dir().joinpath(*subdir)

