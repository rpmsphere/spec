Name:			aquanukex-cursor-theme
Summary:		A cursor os x like theme for X11
License:		GPL v2 or later
Version:		0.2
Release:		18.1
Source:			Aqua-NukeX.tar.gz
BuildArch:		noarch
URL:			http://www.kde-look.org/content/show.php?content=30238
Group:			System/X11/Icons

%description
This is an animated cursor theme, MacOSX style.

Authors:
--------
		Gianluca Turrini

%prep
%setup -q -n Aqua-NukeX

%build

%install
%__install -d $RPM_BUILD_ROOT%{_datadir}/icons/Aqua-NukeX
%__mv cursors index.theme $RPM_BUILD_ROOT%{_datadir}/icons/Aqua-NukeX/

%clean  
rm -rf $RPM_BUILD_ROOT 

%files
%{_datadir}/icons/Aqua-NukeX

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
* Wed May 13 2009 Matthias Propst 0.2-8
- used opensuse build service
- made some changes in specfile
* Tue Mar 31 2009 Matthias Propst 0.2-MP7
- fixed messed up prefix
* Tue Mar 31 2009 Matthias Propst 0.2-MP6
- added BuildArch tag
* Mon Mar 30 2009 Matthias Propst 0.2-MP5
- changed Distribution name to Vendor Opensuse 11.0 unofficial
- write a short warning about opensuse unofficial
- added Provides, Requires and BuildRoot
- fixed some issues, so now its more suse-alike
* Thu Feb 12 2009 Matthias Propst 0.2-MP4
- finaly made a package for opensuse 11.0
- generated srcrpm
* Tue Feb 13 2007 Matthias Propst <penguinuser(at)web.de> 0.2-3
- fixed the ugly white square bug
* Fri Dec 01 2006 Pascal Bleser <guru@unixtech.be> 0.1-2
- fixed installation path on SUSE 10.2/Xorg 7
- rewrote spec file
* Sat Oct 15 2005 Pascal Bleser <guru@unixtech.be> 0.1-1
- new package
