# -*- coding: utf-8 -*-
from pathlib import Path

import pytest

from wemake_python_styleguide.violations.best_practices import (
    ExecutableMismatchViolation
)
from wemake_python_styleguide.visitors.tokenize.comments import (
    ShebangVisitor
)

_python_files_folder = Path(__file__).absolute().parent / 'test_valid_shebang_resources'

@pytest.mark.parametrize("error_code", [
    'exe001',
    'exe002',
    'exe003',
    'exe004',
    'exe005'])
def test_exe_negative(
    assert_errors,
    parse_tokens,
    default_options,
    error_code
):
    """Testing cases when no errors should be reported"""
    filename = _python_files_folder / (error_code + '_neg.py')
    with open(filename) as f:
        contents = f.read()
        file_tokens = parse_tokens(contents)
        visitor = ShebangVisitor(default_options, filename=filename, file_tokens=file_tokens)
        visitor.run()
        assert_errors(visitor,[])


@pytest.mark.parametrize("error_code", [
    'exe001',
    'exe002',
    'exe003',
    'exe004',
    'exe005'])
def test_exe_positive(
    assert_errors,
    parse_tokens,
    default_options,
    error_code
):
    """testing cases when errors should be reported"""
    filename = _python_files_folder / (error_code + '_pos.py')
    with open(filename) as f:
        contents = f.read()
        file_tokens = parse_tokens(contents)
        visitor = ShebangVisitor(default_options, filename=filename, file_tokens=file_tokens)
        visitor.run()
        assert_errors(visitor, [ExecutableMismatchViolation])
