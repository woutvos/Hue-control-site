from phue import Bridge
from dotenv import load_dotenv
from rgbxy import Converter
import requests
import sqlite3
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    filename='app.log', filemode='w',
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)


# Basic configuration
converter = Converter()
DB_PATH = 'settings.db'
logging.info(f'Using: {DB_PATH}')

# Load environment variables
load_dotenv()
logging.info('Loaded dotenv')


# connect to the latest used bridge
def connect_to_latest_bridge():
    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Get the bridge ip
    c.execute("SELECT value FROM settings WHERE setting = 'bridge_ip'")
    bridge_ip = c.fetchone()[0]
    logging.info(f'Ip fetched from database: {bridge_ip}')

    # Close connection
    conn.close()

    # Check to use example data
    if bridge_ip == 'example':
        b = 'example'

    else:
        # Connect to bridge
        b = Bridge(bridge_ip)
        b.connect()

        # Get the api
        b.get_api()
        logging.info('Connected to bridge')

    return b


# Get current bridge ip
def get_current_bridge_ip():
    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Get the bridge ip
    c.execute("SELECT value FROM settings WHERE setting = 'bridge_ip'")
    bridge_ip = c.fetchone()[0]

    # Close connection
    conn.close()

    logging.info(f'Current bridge ip: {bridge_ip}')
    return bridge_ip


# Update bridge ip in database
def update_bridge_ip(bridge_ip):
    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Update bridge ip
    c.execute("UPDATE settings SET value = ? WHERE setting = 'bridge_ip'", (bridge_ip,))

    # Save changes
    conn.commit()

    # Close connection
    conn.close()

    logging.info(f'Bridge ip updated to: {bridge_ip}')


# Get bridges
def get_bridges():
    #r = requests.get('https://discovery.meethue.com/')
    #bridges = r.json()

    #bridges.append({'id': 'example', 'internalipaddress': 'example'})

    bridges = [{'id': '1', 'internalipaddress' : '192.168.1.71'}, {'id': '2', 'internalipaddress' : 'example'}]

    logging.info(f'Found {len(bridges)} bridges: {bridges}')
    return bridges


# Function to get the lights and store them in a list
def get_lights(b):
    if b == 'example':
        logging.info('Using example data for lights')
        lights_list = [{'id': 1, 'name': 'Test', 'status': True, 'brightness': 144, 'colormode': 'xy', 'hue': 7675, 'saturation': 199, 'xy': [0.5016, 0.4151], 'colortemp': 443, 'effect': 'none', 'alert': 'select', 'reachable': True, 'type': 'Extended color light'}, {'id': 2, 'name': 'Kast', 'status': True, 'brightness': 144, 'colormode': 'xy', 'hue': 7675, 'saturation': 199, 'xy': [0.5016, 0.4151], 'colortemp': 443, 'effect': 'none', 'alert': 'select', 'reachable': True, 'type': 'Extended color light'}, {'id': 3, 'name': 'Bed achter', 'status': True, 'brightness': 144, 'colormode': 'xy', 'hue': 7675, 'saturation': 199, 'xy': [0.5016, 0.4151], 'colortemp': 443, 'effect': 'none', 'alert': 'select', 'reachable': True, 'type': 'Extended color light'}, {'id': 4, 'name': 'Setup', 'status': True, 'brightness': 144, 'colormode': 'xy', 'hue': 7675, 'saturation': 199, 'xy': [0.5016, 0.4151], 'colortemp': 443, 'effect': 'none', 'alert': 'select', 'reachable': True, 'type': 'Extended color light'}, {'id': 5, 'name': 'Vloer', 'status': True, 'brightness': 144, 'colormode': 'xy', 'hue': 7675, 'saturation': 199, 'xy': [0.5016, 0.4151], 'colortemp': 443, 'effect': 'none', 'alert': 'select', 'reachable': True, 'type': 'Extended color light'}, {'id': 7, 'name': 'Bed zijkant', 'status': True, 'brightness': 144, 'colormode': 'xy', 'hue': 13523, 'saturation': 200, 'xy': [0.5017, 0.4152], 'colortemp': 443, 'effect': 'none', 'alert': 'select', 'reachable': True, 'type': 'Extended color light'}]

    else:
        # Get the lights
        lights_list = []
        lights_raw = b.lights

        # Get the lights info and put it in a list
        for l in lights_raw:
            lights_list.append(
                {
                    'id': l.light_id,
                    'name': l.name,
                    'status': l.on,
                    'brightness': l.brightness,
                    'colormode': l.colormode,
                    'hue': l.hue,
                    'saturation': l.saturation,
                    'xy': l.xy,
                    'hex': converter.xy_to_hex(l.xy[0], l.xy[1]),
                    'colortemp': l.colortemp,
                    'effect': l.effect,
                    'alert': l.alert,
                    'reachable': l.reachable,
                    'type': l.type
                },
            )

        logging.info(f'Found {len(lights_list)} lights')
    return lights_list


