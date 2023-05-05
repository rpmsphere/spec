%global _name StarChess

Summary: Mini Space Conquest
Name: starchess
Version: 2.1.0
Release: 1.bin
License: Free Software
Group: Applications
Source0: http://kynosarges.org/project/StarChess.zip
Source1: %{name}.png
URL: http://kynosarges.org/StarChess.html
BuildRequires: unzip
BuildArch: noarch
Requires: jre

%description
Star Chess is an abstract 4X strategy game that I wrote to experiment
with turn prediction algorithms.

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
FLAGS='-jar'

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
Categories=Application;Game;Java;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuilt for Fedora
