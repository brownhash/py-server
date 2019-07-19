from yaml import SafeLoader
import yaml

def config_reader():
    stream = open('config.yaml', 'r')
    data = yaml.load(stream, SafeLoader)
    return(data)