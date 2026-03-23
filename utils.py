from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper

def generate_script(subject, video_length, creativity, api_key):
    title_template = ChatPromptTemplate.from_messages(
        [
            ("human", "Think an interesting title for this {subject}")
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """
             You are a short video content creator. Based on the following title and related information, write a video script for a short video channel.
             Video Title: {title},Video Duration: {duration}, minutes (the length o the script should align with the video duration as much as possible)
             The opening must grab attention immediately. The middle section should provide valuable and informative content. The ending should include a surprise element. The script should be structured using the sections [Opening], [Middle], and [Ending].
             The overall tone should be light, engaging, and appealing to a younger audience.
             The script can reference the following information obtained from Wikipedia, but only use what is relevant and ignore anything unrelated:
             ```{wikipedia_search}```
             """)
        ]
    )

    model = ChatOpenAI(openai_api_key=api_key, temperature=creativity)

    title_chain = title_template | model
    script_chain = script_template | model

    title = title_chain.invoke({"subject": subject}).content

    search = WikipediaAPIWrapper(lang="en")
    search_result = search.run(subject)
    script = script_chain.invoke({"title": title, "duration": video_length, "wikipedia_search": search_result}).content

    return search_result, title, script