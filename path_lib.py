"""
路径处理
"""
from pathlib import Path

PATH_ROOT: Path = Path(__file__).parent
PATH_RAW_AUDIO: Path = PATH_ROOT / "audio" / "raw"
PATH_PROCESSED_AUDIO: Path = PATH_ROOT / "audio" / "processed"
