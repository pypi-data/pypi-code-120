from openfisca_us.model_api import *


class is_permanently_disabled_veteran(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    documentation = (
        "Indicates whether a person is a permanently disabled veteran"
    )
    label = "Permanently disabled veteran"
