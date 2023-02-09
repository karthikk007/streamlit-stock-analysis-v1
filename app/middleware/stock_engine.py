import logging

from creation_pattern.singletion import SingletonDoubleChecked
from middleware.services.data_source.cache_data_source.app_state_data_source import AppStateDataSource

logger = logging.getLogger('mylogger')

# singleton class, use get instance()
class StockEngine(SingletonDoubleChecked):
    def __init__(self) -> None:
        super().__init__()
        
        self._app_state_data_source = AppStateDataSource()
        
        logger.error('called init...')
        
    @property
    def app_state_data_source(self):
        return self._app_state_data_source
