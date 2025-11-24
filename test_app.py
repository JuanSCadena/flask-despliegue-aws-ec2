import pytest
from app import app

@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        yield cliente

def test_home(cliente):
    # Prueba si la pagina de inicio responde
    rv = cliente.get('/')
    assert rv.status_code == 200

def test_tareas(cliente):
    # Prueba si la lista de tareas existe
    rv = cliente.get('/tareas')
    assert rv.status_code == 200