from pathlib import Path
from dotenv import dotenv_values

base_dir    = Path(__file__).resolve().parent.parent.parent
config_file = base_dir / "config" / "mqtt-receiver.env"
config_app  = dotenv_values(config_file)


MQTT_HOST   = config_app.get('HOST')
MQTT_PORT   = config_app.get('PORT')
MQTT_USER   = config_app.get('USER')
MQTT_PASS   = config_app.get('PASS')
MQTT_TOPIC  = config_app.get('TOPIC')
MQTT_CLIENT = config_app.get('CLIENT')
MQTT_LOG    = config_app.get('LOGURL')