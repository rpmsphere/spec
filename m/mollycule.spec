%global _name MollyCule

Summary: A chemistry visualisation package
Name: mollycule
Version: 1.0
Release: 1.bin
License: Free Software
Group: Applications
Source0: MollyCule.tgz
URL: http://mollycule.org/
BuildArch: noarch

%description
MollyCule is designed primarily for non-experts and hobby enthusiasts.
It doesn't have all the complicated functions and mathematical features that
a researcher would need - instead, it has many features that will make it
great for school pupils and students; in particular, a special animated
'fly-through' mode that automatically tries to guide you through the molecule.
It's also designed to make it easy to set up nice screen shots that can be 
included in chemistry essays and project documents. It can produce animations
automatically in real-time, that are very suitable for using alongside
a powerpoint presentation.

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
Categories=Application;Education;Java;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -Dm644 mollycule/resource/splashscreen.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
