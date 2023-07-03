%undefine _debugsource_packages
Name: termsaver
Summary: Simple text-based terminal screensaver
Version: 0.3
Release: 3.1
License: Apache License 2.0
Group: misc
URL: https://termsaver.brunobraga.net
Source0: https://github.com/brunobraga/termsaver/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires:  python2

%description
termsaver is a very simple project that aims at bringing
the feel of a screensaver feature in text-based terminal
environment.

There are many screens that can be chosen and customized
with command-line options, and the application has been
developed to accept future plugins to additional screens.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --prefix=%{_prefix}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc README.md TODO LICENSE CHANGELOG
%{_bindir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_mandir}/man1/%{name}.1.*
%{python2_sitelib}/*

%changelog
* Wed Dec 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
