import requests
from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from queue_manager_api import MessageEmitter, MessageEmitterMethod
from python_framework import HttpStatus, GlobalException

from config import QueueConfig


@MessageEmitter(
    url = QueueConfig.SPEAK_ALL_EMITTER_BASE_URL,
    headers = {
        'Api-Key': f'Bearer {QueueConfig.SPEAK_ALL_EMITTER_API_KEY}'
    },
    timeout = QueueConfig.SPEAK_ALL_EMITTER_TIMEOUT,
)
class VoiceEmitter :

    @MessageEmitterMethod(
        queueKey = QueueConfig.SPEAK_ALL_QUEUE_KEY,
        requestClass=[[dict]]
    )
    def speakAll(self, dtoList):
        return self.emit(body=dtoList)
