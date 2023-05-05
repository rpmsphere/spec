Summary: Design circuits using an intuitive graphical interface
Name: logisim
Version: 2.7.1
Release: 1.bin
License: Free Software
Group: Applications
URL: https://sourceforge.net/projects/circuit/
Source0: https://sourceforge.net/projects/circuit/files/2.7.x/%{version}/logisim-generic-%{version}.jar
Source1: %{name}.png
BuildArch: noarch

%description
An educational tool for designing and simulating digital logic circuits,
featuring a simple-to-learn interface, hierarchical circuits, wire bundles,
and a large component library.

%prep
%setup -q -T -c

%build
#No build

%install
install -Dm644 %{SOURCE0} %{buildroot}%{_datadir}/%{name}/%{name}.jar

# script
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/usr/bin/sh
JAVA_HOME=/usr/lib/jvm/jre
for j in \$JAVA_HOME* ; do
  [ -f \$j/bin/java ] && JAVA_HOME=\$j
done
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
FLAGS='-jar'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS %{name}.jar"\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Logisim
Comment=%{summary}
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Education;Java;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.1
- Rebuilt for Fedora
