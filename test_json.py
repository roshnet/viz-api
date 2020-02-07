def remove_field_from_json():
    data = [
        {
            "name": "Roshan Sharma",
            "username": "roshnet"
        },
        {
            "name": "Roshan Sharma",
            "username": "roshnet"
        },
        {
            "name": "Roshan Sharma",
            "username": "roshnet"
        },
        {
            "name": "Roshan Sharma",
            "username": "roshnet"
        }
    ]
 
    for obj in data:
        obj.pop('name')
    return data

print(remove_field_from_json())
