# v1.0 - Rokon Simple AI Meme Roast Battle (Minimal)
# { "Depends": "py-genlayer:latest" }

from genlayer import *
import json
import time

class RokonSimpleMemeRoast(gl.Contract):
    topics: TreeMap[str, str]
    xp: TreeMap[Address, u256]

    def __init__(self):
        self.topics = TreeMap()
        self.xp = TreeMap()

    @gl.public.write
    def create_battle(self) -> str:
        battle_id = "roast_" + str(int(time.time()))

        def get_topic():
            prompt = "Return only this exact JSON: {\"topic\": \"one fun roast or meme battle topic about AI or GenLayer\"}"
            result = gl.nondet.exec_prompt(prompt)
            data = json.loads(result)
            return data["topic"]

        topic = gl.eq_principle.strict_eq(get_topic)
        self.topics[battle_id] = topic
        return battle_id

    @gl.public.write
    def add_xp(self, amount: u256):
        sender = gl.message.sender_address
        if sender not in self.xp:
            self.xp[sender] = 0
        self.xp[sender] += amount

    @gl.public.view
    def get_topic(self, battle_id: str) -> str:
        return self.topics.get(battle_id, "Not found")

    @gl.public.view
    def get_my_xp(self) -> u256:
        sender = gl.message.sender_address
        return self.xp.get(sender, 0)
