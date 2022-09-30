Summary: Connect6 improved
Name: connect6-ng
Version: 0.3
Release: 9.1
License: GPLv3
Group: Amusements/Games
Source: %{name}-%{version}.tar.gz
URL: https://github.com/alick9188/connect6-ng
BuildRequires: java-devel-openjdk, ant, xml-commons-apis, lua
#BuildRequires: ant-findbugs
BuildArch: noarch
Requires: jre

%description
This is connect6-ng, a fork of connect6 project. The project aims at improving
the old project in several aspects.

%prep
%setup -q
sed -i '14d' build.xml

%build
ant -Drepository.version=%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m644 build/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
java -jar %{_datadir}/%{name}/%{name}-%{version}.jar
EOF
 
%files 
%doc LICENSE_GPLv3.txt README.markdown
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Nov 01 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
