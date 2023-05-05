%global _name NetLogo
%undefine _debugsource_packages

Summary: A multi-agent programmable modeling environment
Name: netlogo
Version: 5.2.1
#Version: 6.3.0
Release: 1.bin
License: Free Software
Group: Applications
Source0: http://ccl.northwestern.edu/netlogo/%{version}/%{name}-%{version}.tar.gz
URL: http://ccl.northwestern.edu/netlogo/
ExclusiveArch: x86_64

%description
NetLogo is the next generation of the series of multi-agent modeling languages
including StarLogo and StarLogoT for simulating natural and social phenomena.

%prep
%setup -q

%build
#No build

%install
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

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
FLAGS='-Djava.library.path=./lib -Djava.ext.dirs= -Dfile.encoding=UTF-8 -jar'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS %{_name}.jar "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{_name}
Comment=%{summary}
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Education;Java;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert icon.ico $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 5.2.1
- Rebuilt for Fedora
