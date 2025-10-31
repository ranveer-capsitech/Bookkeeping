import configparser



class ConfigReader:
    def __init__(self, config_file_path):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)

    def get_value(self, section, key):
        return self.config.get(section, key)

    