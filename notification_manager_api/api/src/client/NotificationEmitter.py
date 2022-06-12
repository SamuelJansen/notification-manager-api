from python_helper import log
from python_framework import JwtConstant
from queue_manager_api import MessageDto, MessageEmitter, MessageEmitterMethod

try:
    from config import NotificationConfig
except:
    try:
        from notification_manager_api import NotificationConfig
    except Exception as exception:
        log.warning(log.debug, 'There are most likelly an issue related to queue-manager-api dependencies import', exception=exception)
        from notification_manager_api.api.src.config import NotificationConfig



@MessageEmitter(
    url = NotificationConfig.EMITTER_BASE_URL,
    headers = {
        JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {NotificationConfig.EMITTER_API_KEY}'
    },
    timeout = NotificationConfig.EMITTER_TIMEOUT
)
class NotificationEmitter :

    @MessageEmitterMethod(
        queueKey = NotificationConfig.QUEUE_KEY,
        requestClass=[[dict], str],
        responseClass=[MessageDto.MessageCreationRequestDto]
    )
    def notifyAll(self, dtoList, notificationApiKey):
        return self.emit(
            messageHeaders = {
                JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {notificationApiKey}'
            },
            body = dtoList
        )
