from app.parser import parse_html


def test_parse_html_happy_path():
    html = """
    <html>
        <head>
            <title>Python</title>
            <meta name="description" content="Official Python website">
        </head>
        <body>
            <h1>Welcome</h1>
            <img src="a.jpg">
            <img src="b.jpg" alt="logo">
            <p>Hello world</p>
        </body>
    </html>
    """

    result = parse_html(html)

    assert result["title"] == "Python"
    assert result["meta_description"] == "Official Python website"
    assert result["h1_count"] == 1
    assert result["img_no_alt"] == 1
    assert result["word_count"] == 3


def test_parse_html_missing_title():
    html = """
    <html>
        <head>
            <meta name="description" content="Official Python website">
        </head>
        <body>
            <h1>Welcome</h1>
        </body>
    </html>
    """

    result = parse_html(html)

    assert result["title"] is None
    assert result["meta_description"] == "Official Python website"
    assert result["h1_count"] == 1


def test_parse_html_missing_meta_description():
    html = """
    <html>
        <head>
            <title>Python</title>
        </head>
        <body>
            <h1>Welcome</h1>
        </body>
    </html>
    """

    result = parse_html(html)

    assert result["title"] == "Python"
    assert result["meta_description"] is None
    assert result["h1_count"] == 1

def test_parse_html_no_h1():
    html = """
    <html>
        <head>
            <title>Python</title>
        </head>
        <body>
            <p>Hello world</p>
        </body>
    </html>
    """

    result = parse_html(html)

    assert result["h1_count"] == 0