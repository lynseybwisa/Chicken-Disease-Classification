from dataclasses import dataclass
from pathlib import Path

# The @dataclass decorator automatically generates special methods, such as __init__. 
# The frozen=True argument makes instances of the class immutable (read-only),
# which means that once an instance is created, its attributes cannot be changed.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path