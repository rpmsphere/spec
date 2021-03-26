%define __os_install_post %{nil}

Name:         jstock
Summary:      Free stock market software
URL:          http://jstock.org/
Group:        Applications/Productivity
License:      GPL
Version:      1.0.7.17
Release:      1.bin
Source0:      https://github.com/yccheok/jstock/releases/download/release_%(echo %version | tr . -)/%{name}-%{version}-bin.zip
Source1:      %{name}.png
Requires:     jre
BuildArch:    noarch

%description
JStock makes it easy to track your stock investment. It provides well
organized stock market information, to help you decide your best
investment strategy.

%prep
%setup -q -n %{name}

%build
#ant

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a * %{buildroot}%{_datadir}/%{name}

# script
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# jstock script

JAVA_HOME=/usr/lib/jvm/jre
for j in \$JAVA_HOME* ; do
  [ -f \$j/bin/java ] && JAVA_HOME=\$j
done
JAVACMD=\$JAVA_HOME/bin/java
JAVA_LIBDIR=/usr/share/java
FLAGS='-Xms64m -Xmx512m -jar'

cd /usr/share/%{name}
\$JAVACMD \$FLAGS %{name}.jar
EOF

# icons
%__install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# freedesktop.org menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=JStock
Comment=Free stock market software
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Network;Java;
EOF

%clean
%__rm -rf %{buildroot}

%files
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Dec 12 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.7.17
- Initial binary package
