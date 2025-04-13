import os
import pyblish.api as pyblish


class MyCollector(pyblish.ContextPlugin):
    """This plug-in identifies content and creates instances,alsooo hello """

    order = pyblish.CollectorOrder

    def process(self, context):
        for folder in os.listdir("."):
            if not folder.endswith("_asset"):
                continue
            instance = context.create_instance(folder)
            instance.data["family"] = "asset"

class ValidateContents(pyblish.InstancePlugin):
    """Ensure rig has the appropriate object sets"""

    order = pyblish.ValidatorOrder
    families = ["asset"]

    def process(self, instance):
        self.log.info("Extracting: %s" % instance)
        #assert "controls_SEL" in instance, "%s is missing a controls set" % instance
        #assert "pointcache_SEL" in instance, "%s is missing a pointcache set" % instance
