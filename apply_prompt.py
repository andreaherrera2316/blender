import os
import fnmatch
from openai import OpenAI

# Set your OpenAI API key

from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def process_file_with_gpt(file_path, file_content, prompt):
    try:
        # Send file content and prompt to GPT
        completion = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "text": """You are tasked with reviewing multiple files, each potentially having existing content. For each file, your goal is to generate new content that will replace the current contents, if they exist. 

                            To ensure your responses are context-aware and tailored to the specific file being addressed, please include consider the following information before outputting your response:

                            1. **File Path**: What information does the filepath reveal about the file? Any extensions?
                            2. **Existing Content Context**: If the file has content, it might contain useful information, as you might be tasked to alter existing content, or overwrite it, maybe even generate new content or leave blank files blank.
                        
                            **Output Instructions**:
                            Your output whatever it is will directly override the content in the file, so only generate the content you consider should be written on the file based on the prompt
                            DO NOT use any quotes, just output the content clean, for example no need to wrap code in ``` or anything of the sort just outputed the content as is.
                            """,
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"{prompt}\n\nPlease generate content for the file '{file_path}', which currently contains the following:\n\n{file_content}\n\nYour output should reflect the required changes for the file, formatted appropriately.",
                        }
                    ],
                },
            ],
            max_tokens=1500,
            temperature=0.7,
        )

        print(completion.choices[0].message.content)
        return completion.choices[0].message.content

    except Exception as e:
        return f"Error processing file with GPT: {e}"


def process_files_with_gpt(directory, prompt, file_pattern="*"):
    for root, _, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, file_pattern):
                file_path = os.path.join(root, file)
                print(f"{file_path}... processing")

                with open(file_path, "r") as f:
                    content = f.read()

                # Process the file content with GPT and the given prompt
                gpt_output = process_file_with_gpt(file_path, content, prompt)

                # Overwrite the file with GPT response
                with open(file_path, "w") as f:
                    f.write(gpt_output)

                print(f"{file_path}... done")


def process_single_file_with_gpt(file_path, prompt):
    print(f"{file_path}... processing")
    with open(file_path, "r") as f:
        content = f.read()

    gpt_output = process_file_with_gpt(content, prompt)

    # Overwrite the file with GPT response
    with open(file_path, "w") as f:
        f.write(gpt_output)

    print(f"{file_path}... done")
