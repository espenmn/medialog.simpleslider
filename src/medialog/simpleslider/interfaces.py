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
    
    tags =  schema.Choice( title = _(u"Or use a Tag"),
    	vocabulary = "plone.app.vocabularies.Keywords", 
    	required=False, 
    )
    
    sort_on = schema.Choice(
            title=_(u"Sort Tags on"),
            values=(
                "sortable_title",
                "created",
                "getObjPositionInParent",
                "id",
                "modified",
                "path",
            ),
    )
    
    sort_order = schema.Choice(
            title=_(u"Sort Order"),
            values=(
                "ascending",
                "descending",
            ),
    )
    
    auto = schema.Bool(
        title=_(u"auto", 
            default=u"Animate automatically"),
        required = False,
        default= True,
    )
    
    speed = schema.Int(
        title=_(u"speed", 
            default=u"Speed of the transition, in milliseconds"),
        required = True,
        default=800
    ) 
    
    timeout = schema.Int(
        title=_(u"timeout", 
            default=u"Time between slide transitions, in milliseconds"),
        required = True,
        default= 4000
    )
    
    pager = schema.Bool(
        title=_(u"pager", 
            default=u"Show pager"),
        required = False,
        default= False,
    )

    nav = schema.Bool(
        title=_(u"nav", 
            default=u"Show navigation"),
        required = False,
        default= False,
    )
    
    random = schema.Bool(
        title=_(u"random", 
            default=u"Randomize the order of the slides"),
        required = False,
        default= False,
    )
    
    pause = schema.Bool(
        title=_(u"pause", 
            default=u"Pause on hover"),
        required = False,
        default= False,
    )
    
    pausecontrols = schema.Bool(
        title=_(u"pausecontrols", 
            default=u"Pause when hovering controls"),
        required = False,
        default= True,
    )
                      
    prevtext = schema.ASCIILine(
        title=_(u"prev_text", 
            default=u"Text for the previous button"),
        required = False,
    )
    
    nexttext = schema.ASCIILine(
        title=_(u"next_text", 
            default=u"Text for the next button"),
        required = False,
    )
    
    maxwidth = schema.Int(
        title=_(u"maxwidth", 
            default=u"Max width"),
        required = False,
        default=800,
    ) 
    
