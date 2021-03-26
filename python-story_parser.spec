Name:           python-story_parser
Version:        0.1.2
Release:        2.1
URL:            http://github.com/hugobr/story_parser
Summary:        A Given/When/Then BDD stories parser
License:        MIT
Group:          Development/Languages/Python
Source:         http://pypi.python.org/packages/source/s/story_parser/story_parser-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildArch:      noarch

%description
This project is a start towards writing text stories to pyhistorian, 
but it can be used out of it.
It parsers a string file like::

Story: Writing a parser
As a pyhistorian contributor
I want to add support to stories written in text
So that everyone can use it, even the stakeholders

Scenario 1: Getting Title
  Given I have a story like this one
  When I try parse it and get the title
  Then I get "Writing a parser" title

%prep
%setup -q -n story_parser-%{version}

%build
export CFLAGS="%{optflags}"
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2
- Rebuild for Fedora
* Sat Jul 23 2011 toms@suse.de
- Initial version 0.1.2
