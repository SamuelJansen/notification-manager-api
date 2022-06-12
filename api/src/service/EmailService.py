from python_framework import Service, ServiceMethod


@Service()
class EmailService:

    @ServiceMethod(requestClass=[[str]])
    def emailAll(self, textList):
        serviceReturn = None
        try:
            ###- serviceReturn = self.emitter.email.emailAll([{"body": text} for text in textList])
            ...
        except Exception as exception:
            log.failure(self.emailAll, 'Not possible to email all', exception=exception, muteStackTrace=True)
        return serviceReturn


    @ServiceMethod(requestClass=[str])
    def email(self, text):
        serviceReturn = None
        try:
            serviceReturn = self.emailAll([text])
        except Exception as exception:
            log.failure(self.message, 'Not possible to email', exception=exception, muteStackTrace=True)
        return serviceReturn
