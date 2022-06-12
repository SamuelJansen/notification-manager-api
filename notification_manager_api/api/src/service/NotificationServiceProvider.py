from python_helper import Constant as c
from python_helper import ObjectHelper, log
from python_framework import Service, ServiceMethod, FlaskUtil, JwtConstant

try:
    from config import NotificationConfig
    import NotificationDto
except:
    try:
        from notification_manager_api.api.src.config import NotificationConfig
        from notification_manager_api.api.src.dto import NotificationDto
    except Exception as exception:
        log.warning(log.warning, 'There are most likely an issue related to queue-manager-api dependencies imports', exception=exception)
        from notification_manager_api import NotificationConfig
        from notification_manager_api import NotificationDto


def getNotificationService():
    @Service()
    class NotificationService:

        @ServiceMethod(requestClass=[[NotificationDto.NotificationRequestDto]])
        def notifyAll(self, dtoList):
            return self.notifyAllByApiKey(dtoList, NotificationConfig.NOTIFICATION_API_KEY)


        @ServiceMethod(requestClass=[[NotificationDto.NotificationRequestDto]])
        def notifyAllByCurrentApiKey(self, dtoList):
            notificationApiKey = FlaskUtil.safellyGetHeaders().get(JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME, c.BLANK).split()[-1]
            self.validator.notification.validateNotificationApiKey(notificationApiKey)
            return self.emitter.notification.notifyAll(dtoList, notificationApiKey)


        @ServiceMethod(requestClass=[[NotificationDto.NotificationRequestDto], str])
        def notifyAllByApiKey(self, dtoList, notificationApiKey):
            if ObjectHelper.isNone(notificationApiKey):
                return self.notifyAllByCurrentApiKey(dtoList)
            return self.emitter.notification.notifyAll(dtoList, notificationApiKey)

    return NotificationService
