# In this example, we will extend maya with a custom node to add two numbers

#Use python 2 API. Anything under maya.api. uses the 2.0 API. Anything that is maya. uses 1.0 API
import maya.api.OpenMaya as om


def maya_useNewAPI():
    """
    Its not enough to just import modules that use python 2.0 API. We need to let Maya know that this plugin consumes
    and produces objects using the 2.0 API
    This is done by creating this function.
    From Maya 2019 onwards, we can also use a statement instead of this function as the one below
        maya_useNewAPI = True
    :return:
    """
    pass

# We need to define a few variables here. These are used to help with the custom Node that we will create later.

# This is the name of the node and is required. The variable does not need to be the same.
kPluginNodeName = 'addnode'

# type id is a requirement as well and this is an instance of MTypeId
# The value passed to it must be a unique ID
# For development purposes, a range of 0 to hex 7ffff is available.
# for releasing code, you can generate a unique ID by Autodesk. There is a website for doing so. I think we need an account.
kPluginNodeId = om.MTypeId(0x000F7F7F7)


# If you are reading the comments of the code, please scroll down to line 134 where we initialize the function and then
# come back here where we create a custom node

class AddNode(om.MPxNode):
    """
    A custom node that will add two numbers.
    """
    # Create class level variables that will store the created attribute's MObjects.
    # These will be used by the compute method later.
    addend_1 = None
    addend_2 = None
    sum = None

    def __init__(self):
        """
        Constructor
        """
        super(AddNode, self).__init__()

    @classmethod
    def nodeCreator(cls):
        """
        A method to return an instance of the node class. This can be named anything as we pass the name of the
        function or method when registering the node in the initialize plugin function.
        :return:
        """
        return AddNode()

    @classmethod
    def nodeInitializer(cls):
        """
        A function that will initialize all the attributes of the node.
        :return:
        """

        # Creation  of attributes is by using classes derived from MFnAttribute. This is a FunctionSet for
        # dependency Node attributes
        numericAttributeFn = om.MFnNumericAttribute()

        # lets create an attribute using the FunctionSet. We need to specify the long ,short name, attribute type
        # and default value
        cls.addend_1 = numericAttributeFn.create("addend1", "add1", om.MFnNumericData.kDouble, 0.0)
        # we set the keyable property of the function set to True. This then allows the attribute to show up in the
        # channel box and node editor and also sets the attribute to be keyable.
        numericAttributeFn.keyable = True

        # Notice how we are just operating on the function set. This is because the create method of the Function set
        # in the previous line creates an MObject and attaches itself to this function set.

        # Lets create another attribute
        cls.addend_2 = numericAttributeFn.create("addend2", "add2", om.MFnNumericData.kDouble, 0.0)
        numericAttributeFn.keyable = True

        # Lets now create the attribute that stores the result.
        cls.sum = numericAttributeFn.create("sum", "sum", om.MFnNumericData.kDouble, 0.0)
        # As this holds the result, we may not want the attribute to be writable.
        numericAttributeFn.writable = False

        # Now that the attributes are created, lets add these attributes to the node.
        # This is done by calling addAttribute function of MpxNode, which is what the class inherits from.
        cls.addAttribute(cls.addend_1)
        cls.addAttribute(cls.addend_2)
        cls.addAttribute(cls.sum)

        # We also need to let Maya know how these attributes relate to each other.
        # If addend_1 changes, the sum is affected.
        # If addend_2 changes, the sum is again affected.
        # If addend_1 or addend_2 changes, there is no affect to either addend_2 or addend_1
        cls.attributeAffects(cls.addend_1, cls.sum)
        cls.attributeAffects(cls.addend_2, cls.sum)

        # This is the end of the node initializer function. We have created the attributes and have established
        # its types and relationships.

    def compute(self, pPlug, pDataBlock):
        """
        Node computation method.
        :param pPlug: A connection point related to one of our node attributes (could be an input or an output)
        :param pDataBlock: Contains the data on which we will base our computations.
        Data from the input attrs used to calculate and store results in output attrs
        Compute method should only use data local to the node. It should not use data from other nodes or places.
        :return:
        """

        if pPlug == AddNode.sum:
            # We specify the if condition to ensure that the compute method is run only if its the sum attribute that
            # has been marked dirty. This is just to be efficient and we don't maya to run the code here if its any
            # other attribute (addend_1 or addend_2)

            # Using the data block, a data handle can be retrieved to get or set attribute values.
            addend_1_dataBlock_handle = pDataBlock.inputValue(AddNode.addend_1).asDouble()
            addend_2_dataBlock_handle = pDataBlock.inputValue(AddNode.addend_2).asDouble()

            sum = addend_1_dataBlock_handle + addend_2_dataBlock_handle

            # Now, lets get the data block handle for the sum attribute
            sum_dataBlock_handle = pDataBlock.outputValue(AddNode.sum)

            # Using the handle, set the attribute value
            sum_dataBlock_handle.setDouble(sum)

            # Finally, mark the attribute as clean to maya know that.
            sum_dataBlock_handle.setClean()

