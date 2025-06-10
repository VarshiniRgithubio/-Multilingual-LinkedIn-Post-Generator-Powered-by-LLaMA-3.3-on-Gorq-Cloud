import os
import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm


def process_posts(raw_file_path, processed_file_path):
    enriched_posts = []

    with open(raw_file_path, encoding="utf8") as file:
        raw_data = json.load(file)

        # Fix: access the 'posts' list properly
        posts = raw_data["posts"]

        for post in posts:
            post_text = post["text"]
            metadata = extract_metadata(post_text)
            post_with_metadata = {'text': post_text} | metadata
            enriched_posts.append(post_with_metadata)

    unified_tags = get_unified_tags(enriched_posts)

    for post in enriched_posts:
        current_tags = post['tags']
        new_tags = {unified_tags.get(tag, tag) for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, encoding='utf-8', mode='w') as outfile:
        json.dump(enriched_posts, outfile, indent=4)


def get_unified_tags(posts):
    unique_tags = set()
    for post in posts:
        unique_tags.update(post['tags'])

    unique_tags_list = ', '.join(unique_tags)
    unified_tags = extract_tag_unification(unique_tags_list)
    return unified_tags


def extract_tag_unification(tags):
    template = '''You are given a list of tags. Unify them with these rules:
1. Merge similar tags into a single unified tag. Examples:
   - "jobseekers", "job hunting" → "Job Seeker"
   - "motivation", "inspiration", "divine" → "Motivation"
   - "personal growth", "self improvement" → "Self Growth"
   - "job scam", "scam alert" → "Scam Alert"
2. Use Title Case for all tags.
3. Output must be a valid JSON dictionary mapping original → unified tags.
Here are the tags: {tags}'''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'tags': tags})

    try:
        parser = JsonOutputParser()
        return parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Failed to parse tag unification output.")


def extract_metadata(post):
    template = '''You are given a LinkedIn post. Extract the following:
1. Return a valid JSON (no preamble).
2. The object must have three keys: line_count, language, and tags.
3. Tags must be a list of max 2 relevant tags.
4. Language should be one of: english, hinglish, kannada.
Here is the post:
{post}'''

    pt = PromptTemplate.from_template(template)
    chain = pt | llm
    response = chain.invoke(input={'post': post})

    try:
        parser = JsonOutputParser()
        return parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Failed to parse metadata from post.")


if __name__ == '__main__':
    process_posts(
        r"F:\linkdin-post-generator\data\raw_posts.json",
        r"F:\linkdin-post-generator\data\processed_posts.json"
    )
