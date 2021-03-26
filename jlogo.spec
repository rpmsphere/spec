Name:		jlogo
Version:	2.4.0
Release:	1.bin
Summary:	A Logo interpreter written in Java
License:	freeware
Group:		Development/Education
Source0:	http://guillot.emmanuel.free.fr/jLogo/download-jLogo/v2.4.0/jLogo.zip
Source1:	%{name}.png
URL:		http://guillot.emmanuel.free.fr/jLogo/
Requires:	jre
BuildArch:	noarch

%description
It's written to be compatible with a Logo made by Nathan which was available
on the Thomson TO7, MO5, MO6...However, the features are more from this
millenium than from the last one : all the fonts in your system are available,
216 colors (web safe), play tunes using QuickTime...
Author:		emmanuel.guillot 'at' wanadoo.fr

%prep
%setup -q -c

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -R jLogo/* %{buildroot}%{_datadir}/%{name}

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
\$JAVACMD \$FLAGS jLogo.jar
EOF

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=jLogo
Comment=Logo interpreter written in Java
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Education;Java;
EOF

%__mkdir_p %{buildroot}%{_datadir}/pixmaps
install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Jan 20 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.0
- Initial binary package
