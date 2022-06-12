from queue_manager_api import MessageEmitter, MessageEmitterMethod
from python_framework import JwtConstant
from queue_manager_api import MessageDto

try:
    from config import NotificationConfig
except:
    try:
        from notification_manager_api import NotificationConfig
    except:
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
