import configparser


class ToxIniParser:
    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        return len(self.config.sections())

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        return [
            env.strip()
            for env in self.config["tox"]["envlist"].replace("\n", ",").split(",")
            if env
        ]

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        basepythons = {
            self.config[section]["basepython"]
            for section in self.config.sections()
            if "basepython" in self.config[section]
        }
        return list(basepythons)
