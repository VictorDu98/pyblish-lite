import os
import pyblish.api as pyblish


class ValidateSuffixGeo(pyblish.InstancePlugin):
    hosts = ["maya"]
    families = ["mesh"]
    order = pyblish.ValidatorOrder

    def process(self, instance):
        assert str(instance).endswith('_geo'),"%s is not ending with _geo" % instance