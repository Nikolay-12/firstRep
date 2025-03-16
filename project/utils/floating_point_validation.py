def is_valid_floating_point(new_value: str):
    if len(new_value) == 0:
        return True
    new_value = new_value.replace(",", ".")
    try:
        float(new_value)
    except:
        return False
    else:
        return True
