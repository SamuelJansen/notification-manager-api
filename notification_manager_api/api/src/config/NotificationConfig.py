from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()

try:
    from constant import NotificationConfigurationKeyConstant
except:
    try:
        from notification_manager_api import NotificationConfigurationKeyConstant
    except:
        from notification_manager_api.api.src.constant import NotificationConfigurationKeyConstant


QUEUE_KEY = globalsInstance.getSetting(NotificationConfigurationKeyConstant.QUEUE_KEY)

EMITTER_API_KEY = globalsInstance.getSetting(NotificationConfigurationKeyConstant.EMITTER_API_KEY)
EMITTER_BASE_URL = globalsInstance.getSetting(NotificationConfigurationKeyConstant.EMITTER_BASE_URL)
EMITTER_TIMEOUT = globalsInstance.getSetting(NotificationConfigurationKeyConstant.EMITTER_TIMEOUT)

NOTIFICATION_API_KEY = globalsInstance.getSetting(NotificationConfigurationKeyConstant.NOTIFICATION_API_KEY)
