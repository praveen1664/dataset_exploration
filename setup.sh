mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"productspraveen@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[theme]\n\
primaryColor="#d33682"\n\
backgroundColor="#002b36"\n\
secondaryBackgroundColor="#586e75"\n\
textColor="#fafafa"\n\
font="sans serif"\n\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
