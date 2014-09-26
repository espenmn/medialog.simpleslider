from zope.interface import Interface
from zope import schema
from medialog.simpleslider import simplesliderMessageFactory  as _
from OFS.interfaces import IItem

 
from zope.component import getMultiAdapter
  
class ISimplesliderLayer(Interface):
    """
    marker interface for simpleslider layer
    
    """
    
class ISimpleslider(Interface):
    """
    marker interface for content types that can use the viewlet 
    """

    
class ISimplesliderUtilProtected(Interface):

    def enable():
        """
        enable simpleslider on this object
        """

    def disable():
        """
        disable simpleslider on this object
        """


class ISimplesliderUtil(Interface):

    def enabled():
        """
        checks if simpleslider is enabled  
        """

    def view_enabled():
        """
        checks if the simpleslider is selected
        """

class ISimplesliderSettings(Interface):
    """
    The actual simpleslider settings
    here we define the image urls
    """
    
    imagepaths = schema.TextLine(
        title=_(u"image_url", 
            default=u"path to images"),
            required = False,
    )
    
    tags =  schema.Choice( title = _(u"Or used Tag"),
    	vocabulary = "plone.app.vocabularies.Keywords", 
    	required=False, 
    )
    