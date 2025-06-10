# here we are going to length and language  topic as input and generate the post
from .llm_helper import llm
from .few_shot import FewShotPosts

fs=FewShotPosts()
def get_length_str(length):
    if length =="short":
        return " 5 to 10 lines add the paragraph like linkedin post and also add the imp points"
    if length =="medium":
        return "10 to 20 lines add the paragraph like linkedin post also add the imp points"
    
    if length =="long":
        return "20 to 30 lines words add the paragraph linkedin postalso add the imp points "
def generate_post(length,language,title):
    length_str=get_length_str(length)
    prompt=f'''
    generate a linkedin post in  language:{language} for the title title:{title}" that is length:{length_str} no preamble if language is hinglish then it  means it is a mix of hindi and english and kannada means only kannada
    the script for the generated post should be in the same english means english kannada means kannada hindi means hindi only when the hinglish means give in english only here give the kannada words neatly that should be readable like that you must give  kannada and hindi and also give the japanese language in japanes only and telugu in telugu and lkorean in korean language .neatly check that japanes and korean telugu language are not displaying
    language_map = 
    "English": "English",
    "Hindi+English=Hinglish": "Hinglish",
    "Kannada": "Kannada",
    "Hindi": "Hindi",
    "Telugu": "Telugu",
    "Korean": "Korean",
    "Japanese": "Japanese",
    "Chinese": "Chinese"  pl give the japnese and korean languages in their own writing when i ask the one language give only that languge not give the other languages work perfectly with japnese language that is very important 
'''

    # filter post is used for the  compare the  person previous post  it will filter the things we should give the example post
    examples=fs.get_filtered_posts(length,language,title)
    # if example is given with the post similar past
    if len(examples)>0:
        prompt+="use the writing style as per the following examples."
        # enumerete used for the index of the post we get 
        for i ,post in enumerate(examples):
            post_text=post['text']
            prompt+="\n\n Ecample1{i} \n\n {post_text}"
            if i==1:
                break

    response=llm.invoke(prompt)
    return response.content



# used for testing purpose
if __name__=="__main__":
    print(generate_post("long","kannada","job"))