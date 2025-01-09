from . import _ConnectionPlugin
from .. import log, LOG_PLUGIN


class URLConsolidate(_ConnectionPlugin):
    def __init__(self, config)->None:
        super().__init__(config)
        log.warn(LOG_PLUGIN, _("CONSOLIDATE PLUGIN ACTIVE"))

    def applies_to(self, url_data):
        return True

    def check(self, url_data):
        url_data.warning(str(url_data))
        log.error(LOG_PLUGIN, str(url_data))