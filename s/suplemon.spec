Name: suplemon
Summary: Console (CLI) text editor with multi cursor support
Version: 0.2.1
Release: 1
Group: Development/Editors
License: MIT
URL: https://github.com/richrd/suplemon
Source0: https://codeload.github.com/richrd/suplemon/tar.gz/v%{version}#/%{name}-%{version}.tar.gz
BuildRequires: python3-devel python3-setuptools
BuildArch: noarch
Requires: python3-wcwidth
Requires: python3-pegments
Requires: xsel

%description
Suplemon is a modern, powerful and intuitive console text editor with multi
cursor support. Suplemon replicates Sublime Text style functionality in the
terminal with the ease of use of Nano.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=/usr

%files
%doc LICENSE *.md docs/*
%{_bindir}/*
%{python3_sitelib}/*

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuilt for Fedora
