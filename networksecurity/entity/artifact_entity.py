from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    trained_path_dir:str
    test_path_dir:str