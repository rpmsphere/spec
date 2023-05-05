%global _name GloboNote

Summary: Create sticky notes, to-do list, journals & reminders all in one app
Name: globonote
Version: 1.6
Release: 1.bin
License: BSD
Group: Applications
Source0: https://jaist.dl.sourceforge.net/project/globonote/globonote/GloboNote-%{version}/%{name}-%{version}.tar.gz
URL: https://globonote.info/
Requires: jre
BuildArch: noarch

%description
GloboNote is a 100% free and easy to use desktop note taking application.
Packed with useful features that can run on any OS (Windows, Linux, Mac OS).
You can use it to create sticky notes, to-do lists, personal journals,
reminders and other notes all in one application. There are no limits to
the number of sticky notes you can create. Notes can have different colors,
assigned to different groups and searched using search tool.

%prep
%setup -q -n %{_name}

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
Name=GloboNote
Comment=%{summary}
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Office;Java;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -Dm644 doc/images/%{name}16.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuilt for Fedora
