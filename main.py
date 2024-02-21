import streamlit as st
import datetime
page_index = st.session_state.get("page_index",0)


if page_index == 0:
    st.header(":red[Will you be my valentine ?]")
    st.markdown('![Alt Text](https://s.net.vn/cKHG)', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        yes = st.button("Yes :heart_eyes: :revolving_hearts:")
        if yes:
            st.session_state["page_index"] =1
    with col2:
        st.button("No")



if page_index == 1:
    st.title(":red[Thank you]")
    st.markdown('![Alt Text](https://s.net.vn/HjP5)', unsafe_allow_html=True)
    click  = st.button("Click me UWU")
    if click == True:
        st.session_state["page_index"] =2

if page_index ==2:
    st.title(":red[Are you free on...]")
    st.subheader(":red[select a day]")
    d = st.date_input(":red[Which day]", value=None)
    
    click = st.button("Submit")
    if click == True:
        st.session_state["page_index"] = 3

if page_index ==3:
    st.title(":red[What food would you like to eat ?]")
    col1, col2,col3 = st.columns(3)
    with col1:
        st.image("https://congthucphache.com/wp-content/uploads/2020/04/com-tron-han-quoc-ngon.jpg")
        st.image("https://cdn.tgdd.vn/2021/02/CookProduct/1114-1200x676.jpg")
    with col2:
        st.image("https://daotaobeptruong.vn/wp-content/uploads/2021/01/mi-cay.jpg")
        st.image("https://static.hotdeal.vn/images/1638/1638317/60x60/361274-buffet-nuong-ong-rau-thoa-thich-thit-bo-hai-san-gan-40-mon-bao-gom-trang-mieng.jpg")
    with col3:
        st.image("https://images.foody.vn/res/g4/36621/prof/s/foody-mobile-5879-jpg-722-636341510844476077.jpg")
        st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAkFBMVEX9whQAAAD/yBX/xhT/xxX/yhV0WQmlfg0DBQHjrhJfSQfSoRBPPQb4vhP1vBNqUQfoshKGZwqeeQy3jA4PDAG8kA7ClQ/dqRHvtxP/zhU1KAPQnxCwhw7lrxKUcQuEZQp8Xwk/MASPbQuifAxWQgY7LQQuIwNsUwhZRAYbFAAgGAEpHwJENAQcFQANCgEWEABPzGMoAAAR3klEQVR4nO1daXujvA7FW2gWyNYAKWnWpu00meb//7uLF7AMBtKGd6aZ6/NhnmkgxseLLAlJ8TwHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHBwcHB4c/DkL+dg/+W7DJav7MumiJGENFMP4ZIxeMUYZxF52JViku/iDzzWaBG+7+Uwh+I4HBzbM44c0cA/UXexet0ltbvRl0gxT2N1LEL7IZxSmWrQ5v7+KNwG85Q+TfRpE8iFbOshW6ko2mf30rkqhgiG7bNfhJthLzSSTeh/yr31E/bwDraYrDW3YNVg09Dhljz0fVZGf9vAFsoyk+37CmSJq38mt0yv+7+QnC1GMzTTFov72+nRdUQdJZL28Cmxc9uunMCC5lgtHfPywk2LCTSfTCo0lw0Ymm1Ano5KMTycAOgN/L5EdsQgXiDeSyuvH4ot787ZUL1NE6/jkTKMHS3nEc3z7qUt8m7A/vQCLQcg9mnawqwjiaHibuaHgWbbleao0yksRptIiiYT8kzG7QUBYmCe2CIPFWg4/P02Dl1XHM7hifHl57dauYJPvz5fM4Ta7ZMIR56X4Epdt5M0+q40tm/Ij+nN4kSGVLcfGoGgUJF2rizE6xn1+P25/Ghj1kwXnllR6+yy+FX6ZUQgieM7F2Sh9MaG2jyM755WObqGJR6XQCOECKxC8+398oH9gUPMSqPeABuGNluQOMUbNCxOIdasAJrHJgQN1qBgfGQ55t/TI2zbC61+Lm7+ter5v4ceg9h8ddMSw9tWdpzWRomSbAsMHyIuGujSCaFQuyO4Ze6RmWZVZi+Po9hqSP2rEtzobOGFK/9Ix99fwpMaw+8RqGQGJLXMb72WG9eX+AH/rFFuiO4Wd5GKvHT5lhRaBewZA8l5p4ZoxmwIxNVrp9fTB0xZDMURmHimyuMESROdFg/dUxNK20gwcbIKyvjkhguXXFEL9WGKKKrKwyRH3jJjA/NQwZPHB2SWUnsHC+GU/7YHA7Ygh8Wno/zssULQwfjbU8aWNIFuC7Y+sBnmn/xucdMdTKyNOy8NO8lkfYwhCd4U2tDD0gTt6u6283DIE65jM9iWWD08YQbcFj2xgCDQyNrrQVumEI/FABUL3OpRatDKEzOmlhyICYuVaN7oahlvKZKsN0kyULATAELj6gvrUwhJq7f6251wlD9gZ7q32naGw2CRgSaPkU6k8LQ7rX16/2uHTCUG+fV94G0/0wjSjAMKA7fVehvrUwZPo7Fo2pjqE2eb7NkG312uGCmmodfGO0CRkSaE3mj27bh/py1TAhDJtQn4OJ/zZD0Fe5/YFINI47yNDUL5X6BlqyMQTtVq5Rf4cgPnrq2O+AIdZNKJMJShR4+hoMPbYCHZLqWzNDKGjKfWUWj4Z8uUdvX6XA8lVrB2oeRjcMhnB1K/WthaFWnE7lvpb0cYGL6M3t+5AeLM/Vj1mBDVNi6NGzvk+ob1cz/GC1lwCGHTHULfr5ksT6pR0c7TJDw3fF1TewHJoZllepnaEYXdCX7zGEZpNWM4AUWehJrDA0pA2Xu40MPbAPy5dMJ5GCEAI3MwRmE1CFmXb1gUmsMPQwlDYL3MKwQW21TqJkqHf7txjCluPsRGISSyBrtBHFqja4IW0mYMW3nIer8nmI4+3xiQO4UYUr41aG7Ek32Ht7G48Hg5fR+Xj6pT/+KNQPbWNpRQ18lmlEzQyBTmPprBrdpW5j0QFD+w4vodiJNoZeAEy+rbYd2vTSWtMCSC+h+GN9Un6HIat3rWsUHnowB5phxXdWzxDo9LUxTvAsDm5neNUU6sghMB5AJcdVJ1YNQw+DG6xvRoy9vmO3M4S7sAEjVmEInfYw5KWZIdDp0c7qpaFgzKXGeNN7iyunsLCEAUODgM32t/tpDIPEYkCR6vsvwPD9ywyZxYVohbKEwZSb1n9QcSfXMDRejrxUXsSS4KQvqxkDFvCXGRquvXRYQgrEghrOWoYWaVPjayO/wT2fkfnCl8XQXaweARi+fJUhBQO2ZaQM+D5RmlW1DC3Spo6hORbnhccoD1IgBLNnqD0UPrwb5tBw5NveSgMlS54O9QzN16sNDE09T3R7Pc/WTzrfmwfXpfjC9+eQgSkc2b4LPfDCnQEYVrwQuCRtat89wUi8BhRxiN9nCC1ue7CRcUfYwrBsHdS/P7yK4tD2htQ6D/WAKtTF7vmCxyU/nBoZll58NrwDZgvUhqH13dMXGYJzxvIiTXYa7NQnZjC0BEhjo+NN8cW4f0JNeJ1Ax8L35xAcTXWxOARo1czQS22SyZA2jbEYhDaFKqzNd0/fP/H1qlrXuWep3jI8YBi4vay3A2kzbukMS4yjAWCbmF8FC8m/2lGuup/rbDb1KW8+n7WBaDzMT2S/JnYnp9hrfzwLSx5SjtEqqAxN4cb4auJMdqST+XZ0HkdLWjntc1B2yI6pX4NU3oO9Ne/VKFrW3L6Meufz+DBpaBK0vQyj9fgojO3L02jrD70lq36RLuP9y/llOswa/RJDP8NKwG/CanU4+Cvwp3/wG75yRYvl230/e4Lf+DXV6OFrEbS9+8Pb1zYivkP89RweBwcHBwcHBweHK9GaIXXnIDQ9+P2fllnXIVgqbPDeT0lv7RxsjaZx2N+2OknuDmrrZQRF0tzSr0Zo3zXYxPd5zDuJck84G10wDwjH/8ZUyqCotce8IuyWpGgYRpsP9NJB4uxfB9ugkT97RGg71WG3Aco9uT+ixsxNIDGaLikms0+YDMVe0a/ePFx6GxTf+45kIxG37FGSTsGrhOFEem3Y28e9nxyTQmwSq7s0uTlJ/y+DzOvCUhTYaHzfO5GuW2ph0P3jfS9Tum9jOPsRZXS+j4xA8yrNhuAPdeU/QqbHNCto7P3zvldpdrafGp35CbpzScOjqM7PdZU6CPZGP6Ai2Y2gLwgNas68dP9wbRrjTwb2T9X8DA4Rc729810owFLU43tNciHFv+yI/OT+Z9ATJwYPh6Eb/ke45uRSHpnNBvevdkuwsdA9E34ykgUPe6FrHlqDN/+Kqc8+ePhOdjLGuRaHt4iKuZ39C7vQ42kansjPioXBPxEMQ6GVbzs5C6mqHNVcP+o/RCzi7rLZi8XKnAiefTGrX46ptQEffqGnlHl0VE10+a8hnpdtPbXrkpxhtj552FlsP0W+CBX4tV9Ovhw5dytIshpi0QN+WGTz5uW2RkaaM0wQ6mAfEh4x94TQ71+oo1V/NXjAdCZKcE/E8tE1z2whK5HY15eRgR0UxxKtvC6ZDCVsL+DVJWQNYcojIvn2INGBL9q+UGLIiP+fPnTRJbIYZKotS8/onP5Z0UwOMgiSPipXjNZmlH7DTp04aYgwXkhLKb7/AmQmAndDVKe6sG8IP16dkDvL1WxlvIzLNA+8YqUaf9SMyCIMhxOGbUUCiwiu0sVyWcTsBp4EmWlnfYSGDFcdbYQu30vRtjKnv6Y2oeSXbnhOwGkwE29AsD96hwHdPNJT6EnxEb3C2jtc4OpsWurNZZT/eZqS0soOigS+Y28FKgiG4+MYOmTCwa/BXuR5kBQ9oKfeLIoTWZRRVHYMkjjyN78N4YfD1YCHcu6286Bm0iOQJTQlMuHiCJoQCRhYqFHIFGM8QrTI4TMyKg7mTI3hNfQyVF8SUdHgVnVGcanCQMD05XQ8j867p4/H/JNjMYLEg6H5dplhPj0bHZ6NAF3Kcc5QpDmB01FUi5B/kvBsNINOcGpYOYR9HOike7DiRCLBJZIHA+r35/u3XakM8OPrYD08FdHKeGhetkTSh2oCd6oYdEaAfwkWGioYyiHU1SE1Q5LIVya9VbQ4VAvHimj/8X6/n76pxz2KuHwrw97SE6Vz9tlSpZlsCJLJc5ym8XAYT5IgkxEUp3nEeV5O+XJWA1wVskQ88TXiQjOI3sWGa2GoRVxYMJTZdRuPiTDngHfUmEPOMGI0k0wsUWHyYc5wVmaI5TN1A+H7lvXPB714liOZSaGyU7fPfJM+z36hz8oMypzsrZJYhIUJlfnzT4Bhv8TwV/HknKHMRIyKLuAwMrQOkcGYyyTsvanFUmW4Vgwz4TbF8NN4DCVApnyfcDGwab6ricXHKqZnW9I7rQyJZPjJWebFFQPFUGYORLAZc7GIjA0tdWX2abagrAzfuFJ6AWoLn6nAR0+wTbHj5PzETRqJSEx5Kt9RZvgMGCKxLhbUYEi5sN406OclhnJOMxOoluHEqEZEksCjxvxkHc8OfSEHbOVGNcQsVxyPZYbitPAUQymcE8hQ7oam9wwi3x0wlHm6QZXhTDLMrjcbNNmNGyzubjakxOr6XbmlkWEo5mMnL0uGQj6Ul3ojQ+kRHJJahit4pufRUEBnyeyoMRY9qUtyUV/h+2FasY2aGRKxNmR1IclQFEXT/SdUAtSTXXJJFC21jqsoWxmOMS/wprvFFjP5td2qaFNMslhCjSVhZdeqfqtmhh5dyAkoGIoqIoVgINFaoijzmLy9C63q/eUlHwchAFZNDPNfaCCTndoAfD7ymvjCk9FX/Wpi+IRsZ2QLQ1kF7TMoGJIPwBAUUFAtU5i3nz95LMa2luFcyBv+yRDlQgeDzZAt4574ZYFyTZ8yw5NN0NgZBoqhkDF8SgasmMMT0rmXINlfbSWY05lLSLF6onqGqSywJjKkH6S4JN4DenhAU1lxYZrtk/QKhjvbKiXW08JTemni5ZnZK5zvQ0OOkOlxtzvzhdtTbQSzPR+DwXS6z3eNGKxYCgKLpOFCXp7vjxmrB7QOmZe+8v8q8z57ZITj9lUqVP6KpBHr7FSnecvsbqF5ybo0TBZaASoIr8XCa0FO8zaolDRM1+9M5LIQDMt6KZ/6jAEf+Uw1eBC0BOR/xUunpBB5La+KeUc/K/Mcg+XkqTOFZ8vih6JFoaYdmdqH3G76bUhtsVW1IS5uB6cF5p6KHdNaWn7fQM0pPYgD8Vmy4s/9nTMUzu8Z1xdEheBZs5ssX20lICgbpVQQyqJmKHWF9UVOrvhjQRuaKJ2HQs5nTMTgwTO7EFAh39lF3vxln3iz3Irl16XO12tfpjKHeVLaiWJ7Fie4rHHMu0fBqtDFSIiaMajUML7agHlSYih/SItvNCHECn+CtHrlf6d82axWh5k/TxPuXqEsifz9dvw+I9ni5WtKptU3vyqVgu9S1PUlhI+7LKiq7HBCnvLHch9qccIWlaJI3tGnIJ9FJpoF3iKDIQuFJSKykMWFk9LTmVhSSq0PeLWezBSjIMA7+zMzvwhN1ahIk0YrxCzpVzQclRO+opgnw5LFBZ35PeJD3+MlsmJBUOhGBkOPnDRDVRNiQTHlzYgRgj8iIDXvJa+45cXyeJR6nxzijyFmmakrrVm1SLi8m1unh0yKUkWywMWoz5NssznemKqhgsy1v2z9lb8V9l9fVz952fZk1QpZlZaoy+pBfc0wz1h/3B5W/kaakTBvXTA89bbbce7reAqMIf4Yb8eyFMwhX09cXtso4mftSaFKvRitV6uZ+Fk8m8JeLqMTeJUKD6o7gqEWH1hWB9b9gfg0NjfI6JfY6pVnPh/YYHzUphVvIq/McNZ9SEsNTy2KuNm3JxlwzGAZom3eHP8DnD9S1OWllmJYpKRn+vWwWeLyDf7WCYUFCwxjj/+K0WsKPdKETQZm+jpNjBGaWt2JOFznv6v0lhYS1FO14E/T4rcy+en1bozRGzoXThvC0q0s97ZbT8prJVT9uOzG68gzr7LJXjnB/MCcATbMjqPzPOCOYb7RSPpWHgUe0JA7C0/r2gAGyibpYhH1iTleJJlMAvgDQjgs/RwUNnz+BLNgMkk8228OsQKWcFGqvlf1kxGxwM4bfz5f7cVG61UKupNMekWLxTBp/q2j9t8l+jug3vxdL8LXuln6qd2/CszPtG804naFv/xHIhRMjLj99BkLG6PJ23WvyAxJTm28FIp3m559h8hUc2FQRMqOajGW7hD0Q0zdCXOLkP+v0aV3h8isBzFzmZ6dmYTCOvzbXeoYmY7BWYkznpf+lmT/JYhfC/tUL0TkT1Ee/jGGu9N4XpzlOPQHjzbV+p7BWCkU4k//CqWDg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg4ODg8P/O/4HErj1m3f749MAAAAASUVORK5CYII=")
    
    click = st.button("Next")
    if click == True:
        st.session_state["page_index"] = 4

if page_index ==4:
    st.title(":red[Which dessert we eating ?]")
    st.image("https://staticcookist.akamaized.net/wp-content/uploads/sites/22/2022/06/LINK-TRAFFIC-18.jpg")
    click = st.button("Next")
    if click == True:
        st.session_state["page_index"]= 5

if page_index ==5:
    st.title(":red[What are we doing after ?]")
    col1, col2= st.columns(2)
    with col1:
        st.image("https://cdn.tgdd.vn/Files/2020/09/01/1286001/25-dia-diem-vui-choi-du-lich-sai-gon-cuc-thu-hut-check-in-tha-ga-202202161817584318.jpg")
        st.image("https://mia.vn/media/uploads/blog-du-lich/JP-World-giga-mall-1693126277.jpg")
    with col2:
        st.image("https://photo-cms-vovworld.zadn.vn/w500/Uploaded/vovworld/thpsplu/2021_07_12/vanhoa1_DUCA.jpg")
        st.image("https://lh7-us.googleusercontent.com/letzDdxj4Kkb8EVLy7t6zsOeFWrq9DFyXCl5DoiQXzbGXjiBsIqJkMBexUUeiAurQgYjLLQ5pG1309WrhuZlBwhddF_KHstB2SdxsmaXmiCeUSccoTX2ogumWZi0mevDxAMoH7Ts08FtCXTBlYP4zPE")
    
    click = st.button("Last page")
    if click ==True:
        st.session_state["page_index"] = 6

if page_index ==6:
    st.title(":red[Thank for being my valentine]")
    st.markdown('![Alt Text](https://s.net.vn/cRhy)', unsafe_allow_html=True)        