from bs4 import BeautifulSoup
import codecs, json

def get_data(category):
    for tr in category.find_all("tr", {"class" : "event" }):
        title = tr.find("div", { "class" : "title" }).text
        desc = tr.find("div", { "class" : "subject" }).text
        date = tr.find("div", { "class" : "date" }).text
        time = tr.find("div", { "class" : "time" }).text
        location = tr.find("td", { "class" : "location" }).text

        content.append({
            "fields": {
                "geo": [f"lat {location}", f"long {location}"],
                "category": "event",
                "title": title,
                "desc": desc,
                "date": date,
                "time": time,
                "location": location
            }
        })

# Read local HTML

html_doc = codecs.open("events.htm", "r", "utf-8")

soup = BeautifulSoup(html_doc, 'html.parser')

content = []

# get tables with events
konzerte = soup.find("table", {"id": "cat_1"})
nachtleben = soup.find("table", {"id": "cat_2"})
film = soup.find("table", {"id": "cat_3"})
buehne = soup.find("table", {"id": "cat_4"})
diverses = soup.find("table", {"id": "cat_5"})
ausstellung = soup.find("table", {"id": "cat_6"})

# extract data from tables
get_data(konzerte)
get_data(nachtleben)
get_data(film)
get_data(buehne)
get_data(diverses)
get_data(ausstellung)

# convert to json
output = json.dumps(content, indent=4)

# write to file
with open("output.json", "w") as f:
    f.write(output)