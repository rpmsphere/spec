Summary: A Rubik's Cube Simulator
Name: arcus
Version: 0.3.2
Release: 6.1
License: GPL
Group: Amusements/Games
URL: http://arcus.sourceforge.net/
Source0: http://sourceforge.net/projects/arcus/files/arcus/%{name}-%{version}/%{name}-%{version}-source.tar.gz
BuildArch: noarch
BuildRequires: java-devel-openjdk lua

%description
Arcus is a Rubik's Cube Simulator written in Java featuring 3D display and
cube manipulation. Besides conventional solving, getting from any pattern
to any goal pattern is supported. Allows the user to bidirectionally walk
through the cube's history.

%prep
%setup -q -n %{name}-%{version}-source

%build
make jar

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name} $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/applications
cp %{name}.jar arcus/img/appicon.png collection.arcsp $RPM_BUILD_ROOT%{_datadir}/%{name}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
java -jar %{name}.jar
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Arcus
Comment=Rubik's Cube Simulator
Exec=%{name}
Icon=%{_datadir}/%{name}/appicon.png
Terminal=false
Type=Application
Categories=Game;Simulation;
EOF

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuild for Fedora