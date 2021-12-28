mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"productspraveen@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[theme]
primaryColor="#d33682"
backgroundColor="#002b36"
secondaryBackgroundColor="#586e75"
textColor="#fafafa"
font="sans serif"
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
