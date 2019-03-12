from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-550463879186-550669449941-550404286979-07e3375efbeb847752a2e81c6d69f8b1', #app verification token
							'xoxb-550463879186-550723226005-MmSvBFJQneahEvDp6PZWQZ6E', # bot verification token
							'rgPFLWMkuPK6nYy0yywpfVlW', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))