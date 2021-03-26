Name:		osp-tracker
Version:	4.95
Release:	1.bin
Summary:	Video analysis and modeling tool
License:	opensource
Group:		Education
Source0:	http://physlets.org/tracker/archives/tracker-%{version}.jar
Source1:	%{name}.png
URL:		http://physlets.org/tracker/
Requires:	jre
BuildArch:	noarch

%description
Tracker is a free video analysis and modeling tool built on
the Open Source Physics (OSP) Java framework. It is designed
to be used in physics education.

%prep
%setup -q -T -c

%install
%__rm -rf $RPM_BUILD_ROOT
%__install -Dm644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/%{name}/tracker.jar

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# %{name} script

JAVA_HOME=/usr/lib/jvm/jre
for j in \$JAVA_HOME* ; do
  [ -f \$j/bin/java ] && JAVA_HOME=\$j
done
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
FLAGS='-jar'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS tracker.jar "\$@"
EOF

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Tracker
Comment=Video analysis and modeling tool
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
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Feb 02 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 4.95
- Initial binary package
