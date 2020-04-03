from tags import *

with HTML(output='D:\\index.html') as doc:
    with TopLevelTag(name="head", class_='head') as head:
        with Tag(name="title") as title:
            head.text = "head text"
            title.text = "hello"
            head += title
        doc += head

    with TopLevelTag(name="body") as body:
        with Tag(name="h1", class_="main-text") as h1:
            body.text = "BODY"
            h1.text = "Test"
            body += h1

        with Tag(name="div", class_="container container-fluid", id="lead") as div:
            with Tag(name="p") as paragraph:
                paragraph.text = "another test"
                div += paragraph

            with Tag(name="img", class_='imageclass', is_single=True, src="/icon.png") as img:
                div += img
            body += div
        doc += body

print('done')

  
