from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import (
    INonInstallable as INonInstallableProducts
)
from Products.CMFPlone.interfaces import (
    INonInstallable as INonInstallableProfiles
)
import logging
from zope.i18nmessageid import MessageFactory

MessageFactory = ibwtpaullaplonesiteMessageFactory = MessageFactory('ibwt.paullaplonesite')
logger = logging.getLogger('ibwt.paullaplonesite')
EXTENSION_PROFILES = ('ibwt.paullaplonesite:default',)
SKIN = 'ibwt.skin'
HIDDEN_PRODUCTS = [u'NuPlone']
HIDDEN_PROFILES = [u'NuPlone']

PRODUCT_DEPENDENCIES = (
)


class HiddenProducts(object):
    implements(INonInstallableProducts)

    def getNonInstallableProducts(self):
        return HIDDEN_PRODUCTS


class HiddenProfiles(object):
    implements(INonInstallableProfiles)

    def getNonInstallableProfiles(self):
        return [u'NuPlone']


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


GLOBALS = globals()
