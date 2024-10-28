Name:           jcchess
Version:        0.0.1git
Release:        2.1
Summary:        A chess GUI to play against chess engines
Group:          Games/Boards
License:        GPLv3+
URL:            https://www.johncheetham.com/projects/jcchess/
Source:         %{name}-master.zip
BuildRequires:  python3-devel
Requires:       python3-gobject
Requires:       python3-cairo
BuildArch:      noarch

%description
JCchess is a program to play chess against UCI chess engines.

%prep
%setup -q -n %{name}-master
sed -i 's|jchess.png|jcchess|' %{name}.desktop

%build
python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%files
%doc LICENSE README.rst ChangeLog
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1git
- Rebuilt for Fedora
