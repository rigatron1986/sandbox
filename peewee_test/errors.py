import logging

from peewee_main.cpeewee import DoesNotExist


class CException(Exception):
    """Facility-wide base class for exceptions. This should be subclassed."""


logger = logging.getLogger(__name__)
logger.debug("loading module {0} at {1}".format(__name__, __file__))


class EntityNotFound(CException, DoesNotExist):
    def __init__(self, entity):
        super(EntityNotFound, self).__init__(
            u"The following entity doesn't exist:\n    \"{0}\"".format(entity))


class NoSuchVersionInAsset(CException, DoesNotExist):
    def __init__(self, version, asset):
        if len(asset.entities) == 0:
            entities = '<nothing>'
        else:
            entities = u"   ".join([e.name for e in asset.entities])
        super(NoSuchVersionInAsset, self).__init__(
            (u"A version with the name:\n" +
             u"    \"{0}\"\n" +
             u"doesn't exist in the asset:\n" +
             u"    {1}\n" +
             u"that is attached to :\n" +
             u"    {2}").format(version, asset.name, entities)
        )


class NoSuchAssetInEntity(CException, DoesNotExist):
    def __init__(self, asset, entity):
        super(NoSuchAssetInEntity, self).__init__(
            (u"An asset with the name:\n" +
             u"    \"{0}\"\n" +
             u"doesn't exist in:\n" +
             u"    {1}").format(asset, entity.get_full_name()))


class VersionAlreadyExists(CException):
    def __init__(self, version, asset):
        super(VersionAlreadyExists, self).__init__(
            (u"An version with the name:\n" +
             u"    \"{0}\"\n" +
             u"already exists in:\n" +
             u"    {1}: {2}").format(version, asset.name, asset.get_full_directory()))


class AssetAlreadyExists(CException, DoesNotExist):
    def __init__(self, asset, entity):
        self.asset = asset
        super(AssetAlreadyExists, self).__init__(
            (u"An asset with the name:\n" +
             u"    \"{0}\"\n" +
             u"already exists in:\n" +
             u"    {1}").format(asset.name, entity))
