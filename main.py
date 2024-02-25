import streamlit as st
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_story(topic):
    prompt_text = f"Once upon a time, there was a {topic}. "
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        max_tokens=300
    )
    return response.choices[0].text.strip()

def main():
    st.title("SummariGenius")

    api_key = st.text_input("Enter your OpenAI API key", type="password")
    topic = st.text_input("Enter a topic")

    if st.button("Generate Story"):
        if api_key and topic:
            openai.api_key = api_key
            st.write("Generating story...")
            story = generate_story(topic)
            st.write("### Generated Story")
            st.write(story)
        elif not api_key:
            st.warning("Please enter your OpenAI API key.")
        else:
            st.warning("Please enter a topic.")


if __name__ == "__main__":
    main()
