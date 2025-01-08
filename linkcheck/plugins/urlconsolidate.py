from . import _ParsePlugin
from .. import log, LOG_PLUGIN


class URLConsolidate(_ParsePlugin):
    def __init__(self, config)->None:
        super().__init__(config)
        log.warn(LOG_PLUGIN, _("CONSOLIDATE PLUGIN ACTIVE"))