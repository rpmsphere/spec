Name:		gshogi
Version:	0.5.1git
Release:	2.1
Summary:	A program to play Shogi
Group:		Games/Boards
License:	GPLv3+
URL:		http://www.johncheetham.com/projects/gshogi/
Source:		%{name}-master.zip
BuildRequires:	python3-devel
Requires:       python3-gobject
Requires:	python3-cairo

%description
gshogi is a program to play Shogi (Japanese Chess). It has a builtin engine and
can also use USI engines. It is written in python3 and C and runs on GTK3 (PyGI)
desktops.

%prep
%setup -q -n %{name}-master

%build
python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc LICENSE README.rst ChangeLog
%{_bindir}/%{name}
%{python3_sitearch}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1git
- Rebuild for Fedora
