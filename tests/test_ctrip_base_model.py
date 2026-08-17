import unittest

from python_ctrip import CtripBaseModel
from python_ctrip.approval.model import CtripBaseModel as ApprovalBaseModel
from python_ctrip.basedata.model import CtripBaseModel as BaseDataBaseModel
from python_ctrip.details.model import CtripBaseModel as DetailsBaseModel
from python_ctrip.people.model import CtripBaseModel as PeopleBaseModel
from python_ctrip.sso.model import CtripBaseModel as SSOBaseModel


class ExampleModel(CtripBaseModel):
    name: str
    optional_value: str | None = None


class CtripBaseModelTests(unittest.TestCase):
    def test_domain_models_share_the_public_base_model(self):
        self.assertIs(ApprovalBaseModel, CtripBaseModel)
        self.assertIs(BaseDataBaseModel, CtripBaseModel)
        self.assertIs(DetailsBaseModel, CtripBaseModel)
        self.assertIs(PeopleBaseModel, CtripBaseModel)
        self.assertIs(SSOBaseModel, CtripBaseModel)

    def test_serialization_ignores_none_and_unknown_fields(self):
        model = ExampleModel(name="Ctrip", unexpected="ignored")

        self.assertEqual(model.model_dump(), {"name": "Ctrip"})
        self.assertEqual(model.model_dump_json(), '{"name":"Ctrip"}')


if __name__ == "__main__":
    unittest.main()
