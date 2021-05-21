Summary: BASIC in Java
Name: jbasic
Version: 2.8
Release: 8.1
License: GPL
Group: Development/Languages
Source: http://sourceforge.net/projects/jbasic/files/JBasic%20Source/JBasic%202.8/%{name}28.tar.gz
URL: http://sourceforge.net/projects/jbasic/
BuildRequires: java-openjdk-devel, ant, lua
BuildArch: noarch
Requires: jre

%description
JBasic is a traditional BASIC language intepreter written in Java for command
line or embedded use. It supports conventional GW-BASIC style syntax, plus some
modern extensions for supporting threads, JDBC, etc. JBasic can be run directly
from a shell.

%prep
%setup -q -n %{name}

%build
ant

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 %{name}.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.jar
install -d $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
java -jar %{_datadir}/%{name}/%{name}.jar
EOF
 
%files 
%doc *.TXT
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Sep 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.8
- Rebuilt for Fedora
