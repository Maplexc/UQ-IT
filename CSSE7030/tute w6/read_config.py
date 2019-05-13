def read_config(file_name):
    """

    Parameter:
        file_name (str)

    ...
    """
    config = {}
    notification = {}
    valid = True
    file = open(file_name, 'r')
    for line in file:
        line = line.strip()
        if '=' not in line:
            if '[' not in line and ']' not in line:
                raise ValueError
        if '=' in line:
            info = line.split('=')
            key = info[0]
            if key == 'email' or key == 'sms':
                notification[key] = info[1]
            else:
                config[key] = info[1]
    config['notifications'] = notification
    return config

from pprint import pprint
# using it: pprint(

def read_config_anss(filename):
    config = {}

    with open(filename,'r') as file:
        for line in file:
            # is it a head, is it a property?
            line = line.strip()
            if line.startswith('[') and \
               line.endswith(']'):
                # heading
                heading = [1,-1] # remove []
                config[heading] = {}
            else:
                # property
                key, _, value = line.partition('=')
                config[heading][key] = value
                
                
            

            

    return config


def get_value(config, name_of_setting):
    """

    Parameter:
        config (dict)
        name_of_setting (str)

    ...
    """
    keys = name_of_setting.split('.')
    if keys[0] == 'user':
        value = config[keys[1]]
    else:
        notification = config[keys[0]]
        value = notification[keys[1]]
    return value

        
        
