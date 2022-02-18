# SPDX-FileCopyrightText: 2022 Daniele Tentoni <daniele.tentoni.1996@gmail.com
#
# SPDX-License-Identifier: MIT

"""Test Yaml Configuration parsing.
"""
# Standard Library
from textwrap import dedent

import pytest  # type: ignore
import yaml  # type: ignore

# Codechecker
from cc_codechecker.project import Project, get_project


def test_expect_verr_missing_language():
  yml = dedent('''\
    language:
    ''')
  dic = yaml.full_load(yml)
  with pytest.raises(ValueError) as err:
    get_project(dic)
  assert 'Failed to add {\'language\': None}' in str(err.value)

@pytest.mark.parametrize('language', ['A', 'Cobol'])
def test_except_verr_unknown_language(language: str):
  with pytest.raises(ValueError) as err:
    Project(language)
  message = f'Language {language} is not supported by codechecker'
  assert message in str(err.value)

@pytest.mark.parametrize('yml', ['language: A', 'language: Cobol'])
def test_except_verr_convert_missing_language(yml: str):
  dic = yaml.full_load(yml)
  with pytest.raises(ValueError) as err:
    get_project(dic)
  assert f'Failed to add {dic}' in str(err.value)

@pytest.mark.parametrize('project', [
  Project('bash'),
  Project('csharp'),
])
def test_project_repr(project: Project):
  proj_repr: str = project.__repr__()
  assert project.language in proj_repr
  assert 'Project' in proj_repr

def test_write_proj():
  proj = Project('bash')
  doc = yaml.dump(proj.dump())
  assert dedent('''\
    language: bash
  ''') == doc

def test_read_proj():
  print('Project')
  proj = dedent("""\
    language: bash
    """)
  print(proj)
  yaml_loaded = yaml.full_load(proj)
  assert isinstance(yaml_loaded, dict)
  project = get_project(yaml_loaded)
  assert 'bash' == project.language
