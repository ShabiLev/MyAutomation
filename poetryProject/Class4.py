# After adding to toml
#
# [tool.poetry.dependencies]
# python = "^3.11"
#
# run "poetry install"
## or
## run from terminal "poetry add [package]==[version]"
# C:\Users\shabil\AppData\Roaming\pypoetry\venv\Scripts\poetry add requests==2.28.2


# assert will give TRUE or FALSE
def inc(x):
    return x+1

def test_answer():
    assert inc(4) == 5 # TRUE
    assert inc(4)==6 # FASLE x=4

test_answer()