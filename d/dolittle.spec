%global __spec_install_post %{nil}
%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Summary: Dolittle Programming Language
Name: dolittle
Version: 3.31
Release: 1.bin
License: Free Software
Group: Applications
Source0: dolittle331_linux.zip
Source1: dolittle.png
URL: https://dolittle.eplang.jp/
#BuildArch: noarch

%description
Dolittle is an object-oriented (O-O) programming language suitable for K12 education.
One of the authors developed a LOGO interpreter named Logob in  1990 and it was used
in many schools in Japan. 

%prep
%setup -q -c

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
FLAGS='-cp .:lib/LeapJava.jar:lib/RXTXcomm.jar:lib/commons-lang3-3.9.jar:lib/commons-text-1.8.jar:dolittle.jar -Djava.library.path=lib o3.UI'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS "\$@"
EOF

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Dolittle
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
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 3.31
- Rebuilt for Fedora
