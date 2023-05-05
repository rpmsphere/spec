Summary: Java + Turtle
Name: jurtle
Version: 1.8.1
Release: 1.bin
License: Free Software
Group: Applications
Source0: Jurtle_1.8.1.zip
URL: https://www.otherwise.com/jurtle.html
BuildRequires: unzip
BuildArch: noarch

%description
Jurtle is a simple integrated development tool for learning to program
in the Java programming language. Perfect for a high school curriculum
or for anyone else just starting out.

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
FLAGS='-DBrowserCmd=/usr/bin/firefox -cp ".:Jurtle.jar:AStylePlugin.jar:\$JAVA_HOME/lib/tools.jar" com.otherwise.jurtle.Splash'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Jurtle
Comment=%{summary}
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Education;Java;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -Dm 644 User_Manual/Resources/jurtle64x64.gif $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.gif

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.1
- Rebuilt for Fedora
