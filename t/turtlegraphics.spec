Name:		turtlegraphics
Version:	9.36.6
Release:	1.bin
Summary:	Turtle Graphics
License:	freeware
Group:		Development/Education
Source0:	http://www.bfoit.org/itp/TG.jar
Source1:	%{name}.png
URL:		http://www.bfoit.org/itp/
Requires:	jre
BuildArch:	noarch

%description
TG is an acronym for Turtle Graphics, a well-known subset of the Logo
programming language. TG was born a library of methods, written in Java,
that could be used to do turtle graphics stuff in Java programs.

%prep
%setup -q -T -c

%install
%__rm -rf $RPM_BUILD_ROOT
%__install -Dm644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/%{name}/TG.jar

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
\$JAVACMD \$FLAGS TG.jar "\$@"
EOF

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Turtle Graphics
Comment=A well-known subset of the Logo programming language
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
* Wed Jan 29 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 9.36.6
- Initial binary package
