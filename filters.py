def filter_by_role_name(content, role_name):
    return [x for x in content if x["role"] == role_name]

def filter_by_location(content, location):
    return [x for x in content if x["meeting_location"] == location]