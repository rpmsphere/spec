%define _name WhereIsM13

Name:		whereism13
Version:	2.3
Release:	1.bin
Summary:	A Three Dimensional Galactic Atlas
License:	Freeware
Group:		Applications/Education
Source0:	http://www.thinkastronomy.com/M13/downloads/%{_name}_%{version}.zip
Source1:	%{_name}.png
URL:		http://www.thinkastronomy.com/M13/
Requires:	jre
BuildArch:	noarch

%description
Where is M13? is a unique application that helps you visualize the locations
and physical properties of deep sky objects in and around the Galaxy.

%prep
%setup -q -c

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a Where\ is\ M13/* %{SOURCE1} %{buildroot}%{_datadir}/%{name}

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# %{_name} script

JAVA_HOME=/usr/lib/jvm/jre
for j in \$JAVA_HOME* ; do
  [ -f \$j/bin/java ] && JAVA_HOME=\$j
done
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
FLAGS='-jar'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS %{_name}.jar
EOF

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Where is M13?
Comment=A Three Dimensional Galactic Atlas
Exec=%{name}
Terminal=false
Type=Application
Icon=/usr/share/%{name}/%{_name}.png
Encoding=UTF-8
Categories=Application;Education;
EOF

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Jan 23 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3
- Initial binary package
