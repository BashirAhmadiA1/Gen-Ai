import pandas as pd
import openai
from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os


key = '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'
openai.api_key = key


def get_api_response(string):
    output = None
   
    try:
        response = openai.Completion.create(
            model = 'text-davinci-003',
            prompt=string,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[' Human', ' AI:']
        )

        choices = response.get('choices')[0]
        output = choices.get('text')
    except Exception as e:
        print('ERROR:', e)
    
    return output

def updat_responses(message, array):
    array.append(message)

def create_input_message(message, array):
    p_message = '\nHuman: {}'.format(message)
    updat_responses(p_message, array)
    prompt = ''.join(array)
    return prompt

def get_bot_response(message, array):
    prompt = create_input_message(message, array)
    api_response =  get_api_response(prompt)

    if len(api_response) > 0:
        updat_responses(api_response, array)
        pos = api_response.find('\nAI: ')
        api_response = api_response[pos + 5:]
    else:
        api_response = 'Error, the correct response was not generated.'
    return api_response


def main():
    array = ['\nHuman: How was your day?',
             '\nAI: It was good, thank you!']
    os.environ["OPENAI_API_KEY"] = "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"

    loader = CSVLoader(file_path='ml_project1_data.csv')

    index_creator = VectorstoreIndexCreator()
    docsearch = index_creator.from_loaders([loader])

    chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")
             

    while True:
        user_input = input('You: ')
        if user_input.count('csv') == 0:
            response = get_bot_response(user_input, array)
            print('Bot: {}'.format(response))
        else:
            response = chain({"question": user_input})
            print('Bot: {}'.format(response['result']))

if __name__ == '__main__':
    main()