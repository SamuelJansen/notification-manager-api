from python_framework import ConverterStatic, Serializer

try:
    from constant import NotificationConstant
    from enumeration.NotificationSeverity import NotificationSeverity
    from enumeration.NotificationStatus import NotificationStatus
    from enumeration.NotificationDestiny import NotificationDestiny
except:
    try:
        from notification_manager_api import NotificationConstant
        from notification_manager_api import NotificationSeverity
        from notification_manager_api import NotificationStatus
        from notification_manager_api import NotificationDestiny
    except:
        from notification_manager_api.api.src.constant import NotificationConstant
        from notification_manager_api.api.src.enumeration.NotificationSeverity import NotificationSeverity
        from notification_manager_api.api.src.enumeration.NotificationStatus import NotificationStatus
        from notification_manager_api.api.src.enumeration.NotificationDestiny import NotificationDestiny


def toMessage(message):
    return ConverterStatic.getValueOrDefault(
        message,
        NotificationConstant.DEFAULT_MESSAGE
    )


def toSeverity(severity):
    return NotificationSeverity.map(ConverterStatic.getValueOrDefault(
        severity,
        NotificationConstant.DEFAULT_SEVERITY
    ))


def toDestinyListDto(destinyList):
    if isinstance(destinyList, str):
        destinyList = Serializer.convertFromJsonToDictionary(destinyList)
    return [
        NotificationDestiny.map(destiny)
        for destiny in ConverterStatic.getValueOrDefault(
            destinyList,
            NotificationConstant.DEFAULT_DESTINY_LIST_DTO
        )
    ]


def toDestinyListModel(destinyList):
    return Serializer.jsonifyIt(destinyList)


def toStatus(status):
     return NotificationStatus.map(ConverterStatic.getValueOrDefault(
        status,
        NotificationConstant.DEFAULT_STATUS
    ))
