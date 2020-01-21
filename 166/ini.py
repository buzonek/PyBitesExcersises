import configparser
import re


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
        envs = re.split(r'[,\n]', self.config['tox']['envlist'])
        return [x.strip() for x in envs if x]

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        pythons = set()
        for section in self.config.sections():
            python = self.config[section].get('basepython', None)
            if python:
                pythons.add(python)
        return pythons