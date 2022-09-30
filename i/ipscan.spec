Summary:        A fast and friendly network scanner
Name:           ipscan
Version:        3.8.2
Release:	1.bin
License:        GPLv2+
Group:          Applications/Internet
URL:            http://angryip.org
Source0:	%{name}-%{version}.tar.gz
Source1:	https://github.com/angryip/ipscan/releases/download/%{version}/ipscan-linux64-%{version}.jar
#BuildRequires:  java-11-openjdk-devel lua
#BuildRequires:  ant
#BuildRequires:  fakeroot
#BuildRequires:  git
BuildArch:      noarch
Requires:	jre

%description
Angry IP Scanner is a cross-platform network scanner written in Java.
It can scan IP-based networks in any range, scan ports, and resolve
other information.

The program provides an easy to use GUI interface and is very extensible.

%prep
%setup -q
#sed -i -e '/target="package-linux.*-deb-rpm"/d' -e 's|1\.6|1.7|g' build.xml
#sed -i 's|©|(C)|' src/net/azib/ipscan/config/Version.java
#sed -i -e 's|⌦|Del|' -e 's|⌘C|Ctrl+C|' src/net/azib/ipscan/gui/menu/CommandsMenu.java

%build
#ant linux64
mkdir dist
cp %{SOURCE1} dist

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/ipscan $RPM_BUILD_ROOT/%{_datadir}/applications $RPM_BUILD_ROOT/%{_datadir}/pixmaps $RPM_BUILD_ROOT/%{_bindir}
cp dist/*.jar $RPM_BUILD_ROOT/%{_datadir}/ipscan/ipscan.jar
cp ext/deb-bundle/usr/share/applications/ipscan.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/
cp resources/images/icon128.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/ipscan.png
echo "#/bin/sh" > $RPM_BUILD_ROOT/%{_bindir}/ipscan
echo "java -jar %{_datadir}/ipscan/ipscan.jar" >> $RPM_BUILD_ROOT/%{_bindir}/ipscan
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ipscan

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE README.md CHANGELOG TODO.md
%{_datadir}/ipscan/ipscan.jar
%{_datadir}/applications/ipscan.desktop
%{_datadir}/pixmaps/ipscan.png
%{_bindir}/ipscan

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.8.2
- Rebuilt for Fedora
