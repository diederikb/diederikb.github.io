
# coding: utf-8

# # Talks markdown generator for academicpages
# 
# Takes a TSV of talks with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). The core python code is also in `talks.py`. Run either from the `markdown_generator` folder after replacing `talks.tsv` with one containing your data.
# 
# TODO: Make this work with BibTex and other databases, rather than Stuart's non-standard TSV format and citation style.

# In[1]:

import pandas as pd
import os


# ## Data format
# 
# The TSV needs to have the following columns: title, type, url_slug, venue, date, location, talk_url, description, with a header at the top. Many of these fields can be blank, but the columns must be in the TSV.
# 
# - Fields that cannot be blank: `title`, `url_slug`, `date`. All else can be blank. `type` defaults to "Talk" 
# - `date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. 
#     - The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/talks/YYYY-MM-DD-[url_slug]`
#     - The combination of `url_slug` and `date` must be unique, as it will be the basis for your filenames
# 


# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:

talks = pd.read_csv("talks.tsv", sep="\t", header=0)
talks


# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    if type(text) is str:
        return "".join(html_escape_table.get(c,c) for c in text)
    else:
        return "False"


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page.

# In[5]:

def field(item, name):
    """Value of a TSV column as a stripped string, or None when it is empty."""
    value = item.get(name)
    if pd.isna(value):
        return None
    return str(value).strip() or None

for row, item in talks.iterrows():

    date_start = field(item, "date_start")
    date_end = field(item, "date_end")
    date_single = field(item, "date")

    # Multi-day talks give a start and end date, single-day talks just a date.
    # The filename and the permalink are both built from this one slug, so they
    # can never drift apart.
    slug = str(date_start or date_single) + "-" + item.url_slug

    md = "---\ntitle: \""   + item.title + '"\n'
    md += "collection: talks" + "\n"
    md += 'type: "' + (field(item, "type") or "Talk") + '"\n'
    md += "permalink: /talk/" + slug + "\n"

    if field(item, "venue"):
        md += 'venue: "' + field(item, "venue") + '"\n'

    if date_start:
        md += "date_start: " + date_start + "\n"
        if date_end:
            md += "date_end: " + date_end + "\n"
    elif date_single:
        md += "date: " + date_single + "\n"

    if field(item, "location"):
        md += 'location: "' + field(item, "location") + '"\n'

    md += "---\n"


    if field(item, "talk_url"):
        md += "\n[More information here](" + field(item, "talk_url") + ")\n"


    if field(item, "description"):
        md += "\n" + html_escape(field(item, "description")) + "\n"


    md_filename = os.path.basename(slug + ".md")
    #print(md)

    with open("../_talks/" + md_filename, 'w') as f:
        f.write(md)


# These files are in the talks directory, one directory below where we're working from.

