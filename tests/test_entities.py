#!/usr/bin/env python
"""Tests for `flycs_sdk` package."""
# pylint: disable=redefined-outer-name

import pytest
import logging
from flycs_sdk.entities import (
    Entity,
    BaseLayerEntity,
    ParametrizedEntity,
    ParametrizedBaseLayerEntity,
)

entity_name = "test"
entity_version = "1.0.0"


class TestEntity:
    @pytest.fixture
    def my_entity(self):
        stage_config = {
            "raw": {"table_1": "1.0.0", "table_2": "1.0.0"},
            "staging": {"table_1": "1.0.0", "table_2": "1.0.0"},
        }
        return Entity(entity_name, entity_version, stage_config)

    def test_init(self, my_entity):
        assert my_entity.name == entity_name
        assert my_entity.version == entity_version

    def test_to_dict(self, my_entity):
        assert my_entity.to_dict() == {
            "name": entity_name,
            "version": entity_version,
            "stage_config": [
                {"name": "raw", "versions": {"table_1": "1.0.0", "table_2": "1.0.0"}},
                {
                    "name": "staging",
                    "versions": {"table_1": "1.0.0", "table_2": "1.0.0"},
                },
            ],
        }


class TestBaseLayerEntity(TestEntity):
    @pytest.fixture
    def empty_entity(self):
        return BaseLayerEntity(entity_name, entity_version,)

    @pytest.fixture
    def my_entity(self):
        return BaseLayerEntity(
            entity_name,
            entity_version,
            datalake_versions={"table_1": "1.0.0", "table_2": "1.0.0"},
            preamble_versions={"table_3": "1.0.0", "table_4": "1.0.0"},
            staging_versions={"table_5": "1.0.0", "table_6": "1.0.0"},
            data_warehouse_versions={"table_7": "1.0.0", "table_8": "1.0.0"},
            data_mart_versions={"table_9": "1.0.0", "table_10": "1.0.0"},
        )

    def test_to_dict(self, my_entity):
        assert my_entity.to_dict() == {
            "name": entity_name,
            "version": entity_version,
            "stage_config": [
                {
                    "name": "datalake",
                    "versions": {"table_1": "1.0.0", "table_2": "1.0.0"},
                },
                {
                    "name": "preamble",
                    "versions": {"table_3": "1.0.0", "table_4": "1.0.0"},
                },
                {
                    "name": "staging",
                    "versions": {"table_5": "1.0.0", "table_6": "1.0.0"},
                },
                {
                    "name": "data_warehouse",
                    "versions": {"table_7": "1.0.0", "table_8": "1.0.0"},
                },
                {
                    "name": "data_mart",
                    "versions": {"table_9": "1.0.0", "table_10": "1.0.0"},
                },
            ],
        }

    def test_to_dict_empty(self, empty_entity):
        assert empty_entity.to_dict() == {
            "name": entity_name,
            "version": entity_version,
            "stage_config": [
                {"name": "datalake", "versions": {},},
                {"name": "preamble", "versions": {},},
                {"name": "staging", "versions": {},},
                {"name": "data_warehouse", "versions": {},},
                {"name": "data_mart", "versions": {},},
            ],
        }


class TestParametrizedEntity(TestEntity):
    @pytest.fixture
    def my_entity(self):
        stage_config = {
            "raw": {"table_1": "1.0.0", "table_2": "1.0.0"},
            "staging": {"table_1": "1.0.0", "table_2": "1.0.0"},
        }
        return ParametrizedEntity(entity_name, entity_version, stage_config)


class TestParametrizedBaseLayerEntity(TestParametrizedEntity, TestBaseLayerEntity):
    @pytest.fixture
    def empty_entity(self):
        return ParametrizedBaseLayerEntity(entity_name, entity_version,)

    @pytest.fixture
    def my_entity(self):
        return ParametrizedBaseLayerEntity(
            entity_name,
            entity_version,
            datalake_versions={"table_1": "1.0.0", "table_2": "1.0.0"},
            preamble_versions={"table_3": "1.0.0", "table_4": "1.0.0"},
            staging_versions={"table_5": "1.0.0", "table_6": "1.0.0"},
            data_warehouse_versions={"table_7": "1.0.0", "table_8": "1.0.0"},
            data_mart_versions={"table_9": "1.0.0", "table_10": "1.0.0"},
        )
