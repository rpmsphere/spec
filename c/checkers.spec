%undefine _debugsource_packages
Summary: Play Checkers with two people on the same computer
Name: checkers
Version: 0.2
Release: 3.1
Source0: %{name}-%{version}.tar.gz
License: MIT
Group: Games
BuildArch: noarch
URL: https://purl.oclc.org/NET/JesseW/Python
BuildRequires: python

%description
I made it to play out checkers problems I found.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{python2_sitelib}/*

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
