from phue import Bridge
from rgbxy import Converter
import requests
import sqlite3
import logging
import examples

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


def connect_to_latest_bridge():
    """Connect to the latest used bridge"""
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


def get_current_bridge_ip():
    """Get the ip from the bridge that is currently connected"""
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


def update_bridge_ip(bridge_ip):
    """Update the bridge ip to the database"""
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


def get_bridges():
    """Get all the bridges in the network."""
    #r = requests.get('https://discovery.meethue.com/')
    #bridges = r.json()

    #bridges.append({'id': 'example', 'internalipaddress': 'example'})
    bridges = examples.bridges_example

    logging.info(f'Found {len(bridges)} bridges: {bridges}')
    return bridges


def get_lights(b):
    """Get all the lights"""	
    if b == 'example':
        logging.info('Using example data for lights')
        lights_list = examples.lights_example

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


def light_on_off(b, light_id, state):
    """Turn light on and off"""
    if state == 'on':
        b.set_light(light_id, 'on', True)
        logging.info(f'Light {light_id} turned on')

    elif state == 'off':
        b.set_light(light_id, 'on', False)
        logging.info(f'Light {light_id} turned off')


def set_light_brightness(b, light_id, brightness):
    """Set the brightness of the light"""
    b.set_light(light_id, 'bri', brightness)
    logging.info(f'Light {light_id} brightness set to {brightness}')


def set_light_color(b, light_id, color):
    """Set the color of the light"""
    # Convert the color to xy
    color = color.lstrip('#')
    xy = converter.hex_to_xy(color)
    logging.debug(f'Color {color} converted to xy: {xy}')

    # Set the color
    b.set_light(light_id, 'xy', xy)
    logging.info(f'Light {light_id} color set to {color}')


def get_light_names(light_id, lights):
    """Get the id's of the lights and their corresponding names"""
    # Get the name of the light
    for l in lights:
        if l['id'] == light_id:
            return l['name']


def get_groups(b):
    """Get all the groups"""
    if b == 'example':
        logging.info('Using example data for groups')
        groups_example = examples.groups_example
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


def group_on_off(b, group_id, state):
    """Turn group on and off"""
    if state == 'on':
        b.set_group(group_id, 'on', True)
        logging.info(f'Group {group_id} turned on')

    elif state == 'off':
        b.set_group(group_id, 'on', False)
        logging.info(f'Group {group_id} turned off')