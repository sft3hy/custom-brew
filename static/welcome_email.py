
def customize_welcome(topic: str):
    return f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to Custom Brew</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }}

            .container {{
                max-width: 600px;
                margin: 20px auto;
                background: #ffffff;
                padding: 5px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}

            .header {{
                background: #007bff;
                color: #ffffff;
                text-align: center;
                padding: 20px;
                font-size: 24px;
                font-weight: bold;
                border-radius: 8px 8px 0 0;
            }}

            .content {{
                padding: 20px;
                color: #333;
                line-height: 1.6;
                border: 2px solid #ccc;
                border-radius: 0 0 8px 8px;
            }}

            .button {{
                display: inline-block;
                padding: 12px 20px;
                margin: 20px 0;
                background: #007bff;
                color: #ffffff;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
                text-align: center;
            }}

            .footer {{
                text-align: center;
                font-size: 12px;
                color: #777;
                padding: 20px;
                border-top: 1px solid #ddd;
                margin-top: 20px;
            }}

            @media screen and (max-width: 600px) {{
                .container {{
                    width: 90%;
                    margin: auto;
                }}
            }}
        </style>
    </head>

    <body>

        <div class="container">
            <div class="header">
                Welcome to Custom Brew ☕
            </div>
            <div class="content">
                <p>Hey there,</p>
                <p>We're excited to have you on board! Custom Brew curates the latest news and insights based on your
                    favorite topics and delivers them straight to your inbox. You'll be receiving {topic} news every day at 9am EST.</p>
                <p>Your personalized news experience starts now!</p>
                <a href="https://custom-brew.streamlit.app/" class="button">Subscribe to more custom brews</a>
                <p>If you have any questions, feel free to email me at <a target
                        href="mailto:smaueltown@gmail.com">smaueltown@gmail.com</a>. Enjoy your fresh brews! ☕</p>
            </div>
            <div class="footer">
                Hobby project by Sam Townsend
            </div>
        </div>



    </body>

    </html>
    """