%undefine _debugsource_packages

Name:			piedock
Version:		1.6.9
Release:		3
Summary:		A task bar and application launcher in shape of a pie menu
URL:			https://github.com/markusfisch/PieDock
Group:			User Interface/Desktops
License:		GPLv3
Source:			PieDock-%{version}.tar.gz
BuildRequires: 		libpng-devel
BuildRequires: 		libXext-devel
BuildRequires: 		libXft-devel

%description
PieDock feels a little bit like the famous OS X dock
but in shape of a pie menu which appears directly
around your mouse cursor.
Basically it shows a selection of icons that you can
use to control or launch the corresponding application.

%prep
%setup -q -n PieDock-%{version}
sed -i '14i #include <ctime>' src/WindowManager.cpp

%build
%configure
%make_build

%install
%__rm -rf %buildroot
%make_install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*

%changelog
* Sun Oct 03 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.9
- Rebuilt for Fedora
* Sat Nov 28 2015 gseaman <galen.seaman at comcast.net> 1.6.6-1gseaman2015
- 1.6.6
* Sat May 18 2013 Texstar <texstar at gmail.com> 1.6.1-2pclos2013
- fix rpmgroup
* Wed Jun 20 2012 Neal <nealbrks0 at gmail dot com> 1.6.1-1pclos2012
- process
* Wed Jun 20 2012 Archie Arevalo <pclinuxos.ph at gmail dot com> 1.6.1-1_archie_2012
- update
* Sun Jun 03 2012 Archie Arevalo <pclinuxos.ph at gmail dot com> 1.6.0-2_archie_2012
- fixed missing emblem-new.png
* Tue Apr 03 2012 Neal <nealbrks0 at gmail dot com> 1.6.0-1pclos2012
- process
* Mon Apr 02 2012 Archie Arevalo <pclinuxos.ph at gmail.com> 1.6.0-1_archie_2012
- 1.6.0
* Tue Mar 27 2012 Archie Arevalo <pclinuxos.ph at gmail.com> 1.5.0-1_archie_2012
- Initial build
