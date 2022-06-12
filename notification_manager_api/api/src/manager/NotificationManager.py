from python_helper import log, ReflectionHelper
from python_framework import ResourceManager


class NotificationManager:

    def __init__(self):
        self.addResources = addResources
        log.debug(self.__init__, f'{ReflectionHelper.getName(NotificationManager)} created')


    def addResource(self, api, app):
        api.resource.manager.notification = self
        self.api = api


    def onHttpRequestCompletion(self, api, app):
        ...


    def onRun(self, api, app):
        ...


    def initialize(self, api, app):
        if self.addResources:
            log.status(self.initialize, f'{ReflectionHelper.getClassName(self)} adding resources')
            self.addServices(api, app)
            self.addEmitters(api, app)
        ###- ReflectionHelper.getItNaked(api)
        log.success(self.initialize, f'{ReflectionHelper.getClassName(self)} is running')


    def onShutdown(self, api, app):
        log.success(self.onShutdown, f'{ReflectionHelper.getClassName(self)} is successfuly closed')


    def addServices(self, api, app):
        try:
            import NotificationServiceProvider
        except:
            try:
                from notification_manager_api.api.src.service import NotificationServiceProvider
            except Exception as exception:
                log.warning(log.warning, 'There are most likely an issue related to queue-manager-api dependencies imports', exception=exception)
                from notification_manager_api import NotificationServiceProvider
        ResourceManager.addServiceListTo(api, [NotificationServiceProvider.getNotificationService()])


    def addEmitters(self, api, app):
        try:
            import NotificationEmitterProvider
        except:
            try:
                from notification_manager_api.api.src.client.emitter import NotificationEmitterProvider
            except Exception as exception:
                log.warning(log.warning, 'There are most likely an issue related to queue-manager-api dependencies imports', exception=exception)
                from notification_manager_api import NotificationEmitterProvider
        ResourceManager.addServiceListTo(api, [NotificationEmitterProvider.getNotificationEmitter()])
