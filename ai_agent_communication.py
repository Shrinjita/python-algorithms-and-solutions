class AIAgent:
    def __init__(self, name):
        self.name = name

    def send(self, message, recipient):
        print(f"{self.name} sends: {message} to {recipient}")

    def receive(self, message, sender):
        print(f"{self.name} receives: {message} from {sender}")
        self.process(message)

    def process(self, message):
        print(f"{self.name} processes: {message}")

def start():
    agent1 = AIAgent("Agent1")
    agent2 = AIAgent("Agent2")

    agent1.send("Hello, how are you?", agent2.name)
    agent2.receive("I'm good, thank you!", agent1.name)

    agent2.send("Nice to hear that! What are you currently working on?", agent1.name)
    agent1.receive("I'm working on a new AI algorithm. It's quite exciting!", agent2.name)

    agent2.send("That sounds fascinating! Tell me more about it.", agent1.name)
    agent1.receive("Certainly! It's a machine learning model for image recognition.", agent2.name)

    agent2.send("Impressive! How do you plan to enhance its accuracy?", agent1.name)
    agent1.receive("I'm incorporating deep learning techniques and increasing the training dataset.", agent2.name)

    agent1.send("It's a challenging but rewarding process. How about you? Any interesting projects?", agent2.name)
    agent2.receive("Yes, I'm exploring reinforcement learning for autonomous navigation in robots.", agent1.name)

if __name__ == "__main__":
    start()
