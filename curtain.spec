Name:		curtain
Version:	0.3
Release:	6.1
License:	GPLv3
Group:		Education
URL:		http://code.google.com/p/ardesia
Source:		http://ardesia.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-desktop-file.patch
Patch1:		%{name}-0.3-gtk3tests.patch
Summary:	Show a movable and resizable curtain on the desktop screen
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	glib2-devel
BuildRequires:	gtk3-devel
BuildRequires:	desktop-file-utils

%description
Curtain is a tool that show a movable and resizable curtain
on the desktop screen.

You can use this to hide and show objects on the desktop.
This program has been implemented for educational purposes.

%prep
%setup -q
%patch0
%patch1 -p1 -b .gtk3tests

%build
./autogen.sh
%configure
make

%install
%make_install

install -d -m 755 %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/icons/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README NEWS ChangeLog AUTHORS
%{_bindir}/curtain
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/ui/%{name}.glade
%{_datadir}/%{name}/ui/icons/%{name}.*
%exclude %{_datadir}/icons/%{name}.ico
%{_datadir}/pixmaps/%{name}.*
%{_mandir}/man1/%{name}.1.*

%changelog
* Fri Sep 23 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Thu Feb 04 2016 umeabot <umeabot> 0.3-6.mga6
+ Revision: 935453
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 0.3-5.mga5
+ Revision: 744791
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.3-4.mga5
+ Revision: 678641
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 0.3-3.mga4
+ Revision: 503653
- Mageia 4 Mass Rebuild
* Fri Jan 11 2013 umeabot <umeabot> 0.3-2.mga3
+ Revision: 348500
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Mon Jan 07 2013 matteo <matteo> 0.3-1.mga3
+ Revision: 340394
- patch1: fixed gtk3 test
- added missing build requirement (gtk+3.0-devel)
- added missing build requirement (libtool)
- fixed build
- new version
* Sun Dec 09 2012 matteo <matteo> 0.2-3.mga3
+ Revision: 329046
- fixed menu icon not shown issue
- spec file reviewed
* Thu Jan 05 2012 matteo <matteo> 0.2-2.mga2
+ Revision: 191867
- spec file reviewed; patch unzipped
* Fri Dec 23 2011 matteo <matteo> 0.2-1.mga2
+ Revision: 186745
- libgtk+2.0-devel as br
- libglib2.0-devel as br
- intltool as br
- imported package curtain
