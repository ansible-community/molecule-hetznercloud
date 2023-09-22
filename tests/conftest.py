from __future__ import annotations

import os
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def change_dir(path: Path):
    previous_path = Path.cwd()

    os.chdir(path)
    yield
    os.chdir(previous_path)
