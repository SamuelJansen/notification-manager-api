import requests
from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from queue_manager_api import MessageEmitter, MessageEmitterMethod
from python_framework import HttpStatus, GlobalException, JwtConstant, FlaskUtil

from config import QueueConfig


@MessageEmitter(
    url = QueueConfig.SEND_TELEGRAM_EMITTER_BASE_URL,
    headers = {
        JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {QueueConfig.SEND_TELEGRAM_EMITTER_API_KEY}'
    },
    timeout = QueueConfig.SEND_TELEGRAM_EMITTER_TIMEOUT,
)
class TelegramEmitter :

    @MessageEmitterMethod(
        queueKey = QueueConfig.SEND_TELEGRAM_QUEUE_KEY,
        requestClass=[[dict]]
    )
    def messageAll(self, dtoList):
        self.emit(
            messageHeaders = {
                JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {QueueConfig.TELEGRAM_MANAGER_API_API_KEY}'
            },
            body = dtoList
        )