Name: jsoko
Summary: The Sokoban game implemented in Java
Version: 2.03
Release: 1
Group: Amusements/Games
License: GPLv3
URL: http://www.sokoban-online.de/
Source0: http://sourceforge.net/projects/jsokoapplet/files/JSoko/Version%20%{version}/JSoko_%{version}-src.zip
BuildRequires: ant
BuildRequires: java-devel-openjdk lua
BuildRequires: xml-commons-apis
BuildArch: noarch
Requires: jre

%description
JSoko is a Java program for playing the Sokoban game. It features path finding,
auto push, auto solving, undo/redo, deadlock detection, and more.

%prep
%setup -q -c

%build
ant

%install
cat > %{name} <<EOF
#!/usr/bin/sh
cd %{_datadir}/%{name}
java -jar JSoko.jar
EOF
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp -a JSoko_%{version}/* %{buildroot}%{_datadir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Sep 4 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.03
- Rebuilt for Fedora
