%global _version 20140826-r5761

Name:		drjava
Version:	20140826.r5761
Release:	1.bin
Summary:	A lightweight java programming environment
License:	BSD
Group:		Development/Tools
Source0:	http://sourceforge.net/projects/drjava/files/1.%20DrJava%20Stable%20Releases/drjava-stable-%{_version}/drjava-stable-%{_version}.jar
Source1:	http://sourceforge.net/projects/drjava/files/1.%20DrJava%20Stable%20Releases/drjava-stable-%{_version}/readme.txt
Source2:	%{name}.png
URL:		http://drjava.sourceforge.net/
Requires:	jre
BuildArch:	noarch

%description
DrJava is a lightweight programming environment for Java designed to foster
test-driven software development. It includes an intelligent program editor,
an interactions pane for evaluating program text, a source level debugger,
and a unit testing tool.

%prep
%setup -q -T -c

%build

%install
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp %{SOURCE0} %{SOURCE1} %{buildroot}%{_datadir}/%{name}

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
\$JAVACMD \$FLAGS %{name}-stable-%{_version}.jar
EOF

# icons
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=DrJava
Comment=A lightweight java programming environment
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
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jan 28 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 20140826.r5761
- Initial binary package
