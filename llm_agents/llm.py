from openai import OpenAI
import os
from pydantic import BaseModel
from typing import List, Optional

class ChatLLM(BaseModel):
    model: str = 'gpt-3.5-turbo'
    temperature: float = 0.0
    client: Optional[OpenAI] = None
    
    class Config:
        arbitrary_types_allowed = True  # Needed for the OpenAI client
    
    def __init__(self, **data):
        super().__init__(**data)
        # Initialize the OpenAI client
        self.client = OpenAI(
            #api_key=os.environ.get("OPENAI_API_KEY")
            api_key = "OPENAI_API_KEY" # company openai api key
        )
    
    def generate(self, prompt: str, stop: List[str] = None):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            stop=stop
        )
        return response.choices[0].message.content

if __name__ == '__main__':
    llm = ChatLLM()
    result = llm.generate(prompt='Who is the president of the USA?')
    print(result)


# UPDATE THIS CODE TO USE OPEN SOURCE LLM INSTEAD OF OPEN AI!!!