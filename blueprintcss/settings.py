from ragendja.settings_post import settings
settings.add_app_media('combined-%(LANGUAGE_DIR)s.css',
    'blueprintcss/reset.css',
    'blueprintcss/typography.css',
    'blueprintcss/forms.css',
    'blueprintcss/grid.css',
    'blueprintcss/lang-%(LANGUAGE_DIR)s.css',
)
settings.add_app_media('combined-print-%(LANGUAGE_DIR)s.css',
    'blueprintcss/print.css',
)
settings.add_app_media('ie.css',
    'blueprintcss/ie.css',
)
