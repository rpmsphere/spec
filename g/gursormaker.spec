%undefine _debugsource_packages
Name: gursormaker
Summary: A cursor editor for X11 using GTK+
Version: 0.6.0
Release: 5.1
Group: Development/Libraries
License: GPL
URL: https://gursormaker.sourceforge.net
Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  python2
BuildArch: noarch
Requires: python-numeric
Requires: xorg-x11-apps

%description
A graphical user interface that allows manipulating cursor themes for X11.
It provides an option to import themes made for Stardock CursorXP. 

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{python2_sitelib}/GursorMaker
%{python2_sitelib}/gursormaker-*.egg-info

%changelog
* Wed Mar 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.0
- Rebuilt for Fedora
