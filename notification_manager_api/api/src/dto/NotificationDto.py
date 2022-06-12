from python_helper import log

try:
    from converter.static import NotificationStaticConverter
except:
    try:
        from notification_manager_api import NotificationStaticConverter
    except Exception as exception:
        log.warning(log.debug, 'There are most likelly an issue related to queue-manager-api dependencies import', exception=exception)
        from notification_manager_api.api.src.converter.static import NotificationStaticConverter


class NotificationRequestDto:

    def __init__(self,
        message = None,
        severity = None,
        destinyList = None
    ):
        self.message = NotificationStaticConverter.toMessage(message)
        self.severity = NotificationStaticConverter.toSeverity(severity)
        self.destinyList = NotificationStaticConverter.toDestinyListDto(destinyList)


class NotificationResponseDto:

    def __init__(self,
        message = None,
        severity = None,
        destinyList = None,
        status = None
    ):
        self.message = NotificationStaticConverter.toMessage(message)
        self.severity = NotificationStaticConverter.toSeverity(severity)
        self.destinyList = NotificationStaticConverter.toDestinyListDto(destinyList)
        self.status = NotificationStaticConverter.toStatus(status)
