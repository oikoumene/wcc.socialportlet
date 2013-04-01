from collective.grok import gs
from wcc.socialportlet import MessageFactory as _

@gs.importstep(
    name=u'wcc.socialportlet', 
    title=_('wcc.socialportlet import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('wcc.socialportlet.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
