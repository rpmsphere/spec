%undefine _debugsource_packages
Name:		samuel
Version:	0.1.9git
Release:	1
Summary:	A Draughts Program
Group:		Games/Boards
License:	GPLv3+
URL:		http://www.johncheetham.com/projects/samuel/
Source:		%{name}-master.zip
BuildRequires:	python3-devel
Requires:       python3-gobject
Requires:	pygtk2

%description
A Draughts program for Linux written in Python, GTK, C++.
Derived from the windows program guicheckers.

%prep
%setup -q -n %{name}-master

%build
python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/%{name}-*

sed -i 's|/usr/bin/python$|/usr/bin/python3|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc LICENSE README.rst
%{_bindir}/%{name}
%{_datadir}/%{name}
%{python3_sitearch}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.9git
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.1.8-5
- (e17f99d) MassBuild#1257: Increase release tag
