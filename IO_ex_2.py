with open('html_file.html','r') as web_page:
    with open('urls.txt','a') as wf:
        for lines in web_page.readlines():
            if '<a href' in lines:
                pos = lines.find('<a href')
                first_quote = lines.find('\"',pos+1)
                second_quote = lines.find('\"',first_quote+1)
                url = lines[first_quote+1 : second_quote]
                wf.write(url + '\n')
        

