from middleware.services.data_source.cache_data_source.cache.app_state_cache import AppStateCache


class AppStateDataSource(object):
    def __init__(self) -> None:
        self.app_state_cache = AppStateCache()

    def update(self, page_name, state_dict):
        dict = self.app_state_cache.cache
        inner_dict = self.app_state_cache.cache.get(page_name)

        if inner_dict is None:
            dict[page_name] = state_dict
        else:
            for key, value in state_dict.items():
                inner_dict[key] = value
            
            dict[page_name] = inner_dict
        
        self.app_state_cache.update_cache(dict)

    def get(self, page_name):
        return self.app_state_cache.cache.get(page_name)

    def clear(self, page_name):
        if self.app_state_cache.cache.get(page_name):
            del self.app_state_cache.cache[page_name]
            self.app_state_cache.save_cache()

    def clear_all(self):
        dict = {}
        self.app_state_cache.update_cache(dict)