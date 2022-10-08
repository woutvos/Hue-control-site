lights_example = [
    {
        "id": 1,
        "name": "TV",
        "status": True,
        "brightness": 170,
        "colormode": "xy",
        "hex": "ffbd56",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
    {
        "id": 2,
        "name": "Desk",
        "status": True,
        "brightness": 254,
        "colormode": "xy",
        "hex": "ffcf78",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
    {
        "id": 3,
        "name": "Seat",
        "status": True,
        "brightness": 200,
        "colormode": "xy",
        "hex": "ffbd56",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
    {
        "id": 4,
        "name": "Bed",
        "status": True,
        "brightness": 130,
        "colormode": "xy",
        "hex": "ffbd56",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
    {
        "id": 5,
        "name": "Door",
        "status": True,
        "brightness": 254,
        "colormode": "xy",
        "hex": "ffcf78",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
    {
        "id": 6,
        "name": "Kitchen table",
        "status": True,
        "brightness": 254,
        "colormode": "xy",
        "hex": "ffcf78",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
    {
        "id": 7,
        "name": "Countertop",
        "status": False,
        "brightness": 254,
        "colormode": "xy",
        "hex": "ffcf78",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
    {
        "id": 8,
        "name": "Sofa",
        "status": True,
        "brightness": 200,
        "colormode": "xy",
        "hex": "ffbd56",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
    {
        "id": 9,
        "name": "TV cabinet",
        "status": False,
        "brightness": 100,
        "colormode": "xy",
        "hex": "ffbd56",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
    {
        "id": 10,
        "name": "Storage cabinet",
        "status": False,
        "brightness": 254,
        "colormode": "xy",
        "hex": "ffcf78",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
]

groups_example = [
    {
        "id": 1,
        "name": "All",
        "lights": {
            "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "name": ["TV", "Desk", "Seat", "Bed", "Door", "Kitchen table", "Countertop", "Sofa", "TV cabinet", "Storage cabinet"],
        },
        "type": "LightGroup",
        "state": {
            "all_on": False,
            "any_on": True
        },
        "average_brightness": 227,
    },
    {
        "id": 2,
        "name": "Bedroom",
        "lights": {
            "id": [1, 2, 3, 4, 5],
            "name": ["TV", "Desk", "Seat", "Bed", "Door"],
        },
        "type": "LightGroup",
        "state": {
            "all_on": False,
            "any_on": True
        },
        "average_brightness": 202,
    },
    {
        "id": 3,
        "name": "Living room",
        "lights": {
            "id": [8, 9],
            "name": ["Sofa", "TV cabinet"],
        },
        "type": "LightGroup",
        "state": {
            "all_on": True,
            "any_on": True
        },
        "average_brightness": 150,
    },
    {
        "id": 4,
        "name": "Kitchen",
        "lights": {
            "id": [6, 7],
            "name": ["Kitchen table", "Countertop"],
        },
        "type": "LightGroup",
        "state": {
            "all_on": True,
            "any_on": True
        },
        "average_brightness": 254,
    },
]

bridges_example = (
    {
        "id": "1",
        "internalipaddress": "example"
    },
    {
        "id": "1",
        "internalipaddress": "192.168.1.71"
    },
)