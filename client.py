from tags import *



# with HTML(output=f'D:\index.html') as f:
#     with TopLevelTag(name="aside", class_='container divmode', id_="id", text="texttext") as div:
#         with TopLevelTag(name="div", class_='div child', id_="id2", text="texttext23") as div2:
#             div2.text = "NEW TEXT"
#             with Tag(name='tag', class_='class') as t:
#                 t.text = 'TAG TEXT'
#                 div2+=t
#             with Tag(name='tag2', class_='class') as t:
#                 t.text = 'TAG22 TEXT'
#                 div2 += t
#             div+=div2
#         f+=div


# with HTML(output="D:\index.html") as doc:
#     with TopLevelTag(name="head", class_="head") as head:
#         with Tag(name="title", text="head text") as title:
#             title.text = 'hello'
#             head += title
#         doc += head

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

    # f += div
    #         div += div2
    #             div2 += body
# print("end")
# with TopLevelTag(name="aside", class_='container divmode', id_="id", text="texttext") as tlt:
#     print(tlt)
