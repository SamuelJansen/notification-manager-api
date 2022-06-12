from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus


def buildNotificationValidator():

    @Validator()
    class NotificationValidator:

        @ValidatorMethod(requestClass=[str])
        def validateNotificationApiKey(self, notificationApiKey):
            if ObjectHelper.isNoneOrBlank(notificationApiKey):
                raise GlobalException(
                    message = f'Unauthorized',
                    logMessage = 'Missing current api key',
                    status = HttpStatus.UNAUTHORIZED
                )

    return NotificationValidator
