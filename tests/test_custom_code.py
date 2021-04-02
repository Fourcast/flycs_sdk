import pytest

from flycs_sdk.custom_code import CustomCode, WrongSignatureError


class TestCustomCode:
    def test_imported_modules(self):
        def build(dag, env=None):
            from airflow.operators.dummy_operator import DummyOperator
            import os

            return DummyOperator(dag=dag)

        cc = CustomCode("mycode", "1.0.0", build, requirements=["airflow==1.10.0"])
        assert cc.requirements == ["airflow==1.10.0"]

    def test_validation_signature_builder(self):
        def build():
            from airflow.operators.dummy_operator import DummyOperator

            return DummyOperator()

        with pytest.raises(WrongSignatureError):
            cc = CustomCode("mycode", "1.0.0", build)

        def build(dag, env=None):
            from airflow.operators.dummy_operator import DummyOperator

            return DummyOperator()

        cc = CustomCode("mycode", "1.0.0", build)
