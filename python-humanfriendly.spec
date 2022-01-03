%bcond_with tests

%global srcname humanfriendly

Name:           python-%{srcname}
Version:        10.0
Release:        1
Summary:        Human friendly output for text interfaces using Python

License:        MIT
URL:            https://%{srcname}.readthedocs.io
Source0:        https://github.com/xolox/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%{?python_provide:%python_provide python-%{srcname}}

%if %{with tests}
BuildRequires:  python-capturer
BuildRequires:  python-coloredlogs
BuildRequires:  python-pytest
%endif # with_tests

%description
The functions and classes in the humanfriendly package can be used to make text
interfaces more user friendly. Some example features:

- Parsing and formatting numbers, file sizes, pathnames and timespans in
  simple, human friendly formats.
- Easy to use timers for long running operations, with human friendly
  formatting of the resulting timespans.
- Prompting the user to select a choice from a list of options by typing the
  option's number or a unique substring of the option.
- Terminal interaction including text styling (ANSI escape sequences), user
  friendly rendering of usage messages and querying the terminal for its size.


%package doc
Summary:        Documentation for the '%{srcname}' Python module
BuildRequires:  python-sphinx

%description doc
HTML documentation for the '%{srcname}' Python module.

%prep
%autosetup


%build
%py_build

# Don't install the tests.py
rm build/lib/%{srcname}/tests.py

#sphinx-build-%{python_version} -nb html -d docs/build/doctrees docs docs/build/html
#rm docs/build/html/.buildinfo


%install
%py_install


%if 0%{?with_tests}
%check
PYTHONUNBUFFERED=1 py.test-%{python_version} %{srcname}/tests.py
%endif # with_tests


%files doc
%license LICENSE.txt
#doc docs/build/html

%files
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{python_sitelib}/%{srcname}/
%{python_sitelib}/%{srcname}-%{version}-py%{python_version}.egg-info/
%{_bindir}/%{srcname}
