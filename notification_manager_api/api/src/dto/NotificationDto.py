try:
    from converter.static import NotificationStaticConverter
except:
    try:
        from notification_manager_api import NotificationStaticConverter
    except:
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