# Function to turn on the lights
def light_on(b, light_id):
    b.set_light(light_id, 'on', True)
    logging.info(f'Light {light_id} turned on')


# Function to turn off the lights
def light_off(b, light_id):
    b.set_light(light_id, 'on', False)
    logging.info(f'Light {light_id} turned off')


# Funtion to change the brightness
def set_light_brightness(b, light_id, brightness):
    b.set_light(light_id, 'bri', brightness)
    logging.info(f'Light {light_id} brightness set to {brightness}')


# Function to change the color
def set_light_color(b, light_id, color):
    # Convert the color to xy
    color = color.lstrip('#')
    xy = converter.hex_to_xy(color)
    logging.debug(f'Color {color} converted to xy: {xy}')

    # Set the color
    b.set_light(light_id, 'xy', xy)
    logging.info(f'Light {light_id} color set to {color}')


# Function to get the light name by id
def get_light_names(light_id, lights):
    # Get the name of the light
    for l in lights:
        if l['id'] == light_id:
            return l['name']


# Function to get the groups
def get_groups(b):
    if b == 'example':
        logging.info('Using example data for groups')
        groups_example = [{'id': 1, 'name': 'All', 'lights': {'id': [3, 4, 5, 7], 'name': ['Lamp1', 'Lamp2', 'Lamp3', 'Lamp4']}, 'type': 'LightGroup', 'state': {'all_on': True, 'any_on': True}}, {'id': 2, 'name': 'Groep 1', 'lights': {'id': [1, 2, 3, 4], 'name': ['Lamp1', 'Lamp2', 'Lamp3', 'Lamp4']}, 'type': 'LightGroup', 'state': {'all_on': True, 'any_on': True}}, {'id': 3, 'name': 'Groep 2', 'lights': {
            'id': [1, 2], 'name': ['Lamp1', 'Lamp2']}, 'type': 'LightGroup', 'state': {'all_on': True, 'any_on': True}}, {'id': 4, 'name': 'Groep 3', 'lights': {'id': [1, 2], 'name': ['Lamp1', 'Lamp2']}, 'type': 'LightGroup', 'state': {'all_on': True, 'any_on': True}}, {'id': 5, 'name': 'Groep 4', 'lights': {'id': [1, 2], 'name': ['Lamp1', 'Lamp2']}, 'type': 'LightGroup', 'state': {'all_on': True, 'any_on': True}}]
        return groups_example

    logging.info('Getting groups')

    # Get the groups
    groups_list = []
    groups_raw = b.get_group()
    lights = get_lights(b)

    # Get the groups info and put it in a list
    for g in groups_raw:
        groups_list.append(
            {
                'id': g,
                'name': groups_raw[g]['name'],
                'lights': {
                    'id': groups_raw[g]['lights'],
                    'name': [get_light_names(l, lights) for l in [eval(i) for i in groups_raw[g]['lights']]]
                },
                'type': groups_raw[g]['type'],
                'state': groups_raw[g]['state'],
            },
        )

    logging.info(f'Found {len(groups_list)} groups')

    return groups_list
