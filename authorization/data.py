import configparser


class Config:
    username = None
    password = None

    def read_config(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)
        return config
