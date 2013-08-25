class Conf(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

    def load(self, settings_module='base'):
        from importlib import import_module
        settings_module = import_module('.{module}'.format(module=settings_module), __package__)
        self.update(settings_module.__dict__)


def setup_settings(pull_options=True):

    from tornado.log import enable_pretty_logging
    from tornado.options import options

    options.define('settings', default='base', help='Define settings module')

    def parse_callback():
        global settings
        settings.load(options.settings)

        if pull_options:
            # let's pull options from the settings
            for option_name in options:
                if option_name in settings:
                    setattr(options, option_name, settings[option_name])
            # resets logging configuration
            enable_pretty_logging()

    options.add_parse_callback(callback=parse_callback)


settings = Conf()
__all__ = ['settings', 'setup_settings']
