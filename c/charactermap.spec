%undefine _debugsource_packages
Name: charactermap
Version: 4.3.2
Release: 1
Summary: Character Map in Qt4
License: GPL
Group: Applications/Utility
Source0: https://jserv.sayya.org/misc/%{name}.tar.bz2
Source1: charactermap.png
BuildRequires: qt4-devel

%description
The Character Map example shows how to create a custom widget
that can both display its own content and respond to user input.

%prep
%setup -q -n %{name}

%build
qmake-qt4 charactermap.pro -o Makefile.qt
make -f Makefile.qt

%install
%__rm -rf %{buildroot}
%__install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
%__install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Character Map
Name[zh_TW]=字型查看工具
Comment=Character Map in Qt4
Comment[zh_TW]=Qt4 內附的字型查看工具
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Utility;
EOF

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.3.2
- Rebuilt for Fedora
