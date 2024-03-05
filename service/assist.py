from openai import OpenAI
import time

class Assist:
    def __init__(self):
        self.client = OpenAI()
        self.assist = self.client.beta.assistants.retrieve("asst_ugBhcqnuSdm17geQb5MIUrYG")
        self.thread = self.client.beta.threads.create()

    def ask(self, question: str) -> str:
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=question
        )
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assist.id
        )

        while run.status != "completed":
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=run.id
            )
            time.sleep(3)

        messages = self.client.beta.threads.messages.list(
            thread_id=self.thread.id
        )

        response = messages.data[0].content[0].text.value

        return response
    
    def chat(self, question: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                { "role": "user", "content": question },
            ]
        )
        return completion.choices[0].message.content
