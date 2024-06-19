import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


def create_table_definition_prompt(df, table_name):
    """This function creates a prompt for the Gemini Pro API to generate SQL queries.

    Args:
        df (dataframe): pd.DataFrame object to automtically extract the table columns
        table_name (string): Name of the table within the database

        Returns: string containing the prompt for Gemini Pro
    """
    
    prompt = '''### sqlite table, with its properties:
#
# {}({})
#
'''.format(table_name, ",".join(str(x) for x in df.columns))
    
    return prompt

# def user_query_input():
#     """Ask the user what they want to know about the data.

#     Returns:
#         string: User input
#     """
#     user_input = input("Tell Gemini Pro what you want to know about the data: ")
#     return user_input

def combine_prompts(fixed_sql_prompt, user_query):
    """Combine the fixed SQL prompt with the user query.

    Args:
        fixed_sql_prompt (string): Fixed SQL prompt
        user_query (string): User query

    Returns:
        string: Combined prompt
    """
    final_user_input = f"### A query to answer: {user_query}.\nUse order by for interesting insights. Return only the SQL query starting with (including): 'SELECT'.\nInclude only SQL query in one line."
    return fixed_sql_prompt + final_user_input

def send_to_geminipro(prompt):
    """Send the prompt to Gemini Pro

    Args:
        prompt (string): Prompt to send to Gemini Pro

    Returns:
        string: Response from Gemini Pro
    """
    response = chat.send_message(prompt)
    return response

def final_answer(query,answer):
    prompt = f"Given the following question and answer, properly formulate the answer in simple language:\n\nQuestion:{query}\n\nAnswer:{answer} \n Note: If the question can be answered in one line then don't make any changes, otherwise tabulate the data containing more than one column. Also report the answer with proper currency as dollars. Combine the first name and last name of customer wherever necessary."
    final_response = chat.send_message(prompt)
    # print(final_response.text)
    return final_response.text

