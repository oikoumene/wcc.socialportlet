from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from wcc.socialportlet import MessageFactory as _

class IWCCSocialConnectPortlet(IPortletDataProvider):
    """
    Define your portlet schema here
    """
    gplus_url = schema.TextLine(
        title=_(u'Google+ URL'),
        required=False
    )

    facebook_url = schema.TextLine(
        title=_(u'Facebook URL'),
        required=False,
    )

    twitter_url = schema.TextLine(
        title=_(u'Twitter URL'),
        required=False
    )

    rss_url = schema.TextLine(
        title=_(u'RSS URL'),
        required=False
    )

class Assignment(base.Assignment):
    implements(IWCCSocialConnectPortlet)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('WCC Social Connect Portlet')

class Renderer(base.Renderer):
    
    render = ViewPageTemplateFile('templates/wccsocialconnectportlet.pt')

    @property
    def available(self):
        return True

class AddForm(base.AddForm):
    form_fields = form.Fields(IWCCSocialConnectPortlet)
    label = _(u"Add WCC Social Connect Portlet")
    description = _(u"")

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IWCCSocialConnectPortlet)
    label = _(u"Edit WCC Social Connect Portlet")
    description = _(u"")
