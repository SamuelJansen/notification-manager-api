from python_framework import SqlAlchemyProxy as sap
from python_framework import ConverterStatic

from constant import AuditoryConstant, NotificationConstant
from util import AuditoryUtil
from enumeration.NotificationSeverity import NotificationSeverity
from enumeration.NotificationStatus import NotificationStatus
from ModelAssociation import MODEL, NOTIFICATION


class Notification(MODEL):
    __tablename__ = NOTIFICATION

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    message = sap.Column(sap.String(sap.STRING_SIZE), nullable=False, default=NotificationConstant.DEFAULT_MESSAGE)
    severity = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False, default=NotificationConstant.DEFAULT_SEVERITY)
    status = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False, default=NotificationConstant.DEFAULT_STATUS)
    createdAt = sap.Column(sap.DateTime(), nullable=False)
    updatedAt = sap.Column(sap.DateTime(), nullable=False)
    createdBy = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False, default=AuditoryConstant.DEFAULT_USER)
    updatedBy = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False, default=AuditoryConstant.DEFAULT_USER)

    def __init__(self,
        id = None,
        message = None,
        severity = None,
        status = None,
        createdAt = None,
        updatedAt = None,
        createdBy = None,
        updatedBy = None
    ):
        self.id = id
        self.message = ConverterStatic.getValueOrDefault(message, NotificationConstant.DEFAULT_MESSAGE)
        self.severity = NotificationSeverity.map(ConverterStatic.getValueOrDefault(severity, NotificationConstant.DEFAULT_SEVERITY))
        self.status = NotificationStatus.map(ConverterStatic.getValueOrDefault(status, NotificationConstant.DEFAULT_STATUS))
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.createdBy = createdBy
        self.updatedBy = updatedBy
        AuditoryUtil.overrideApiKeyData(self)

    def __repr__(self):
        return f'{self.__tablename__}(id: {self.id}, severity: {self.severity}, status: {self.status})'
