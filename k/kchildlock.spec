%undefine _debugsource_packages

Name: kchildlock
BuildRequires: kdelibs kdelibs-devel perl-Data-Dumper perl-Digest perl-Digest-MD5 qca
Summary: Restricts Computer Usage Time of Children
Version: 0.91.1
Release: 1
License: GPL
Group: System/Management
Source0: kchildlock-0.91.1.tar.gz
URL: https://sourceforge.net/projects/kchildlock

%description
This tool monitors and restricts the usage time of the computer. It is intended
to limit childrens time spent on the computer. The limits can be specified per
day of week and by lower and upper hour, and daily usage time. Limits for
applications are possible too.

%prep
%setup -q

%build
cmake -DCMAKE_BUILD_TYPE=release \
	-DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT/usr -DHTML_INSTALL_DIR=$RPM_BUILD_ROOT/usr/share/doc/kde/HTML \
	-DCONFIG_INSTALL_DIR=$RPM_BUILD_ROOT/usr/share/kde4/config -DCMAKE_SKIP_RPATH=ON
make -j 2

%install
install -m 755 -d %{_tmppath}/%{name}_%{version}-%{release}-build/usr/share/doc/kde/HTML/en/common
/usr/bin/cmake -DDESTDIR=$RPM_BUILD_ROOT -P cmake_install.cmake 
rm -f ${RPM_BUILD_ROOT}/usr/share/doc/kde/HTML/en/kcontrol/kchildlock/common
ln -sf /usr/share/doc/kde/HTML/en/common ${RPM_BUILD_ROOT}/usr/share/doc/kde/HTML/en/kcontrol/kchildlock/common

cd $RPM_BUILD_ROOT

find . -type d -fprint $RPM_BUILD_DIR/file.list.%{name}.dirs
find . -type f -fprint $RPM_BUILD_DIR/file.list.%{name}.files.tmp
sed '/\/man\//s/$/.gz/g' $RPM_BUILD_DIR/file.list.%{name}.files.tmp > $RPM_BUILD_DIR/file.list.%{name}.files
find . -type l -fprint $RPM_BUILD_DIR/file.list.%{name}.libs
sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' $RPM_BUILD_DIR/file.list.%{name}.dirs > $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.files >> $RPM_BUILD_DIR/file.list.%{name}
sed 's,^\.,\%attr(-\,root\,root) ,' $RPM_BUILD_DIR/file.list.%{name}.libs >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
/usr/lib*/kde*/kcm_kchildlock.so
/usr/lib*/kde*/kded_kchildlockdaemon.so
/usr/share/kde*/config/kchildlockrc
/usr/share/kde*/services/kcm_kchildlock.desktop
/usr/share/kde*/services/kded/kchildlockdaemon.desktop
/usr/share/doc/kde*/HTML/en/kcontrol/kchildlock/*
/usr/share/locale/*/LC_MESSAGES/kchildlock.mo
/usr/share/icons/hicolor/*/apps/kchildlock.png
/var/opt/kchildlock/dummy.txt

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.91.1
- Rebuilt for Fedora
