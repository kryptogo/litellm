## This is a template base class to be used for adding new LLM providers via API calls

class BaseLLM():
    def validate_environment(): # set up the environment required to run the model 
        pass  

    def completion(): # logic for parsing in - calling - parsing out model completion calls
        pass

    def embedding(): # logic for parsing in - calling - parsing out model embedding calls
        pass 