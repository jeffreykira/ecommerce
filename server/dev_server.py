
try:
    import logging.config
    from ecommerce import logging_config
    from ecommerce import app_config
    from ecommerce import main

    app_config.CONFIG = app_config.DevelopmentConfig
    logging.config.dictConfig(logging_config.DEV)

    main.init(app_config.CONFIG)
except Exception:
    import traceback
    traceback.print_exc()
