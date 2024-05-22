import time
from datetime import datetime
from config import *
from tools_constants import *
from text_to_speech import *
from assistant import *
from speech_to_text import *

volume = 5


def main():
    client = openai.OpenAI()

    assistant_id = create_assistant(client)
    # assistant_id="asst_K6tbdRlLfNV30PGqFs8f4ehR"
    # query = "Ile wody dziennie powinienem pić?"
    # run, thread = create_message_and_run(client, assistant_id=assistant_id, query=query)

    query = "Witaj! Jak się nazywasz i co jest twoim zadaniem?"
    run, thread = create_message_and_run(client, assistant_id=assistant_id, query=query)

    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            print("run status", run.status)

            if run.status == "requires_action":
                function_name, arguments, function_id = get_function_details(run)
                function_response = execute_function_call(function_name, arguments)
                run = submit_tool_outputs(
                    client, run, thread, function_id, function_response
                )
                continue
            elif run.status == "completed":
                messages = client.beta.threads.messages.list(thread_id=thread.id)
                latest_message = messages.data[0]
                text = latest_message.content[0].text.value
                print(text)

                if text:
                    path_to_mp3 = text_to_speech(text, TTS_URL)
                    play_voice_message(path_to_mp3)
                else:
                    print("No response received from assistant.")

                user_input = input()
                if user_input.upper() == "STOP":
                    break
                elif user_input.upper() == "V":
                    record_audio("output.wav", duration=10, channels=1)
                    user_input = speech_to_text("output.wav")
                    print(user_input)

                run, thread = create_message_and_run(
                    client, assistant_id=assistant_id, query=user_input, thread=thread
                )

                if not run:
                    print("Error creating new run.")
                    break
                continue

            elif run.status == "failed":
                print_error_details(run)
                break
            time.sleep(1)
        except Exception as e:
            print(f"Error in main loop: {e}")
            break


if __name__ == "__main__":
    main()
