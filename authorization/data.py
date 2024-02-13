import configparser


class Config:
    config = None

    def read_config(self, filename):
        self.config = configparser.ConfigParser()
        self.config.read(filename)
        return self.config
