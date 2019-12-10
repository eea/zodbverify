""" Fix plone.dexterity.schema.generated exception
"""
import logging
from zope.component.hooks import getSiteManager
logger = logging.getLogger("zodbverify")
sm = getSiteManager()

try:
    from plone.dexterity.schema import SchemaModuleFactory
    sm.registerUtility(factory=SchemaModuleFactory, name="plone.dexterity.schema.generated")
except Exception as err:
    logger.exception(err)
else:
    logger.warn("Manually register plone.dexterity.schema.generated utility")
