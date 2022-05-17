from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from python_framework import Service, ServiceMethod, EnumItem

from config import NotificationConfig
from enumeration.NotificationSeverity import NotificationSeverity
from enumeration.NotificationStatus import NotificationStatus
import NotificationDto
import Notification


@Service()
class NotificationService:

    @ServiceMethod(requestClass=[[Notification.Notification]])
    def notifyAll(self, modelList):
        serviceException = None
        nextModelStatus = None
        try:
            serviceReturn = self.service.voice.speakAll([
                f'{model.severity} from {StringHelper.join(StringHelper.join(model.createdBy.split(c.DASH), character=c.SPACE).split(c.DOT), character=c.SPACE)}: {model.message}'
                for model in modelList
                if NotificationConfig.CURRENT_NOTIFICARION_DEGREE <= NotificationSeverity.map(model.severity).degree
            ])
            nextModelStatus = NotificationStatus.DELIVERED
        except Exception as exception:
            serviceException = exception
            nextModelStatus = NotificationStatus.NOT_DELIVERED
            log.prettyPython(self.notifyAll, 'Not possible to deliver notifications', modelList, logLevel=log.FAILURE)
        self.mapper.notification.overrideModelListStatus(modelList, nextModelStatus)
        self.persistAll(modelList)
        if ObjectHelper.isNotNone(serviceException):
            raise serviceException


    @ServiceMethod(requestClass=[[NotificationDto.NotificationRequestDto]])
    def acceptAll(self, dtoList):
        modelList = self.persistAll(self.mapper.notification.fromRequestDtoListToModelList(dtoList))
        log.status(self.acceptAll, f'Accpeting notifications: {modelList}')
        self.notifyAll(modelList)


    @ServiceMethod(requestClass=[[Notification.Notification]])
    def persistAll(self, modelList):
        log.status(self.persistAll, f'Persisting notifications: {modelList}')
        return self.repository.notification.saveAll(modelList)
