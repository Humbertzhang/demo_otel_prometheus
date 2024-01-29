import os
import time
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from traceloop.sdk import Traceloop
from openai import OpenAI

Traceloop.init(disable_batch=True,
               exporter=ConsoleSpanExporter())
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def main():
    while True:
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
                ]
            )

            print(completion.choices[0].message)
            print(f"{completion.usage=}")

            time.sleep(10)
        # have to try catch because of network instability problem
        except Exception as e:
            print(f"{e=}")
            time.sleep(5)


if __name__ == '__main__':
    main()
