import requests
import streamlit as st

base_url = "http://api.github.com"


def selecionarusuario(username):
    url = f'{base_url}/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Consulta Github')
    usuario = st.text_input('Insira o username de usuario do github')
    if st.button('Buscar'):
        infousuario = selecionarusuario(usuario)
        if infousuario is not None:
            # st.write(infousuario)
            st.markdown(f'''
                        <div class="card" style="width: 18rem;">
                        <img class="card-img-top" src="{infousuario['avatar_url']}" alt="Card image cap">
                        <div class="card-body">
                            <h5 class="card-title">{infousuario['login']}</h5>
                            <p class="card-text">{infousuario['bio']}</p>
                            <a href="#" class="btn btn-primary">Go somewhere</a>
                        </div>
                        </div>
                        ''', unsafe_allow_html=True)


ui()
