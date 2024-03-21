import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/config.ini")

class ReadConfig:

    @staticmethod
    def get_basr_uri():
        base_uri = config.get('common_info', 'BASE_URI')
        return base_uri

    @staticmethod
    def get_covid_tracker_host():
        covid_tracker_host = config.get('common_info', 'COVID_TRACKER_HOST')
        return covid_tracker_host


