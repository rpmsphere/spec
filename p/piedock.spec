%undefine _debugsource_packages

Name:			piedock
Version:		1.6.9
Release:		2.1
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

%build
%configure
%make_build
sh/instant

%install
%__rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT%_datadir/%name
cp %{name}-instant-*.bin $RPM_BUILD_ROOT%_datadir/%name

%post
/sbin/ldconfig
cd %_datadir/%name/
./%{name}-instant-*.bin
mkdir -p %_datadir/icons/gnome/48x48/emblems
cp %_datadir/icons/oxygen/48x48/emblems/emblem-new.png %_datadir/icons/gnome/48x48/emblems/ 

%postun
/sbin/ldconfig
rm -rf %_datadir/%name/%{name}-instant

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%_datadir/%name

%changelog
* Thu Feb 01 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.9
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
