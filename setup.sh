mkdir -p ~/.streamlit/

acho "\
[server]\n\
headless = true\n\
port = $PORT\n\
enbleCORS = false\n\
\n\
" > ~/.streamlit/config.toml