%define __python /usr/bin/python2

Name: colout
Summary: Color Up Arbitrary Command Ouput
Version: 0.1
Release: 4.1
Group: Applications/Tools
License: GPL
URL: https://nojhan.github.io/colout/
Source0: nojhan-colout-v0.1-61-g566a9b2.tar.gz
BuildArch: noarch
BuildRequires: python2

%description
colout is a simple command to add colors to a text stream in your terminal.
The colout command line interface has been carefully designed to be simple.
colout has the ability to use 8 colors mode, 256 colors mode, colormaps,
themes and source code syntax coloring. Patterns are regular expressions.
You can think of colout as an alternative to grep --color which will preserve
the surrounding context, whith more powerful coloring capabilites.

%prep
%setup -q -n nojhan-colout-566a9b2

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{python2_sitelib}/%{name}*

%changelog
* Sun Jun 30 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
