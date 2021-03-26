Summary: Connect6 game written in Java
Name: meinstein
Version: 2009
Release: 8.1
License: GPLv3
Group: Amusements/Games
Source: TheosConnect6.zip
URL: http://www.csvn.nl/downloads/doc_download/176-meinstein-connect6
BuildRequires: java-devel-openjdk, ant, xml-commons-apis, lua
BuildArch: noarch
Requires: jre

%description
This MeinStein Connect6 release contains the code as left by Theo van der
Storm (1960- 2009) for his Connect6 program. The program won silver in the
2007 (Amsterdam) and 2009 (Pamplona) Computer Games Olympiad as organised
by the ICGA.

%prep
%setup -q -n TheosConnect6
sed -i 's|/Users/jan/Documents/workspace/TheosConnect6/||' nbproject/private/private.properties

%build
ant -Dplatforms.JDK_1.6.home=/usr/lib/jvm/java

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a dist/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
java -jar %{_datadir}/%{name}/MeinSteinConnect6.jar
EOF
 
%files 
%doc README COPYING USAGE
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Fri Nov 01 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2009
- Rebuild for Fedora
