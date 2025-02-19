from typing import List, Union, Generator, Iterator
import os 
from pydantic import BaseModel
from open_webui.models.users import Users

class Pipeline:
    class Valves(BaseModel):
        first_name: str
        last_name: str

    # Update valves/ environment variables based on your selected database 
    def __init__(self):
        self.name = "GVO Pipeline"
        
        # Initialize
        self.valves = self.Valves(
            **{
                "first_name": os.getenv("first_name", "<your first name here>"),
                "last_name": os.getenv("last_name", "<your last name here>")
            }
        )

    async def on_startup(self):
        # This function is called when the server is started.
        pass

    async def on_shutdown(self):
        # This function is called when the server is stopped.
        pass

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict, __user__: dict
    ) -> Union[str, Generator, Iterator]:
        # This is where you can add your custom pipelines like RAG.
        print(f"pipe:{__name__}")
        print(messages)
        print(user_message)
        
        return str(__user__["id"])