# Every plugin must have two functions at the very least. A function that initializes the plugin and another function
# that uninitializes the plugin.
# The initializePlugin is the entry point and is called once by Maya.
# It is where we register all nodes , commands, contexts that this plugin creates.
# Maya passes an MObject to this function. More about what an MObject is later.


def initializePlugin(plugin):

    # Let's add the vendor name and version number. This will be used later.
    vendor = "BASE Pipeline"
    version = "1.0"

    # Now we will use the MObject that Maya passes to this function. Before that, a primer about MObjects
    # An MObject is a generic class for accessing any maya object, be it a mesh, camera, light or even a plugin.

    # Just note that when we have an MObject instance, we do not have the actual object but what we have
    # is a handle to the object.

    # This is because Maya always maintains ownership of the objects.
    # This is to avoid accidental deletions or using objects that are already deleted.

    # If you look at the methods available in an MObject class, you would not find much.
    # Here is the link to the reference page - https://download.autodesk.com/us/maya/2011help/api/class_m_object.html

    # This is because we cannot directly operate on an MObject. Operations to an MObject can only be done by attaching
    # it to a Function Set

    # Now, lets get back to the plugin code and interact with the MObject that Maya passed to the function. The next
    # line uses a function set called MfnPlugin. The Mobject can then be attached to this function set.

    # To initialize a plugin function set, we will pass the MObject that we want to attach along with the vendor name
    # and version.
    # You can see the constructor requirements here:
    # https://download.autodesk.com/us/maya/2009help/api/class_m_fn_plugin.html

    plugin_fn = om.MFnPlugin(plugin, vendor, version)

    # We are building this plugin so that we can have a node that can add two numbers.
    # For that we need to register the node that we plan on creating.
    # We can use the registerNode method of the plugin Function set to do so.
    # We wrap this in a try except so that we can catch any issues if Maya is unable to register the Node.
    try:
        plugin_fn.registerNode(kPluginNodeName, kPluginNodeId,
                               AddNode.nodeCreator, AddNode.nodeInitializer,
                               om.MPxNode.kDependNode)
    except:
        om.MGlobal.displayError("Failed to register node: {}".format(kPluginNodeName))


def uninitializePlugin(plugin):
    """
    The uninitializePlugin is the exit point and is called once.
    It deregisters all nodes , commands, contexts.
    A single MObject is passed to it.
    :param plugin:
    :return:
    """

    plugin_fn = om.MFnPlugin(plugin)

    try:
        plugin_fn.deregisterNode(kPluginNodeId)
    except:
        om.MGlobal.displayError("Failed to de-register node: {}".format(kPluginNodeName))


# Now that we have seen how to initialize and uninitialize the plugin, we can look at how to create a custom node.
# Goto line 33


# Load the plugin in maya and create the node using
# cmds.createNode('addnode')
# Then in the node editor, connect the sum to any other node, change the add1 and add2 values to see it in action.