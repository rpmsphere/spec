Name:           jwm
Version:        2.2.3
Release:        0%{?dist}
Summary:        Joe's Window Manager

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://joewing.net/programs/jwm
#Source0:        http://joewing.net/programs/jwm/releases/%{name}-%{version}.tar.xz
Source0:	jwm-master.zip
Source1:        %{name}.desktop
Patch0:         %{name}-nostrip.patch
Patch1:         %{name}-timestamps.patch

BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libXft-devel
BuildRequires:  fribidi-devel
BuildRequires:  freetype-devel
BuildRequires:  gettext
BuildRequires:  cairo-devel
BuildRequires:  librsvg2-devel
Requires:       xterm

%description
JWM is a window manager for the X11 Window System. JWM is written in C and uses
only Xlib at a minimum. The following libraries can also be used if available:

* libXext for the shape extension
* libXrender for the render extension
* libXmu for drawing rounded windows (shape extension also needed)
* libXinerama for Xinerama support
* libXpm for XPM backgrounds and icons
* libjpeg for JPEG backgrounds and icons
* libpng for PNG backgrounds and icons
* librsvg2 for PNG backgrounds and icons
* libXft for antialiased and true type fonts
* fribidi for right-to-left language support

JWM supports MWM and Extended Window Manager Hints (EWMH).

%prep
%setup -q -n jwm-master

# Do not strip binary file
%patch0 -p0 -b .orig

# Preserve timestamps in installation
%patch1 -p0 -b .orig

%build
autoreconf
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/xsessions
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/

%find_lang %{name}

%files -f %{name}.lang
%doc LICENSE README.md
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/system.jwmrc
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/%{name}.*

%changelog
* Fri Sep 12 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.3-0
- Updated to git master

* Wed Feb 12 2014 Germán A. Racca <skytux@fedoraproject.org> - 2.2.0-1
- Updated to new upstream version 2.2.0
- Cleaned spec file
- Changed tarball format (from bz2 to xz)
- Recreated patches jwm-nostrip and jwm-timestamps
- Dropped patch jwm-destdir
- Added translations
- Added gettext as BR

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.1.0-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.1.0-3
- rebuild against new libjpeg

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 09 2012 Germán A. Racca <skytux@fedoraproject.org> - 2.1.0-1
- Updated from snapshot to new release
- Rearranged spec file

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-8.svn500
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.0.1-7.svn500
- Rebuild for new libpng

* Tue Aug 30 2011 Germán A. Racca <skytux@fedoraproject.org> 2.0.1-6.svn500
- Added patch to remove strip from makefile
- Recreated the other patches and changed order of application
- Removed optflags from make line

* Mon Aug 22 2011 Germán A. Racca <skytux@fedoraproject.org> 2.0.1-5.svn500
- Added optflags to the make line
- Replaced libjpeg-devel by libjpeg-turbo-devel in BR
- Added freetype-devel as BR

* Fri Aug 19 2011 Germán A. Racca <skytux@fedoraproject.org> 2.0.1-4.svn500
- Added xterm as requires
- Modified release tag format

* Sun Jan 09 2011 Germán A. Racca <skytux@fedoraproject.org> 2.0.1-3.20110108svn
- Updated to snapshot 20110108
- Removed some patches because they were fixed by upstream

* Thu Jun 17 2010 German A. Racca <gracca@gmail.com> 2.0.1-2.20100616svn
- Rebuild for Fedora 13
- Updated to snapshot 20100616

* Wed May 19 2010 German A. Racca <gracca@gmail.com> 2.0.1-1.20100503svn
- Initial release of RPM package
