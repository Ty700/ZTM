# In python, there are no true private members

# Instead, we do self._age <= Standard for a "private" variable

class PlayerCharacter:
    def __init__(self, name, age):
        # Py3 community agree to treat _<var_name> variables as private
        # However, it is not actually private
        self._age = age
        self._name = name 