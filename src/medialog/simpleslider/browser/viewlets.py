from Acquisition import aq_inner
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implements, Interface
from Products.CMFCore.utils import getToolByName

from medialog.simpleslider import simplesliderMessageFactory as _
from medialog.simpleslider.settings import SimplesliderSettings
from medialog.simpleslider.settings import ISimplesliderSettings
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter

from AccessControl import getSecurityManager


class SliderViewlet(ViewletBase):
    render = ViewPageTemplateFile('simpleslider.pt')
    
    implements(ISimplesliderSettings)
    

    
    def update(self):
        super(SliderViewlet, self).update()
        
        #XXX the order in which these are called is important!
        self.images = self.get_images()
        self.image_urls = self.get_image_urls()
        self.hasImages = len(self.images) > 0
        
    def get_min_height(self):
        """
        Right now if you don't set the min-height on the container,
        it does a little jarring when the js sets the image.
        So this prevents it....
        """
        if not self.hasImages:
            return 0
        else:
            height = self.images[0].getHeight()
            for image in self.images[1:]:
                im_height = image.getHeight()
                if im_height < height:
                    height = im_height
                    
            return height
        
    def style(self):
    	""" return max instead of min as described above"""
        return 'max-height:%spx' % self.get_min_height(), 
        
        
    def get_images(self):
        settings = SimplesliderSettings(self.context)
        imagepaths = settings.imagepaths
        tags = settings.tags
        try:
            image_folder = self.context.unrestrictedTraverse(str(imagepaths))
            return [image_folder[id] for id in image_folder.objectIds() if image_folder[id].portal_type == "Image"]
        except:
        	
        
        return []

    def get_image_urls(self):
        if hasattr(self, 'images') and type(self.images) == list:
            return [image.absolute_url() for image in self.images]
        else:
            return []
