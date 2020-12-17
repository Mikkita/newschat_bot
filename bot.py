{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import telebot\n",
    "import requests\n",
    "import time\n",
    "import json\n",
    "\n",
    "bot = telebot.TeleBot(!токен бота!)\n",
    "URL = 'https://api.telegram.org/bot!токен бота!/getUpdates?chat_id=!канал from!'\n",
    "from_chat_id = 'канал from'\n",
    "to_chat_id = 'канал to'\n",
    "starttime=time.time()\n",
    "messageid = 1\n",
    "\n",
    "while True:\n",
    "    response = requests.get(URL)\n",
    "    r = response.json()\n",
    "    if messageid < int(r['result'][-1]['channel_post']['message_id']):\n",
    "        messageid = int(r['result'][-1]['channel_post']['message_id'])\n",
    "        bot.forward_message(to_chat_id, from_chat_id, messageid)\n",
    "    time.sleep(10.0 - ((time.time() - starttime) % 10.0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
