import json
import pandas as pd

class FewShotPosts:
    def __init__(self, file_path=r"F:\linkdin-post-generator\data\processed_posts.json"):  # changed to .json
        self.df = None
        self.unique_tags = None
        self.load_data(file_path)

    def load_data(self, file_path): 
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            df = pd.json_normalize(posts)
            self.df = df
            # for adding the column in dataframe
            df["length"]=df["line_count"].apply(self.categorize_length)
            # collect the various tags
            # sum is added to collect all the values into single array
            all_tags = df["tags"].sum()
            # for unique tags
            self.unique_tags=set(list(all_tags))
            self.df = df


# this is for the giving the length of the post 
    def categorize_length(self,line_count):
        if line_count < 5:
            return "Short"
        elif 5<= line_count  <= 10:
            return " Medium"
        else:
            return "Long"
        
    def get_tags(self):
        return self.unique_tags
    def get_filtered_posts(self, length, language, tag):
        df_filtered = self.df[
            (self.df['language'] == language) &
            (self.df["length"].str.lower() == length.lower()) &  # handle case sensitivity
            (self.df["tags"].apply(lambda tags: tag in tags))
        ]
        return df_filtered.to_dict(orient='records')



if __name__ == "__main__":
    fs = FewShotPosts()
    # short and english
    post = fs.get_filtered_posts("short","english","job search")
    print(post)


