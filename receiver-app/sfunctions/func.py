from pathlib import Path
from dotenv import dotenv_values

base_dir    = Path(__file__).resolve().parent.parent.parent
config_file = base_dir / "config" / "mqtt-receiver.env"
config_app  = dotenv_values(config_file)