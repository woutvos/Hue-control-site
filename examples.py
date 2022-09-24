lights_example = [
    {
        "id": 1,
        "name": "Tv",
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
        "name": "Bureau",
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
        "name": "Bank",
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
        "status": False,
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
        "name": "Deur",
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
        "id": 6,
        "name": "Keukentafel",
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
        "name": "Aanrecht",
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
        "id": 8,
        "name": "Bank",
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
        "name": "Tv meubel",
        "status": True,
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
        "name": "Opbergkast",
        "status": False,
        "brightness": 256,
        "colormode": "xy",
        "hex": "ffcf78",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
    {
        "id": 11,
        "name": "Gang",
        "status": False,
        "brightness": 200,
        "colormode": "xy",
        "hex": "ffbd56",
        "effect": "none",
        "alert": "select",
        "reachable": True,
        "type": "Extended color light",
    },
]

groups_example = [
    {
        "id": 1,
        "name": "Alles",
        "lights": {
            "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "name": ["Tv", "Bureau", "Bank", "Bed", "Deur"],
        },
        "type": "LightGroup",
        "state": {
            "all_on": False,
            "any_on": True
        },
    },
    {
        "id": 1,
        "name": "Slaapkamer",
        "lights": {
            "id": [1, 2, 3, 4, 5],
            "name": ["Tv", "Bureau", "Bank", "Bed", "Deur"],
        },
        "type": "LightGroup",
        "state": {
            "all_on": False,
            "any_on": True
        },
    },
    {
        "id": 3,
        "name": "Woonkamer",
        "lights": {
            "id": [8, 9],
            "name": ["Bank", "Tv meubel"]
        },
        "type": "LightGroup",
        "state": {
            "all_on": True,
            "any_on": True
        },
    },
    {
        "id": 4,
        "name": "Keuken",
        "lights": {
            "id": [6, 7],
            "name": [
                "Keukentafel",
                "Aanrecht",
            ],
        },
        "type": "LightGroup",
        "state": {
            "all_on": True,
            "any_on": True
        },
    },
]

bridges_example = (
    {
        "id": "1",
        "internalipaddress": "example"
    },
    {
        "id": "2",
        "internalipaddress": "example2"
    },
    {
        "id": "1",
        "internalipaddress": "192.168.1.71"
    },
)
