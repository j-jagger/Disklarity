def wmi_to_dict(obj):
    props = {}
    for prop in obj.properties:
        props[prop] = getattr(obj, prop, None)
    return props
