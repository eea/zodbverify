""" Fix plone.dexterity.schema.generated exception
"""
try:
    from eea import aliases
except ImportError:
    # eea.aliases not present
    pass
