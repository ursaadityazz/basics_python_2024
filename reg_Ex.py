import re

text = "A wiki is a form of online hypertext publication that is collaboratively edited and managed by its audience directly through a web browser. A typical wiki contains multiple pages that can either be edited by the public or limited to use within an organization for maintaining its internal knowledge base."


x = re.search(r"\s",text)
# x = re.findall(r"\s",text)
y = re.split('\s',text)
y = re.sub('\s',' ok ',text)
print(x)
print(y)