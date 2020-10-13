import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it("Use the map function ")
def test_map():
    f = open(os.path.dirname(os.path.abspath(__file__))+'/app.py')
    content = f.read()
    assert content.find("map") > 0



