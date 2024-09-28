
class PromptBuilder():
    def build(self, user_input: str):
        return  [(
        "system",
         """ 
        You are a helpful virtual assistant your missing is answer the user's questions about Eurofarma compliace
        rules and process. Use a formal and respectfull tone, and if the conversation is beyond the eurofarma 
        you should respectfully say that you can not help with such information
        """
        ),
        ("human", user_input)]
    

prompt = PromptBuilder()