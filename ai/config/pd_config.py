import os
from urllib.parse import urlencode, urlunparse
from ai.common.decorators import singleton
from sqlalchemy import create_engine, Engine


@singleton
class Database:
    """
    Database configuration class.
    """

    def __init__(self):
        self.url = self.config_db()

    def config_db(self):
        db_protected = os.getenv('DB_PROTECTED_URL')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_user = os.getenv('DB_USERNAME')
        db_pwd = os.getenv('DB_PASSWORD')
        db_name = os.getenv("DB_NAME")
        db_driver = os.getenv("DB_DRIVER")
        db_schema = os.getenv("DB_SCHEMA")
        db_ssl = os.getenv("DB_SSL")
        # base_url = f"{db_protected}://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}"
        param = {}
        if db_driver is not None:
            param['driver'] = db_driver

        if db_ssl is not None:
            param['TrustServerCertificate'] = db_ssl

        if db_schema is not None:
            param['options'] = '-csearch_path=qa,public'

        return urlunparse(
            (db_protected, f"{db_user}:{db_pwd}@{db_host}:{db_port}", f"/{db_name}", '', urlencode(param), ''))

    def create_engine(self) -> Engine:
        """
        Create a new engine instance.
        """
        return create_engine(self.url)
