import markov_chain
import random
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

TOKEN="you token"
id_group="you id group"

def msgst():
	mc = markov_chain.MarkovChain()
	with open('bd.txt', 'r') as c:
		for line in c.readlines():
			mc.parse_and_add(line.strip())
		return mc.generate_sentence(random.randint(0,140))
   
    
    		
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

longpoll = VkBotLongPoll(vk_session, id_group)

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text.find("@otynbotleja") != -1 :
            vk.messages.send(peer_id=event.obj.peer_id,random_id=get_random_id(),message=msgst())
        	











