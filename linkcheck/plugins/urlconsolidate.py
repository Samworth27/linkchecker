from . import _ParserPlugin
from .. import log, LOG_PLUGIN


class URLConsolidate(_ParserPlugin):
    def __init__(self, config)->None:
        super().__init__(config)
        log.warn(LOG_PLUGIN, _("CONSOLIDATE PLUGIN ACTIVE"))

    def check(self, url_data):
        log.error(LOG_PLUGIN, "URL CONS")