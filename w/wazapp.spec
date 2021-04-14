%undefine _debugsource_packages

Summary: Full featured Whatsapp client
Name: wazapp
Version: 0.9.21
Release: 7.1
License: GPLv2+
Group: Applications/Communication
Source: wazapp-master.zip
URL: https://github.com/tgalal/wazapp
BuildRequires: gcc-c++, unzip, qt-devel, python2-devel
BuildRequires: libaccounts-qt-devel
BuildRequires: libaccountsetup-devel
Requires: python-yowsup

%description
Wazapp is Harmattan's IM application for N9 that allows you to chat with your
Whatsapp buddies.

%prep
%setup -q -n %{name}-master
sed -i 's|python2\.6|python2.7|' src/wazlibs/wazlibs.pro
sed -i 's| = */| = %{buildroot}/|' src/*/*.pro

%build
cd src/accounts
qmake-qt4
make
cd ../../src/wazlibs
qmake-qt4
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a src/client/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cd src/accounts
%make_install
cd ../../src/wazlibs
%make_install

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}/opt/waxmppplugin/bin/wazapp/wazapp* %{buildroot}%{_datadir}/wazapp/wazapp*

%clean
rm -rf $RPM_BUILD_ROOT

%files
/etc/powervr.d/python.ini
/opt/waxmppplugin
/usr/lib/lib*
%{_datadir}/accounts
%{_datadir}/contextkit/providers/org.tgalal.wazapp.context
%{_datadir}/meegotouch/notifications/eventtypes/wazapp.message.new.conf
%{_datadir}/themes/*/meegotouch/icons/*.png
%{_datadir}/%{name}

%changelog
* Mon Nov 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.21
- Rebuilt for Fedora
