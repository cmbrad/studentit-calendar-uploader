import json
import pytest

from mock import mock_open, patch

from studentit.config import Config


@pytest.fixture()
def config():
    return Config()


def test_config_should_originally_be_blank(config):
    assert len(config._data) == 0


def test_from_file_should_load_json_string_into_python_object(config):
    m = mock_open(read_data=json.dumps({'hello': 'world'}))
    with patch('builtins.open', m):
        assert 'hello' in config.from_file('fake_filename')._data


def test_get_should_return_default_for_keys_that_do_not_exist(config):
    assert config.get('I do not exist') is None
    assert config.get('I do not exist', 'potato') == 'potato'
