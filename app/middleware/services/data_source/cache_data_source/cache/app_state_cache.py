from middleware.services.data_source.cache_data_source.cache.cache import Cache


class AppStateCache(Cache):
    name = 'app_state_cache'
    dir_path = 'app/middleware/services/data_source/cache_data_source/cache/.app_state/.{}'.format(name)
    file_name = '{}.json'.format('app_state')

    def __init__(self) -> None:
        super().__init__()