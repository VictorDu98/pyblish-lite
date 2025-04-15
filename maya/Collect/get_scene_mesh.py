import os
import pyblish.api as pyblish

class getSceneMesh(pyblish.ContextPlugin):
    """Gather all mesh from current maya scene"""
    hosts = ["maya"]
    order = pyblish.CollectorOrder

    def process(self, context):

        from maya import cmds
        shapes= cmds.ls(g=1)
        #FOR shape IN SHAPES
            # REMOVE
        assert len(shapes)>0,"No mesh!"
        for shape in shapes:
            instance = context.create_instance(shape)
            instance.data["family"] = "mesh"

