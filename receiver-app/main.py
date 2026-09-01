import paho.mqtt.client as mqtt
from sfunctions.func import MQTT_TOPIC, MQTT_CLIENT, MQTT_USER, MQTT_PASS, MQTT_HOST, MQTT_PORT

def on_connect(client, userdata, connect_flags, reason_code, properties):
    if reason_code == 0:
        print(f'CONNECTADO')
        client.subscribe(MQTT_TOPIC, qos=1)
        print(f'escuchando topic {MQTT_TOPIC}')
    else:
        print(f'ERROR {reason_code}')


def on_desconnect(client, userdata, disconnect_flags, reason_code, propeties):
    if reason_code != 0:
        print(f'Conexion MQTT perdidida {reason_code}')


def on_message(client, userdata, message):
    try:
        payload = message.payload.decode("utf-8")
        print(f'{message} {payload}')

    except Exception:
        print(f'ERROR {str(message)}')



client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2, client_id=MQTT_CLIENT, protocol=mqtt.MQTTv311)
client.username_pw_set(username=MQTT_USER, password=MQTT_PASS)
client.on_connect = on_connect
client.on_disconnect = on_desconnect
client.on_message = on_message
client.reconnect_delay_set(min_delay=2, max_delay=33)
client.connect_async(host=MQTT_HOST, port=int(MQTT_PORT), keepalive=66)
client.loop_forever(retry_first_connection=True)



