%global debug_package %{nil}
%global __os_install_post %{nil}

Name:		netlogo
Version:	5.0.5
Release:	1.bin
Summary:	A cross-platform multi-agent programmable modeling environment
License:	Freeware
Group:		Development/Languages
Source:		http://ccl.northwestern.edu/%{name}/%{version}/%{name}-%{version}.tar.gz
URL:		http://ccl.northwestern.edu/netlogo/
Requires:	jre
BuildRequires:	ImageMagick

%description
NetLogo was authored by Uri Wilensky in 1999 and is under
continuous development at the CCL (the people who brought
you StarLogoT). NetLogo also powers the HubNet participatory
simulation system. NetLogo is free of charge.

%prep
%setup -q
%ifarch %{ix86}
rm -rf lib/Linux-amd64
#rm -rf extensions/gogo/lib/Linux-amd64
%else
rm -rf lib/Linux-x86
#rm -rf extensions/gogo/lib/Linux-x86
%endif

%build

%install
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -R * %{buildroot}%{_datadir}/%{name}

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# netlogo script

JAVA_HOME=/usr/lib/jvm/jre
for j in \$JAVA_HOME* ; do
  [ -f \$j/bin/java ] && JAVA_HOME=\$j
done
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
FLAGS='-server -Djava.library.path=./lib -Djava.ext.dir= -XX:MaxPermSize=128m -Xss16m -Xmx1024m -Dfile.encoding=UTF-8 -jar'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS NetLogo.jar "\$@"
EOF

%__cat > %{buildroot}%{_bindir}/%{name}-3D << EOF
#!/bin/sh
#
# netlogo-lite script

JAVA_HOME=/usr/lib/jvm/jre
for j in $JAVA_HOME* ; do
  [ -f \$j/bin/java ] && JAVA_HOME=\$j
done
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
FLAGS='-Djava.library.path=./lib -Djava.ext.dir= -XX:MaxPermSize=128m -Xss16m -Xmx1024m -Dfile.encoding=UTF-8 -Dorg.nlogo.is3d=true -jar'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS NetLogo.jar "\$@"
EOF

%__cat > %{buildroot}%{_bindir}/%{name}-headless << EOF
#!/bin/sh
#
# netlogo-headless script

JAVA_HOME=/usr/lib/jvm/jre
for j in \$JAVA_HOME* ; do
  [ -f \$j/bin/java ] && JAVA_HOME=\$j
done
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
FLAGS='-Xss16m -Xmx1024m -Dfile.encoding=UTF-8 -classpath'
OPTIONS='org.nlogo.headless.Main'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS NetLogo.jar \$OPTIONS "\$@"
EOF

# icons
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
unzip -j NetLogo.jar images/icon16.gif
convert icon16.gif %{buildroot}%{_datadir}/pixmaps/%{name}.png

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=NetLogo
Comment=Programmable Modeling Environment
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Development;Java;
EOF

%files
%attr(0755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Mon Jan 20 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0.5
- Initial binary package
