from zope.interface import Interface, Attribute
from zope import schema
from medialog.simpleslider import simplesliderMessageFactory  as _
from OFS.interfaces import IItem

from plone.memoize.instance import memoize

 
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
    """
    
    gallerypath = schema.TextLine(
        title=_(u"label_width_title_simpleslider_setting", default=u"Which Gallery"),
        description=_(u"label_width_description_simpleslider_setting", 
        default=u"The path to the gallery you want to  show."),
        required=True)
