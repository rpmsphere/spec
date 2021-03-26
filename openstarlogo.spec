Name:		openstarlogo
Version:	2.22
Release:	1.bin
Summary:	A specialized version of the Logo programming language
License:	Restricted, see http://education.mit.edu/openstarlogo/index.php?option=com_content&task=view&id=17&Itemid=29
Group:		Development/Languages
Source0:	WindowsOpenStarLogo.zip
Source1:	openstarlogo.png
URL:		http://education.mit.edu/openstarlogo/
Requires:	jre
BuildArch:	noarch

%description
OpenStarLogo is a programmable modeling environment for exploring
the workings of decentralized systems -- systems that are organized
without an organizer, coordinated without a coordinator.

%prep
%setup -q -n OpenStarLogo

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp "Internal StarLogo Files/starlogo.jar" %{buildroot}%{_datadir}/%{name}/%{name}.jar
%__cp -R README.txt LICENSE.txt Templates %{buildroot}%{_datadir}/%{name}

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# openstarlogo script

JAVA_HOME=/usr/lib/jvm/jre
for j in \$JAVA_HOME* ; do
  [ -f \$j/bin/java ] && JAVA_HOME=\$j
done
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
FLAGS='-cp'
OPTIONS='starlogo.Toplevel compiler en init 100'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS %{name}.jar \$OPTIONS
EOF

# icons
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=OpenStarLogo
Comment=Programmable Modeling Environment
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Development;Java;
EOF

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Mon Jan 20 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.22
- Initial binary package
