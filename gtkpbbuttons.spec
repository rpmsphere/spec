Name:           gtkpbbuttons
URL:            http://pbbuttons.berlios.de/projects/gtkpbbuttons/
Summary:        Graphical PBButtons Client
Version:        0.6.10
Release:        156.1
Group:          System/Daemons
License:        GPL v2 or later
Source:         %{name}-%{version}.tar.gz
Patch:          %{name}-%{version}.diff
BuildRequires:  libpng-devel
BuildRequires:  audiofile-devel gtk2-devel pbbuttonsd-devel popt-devel

%description
This package contains a PBButtons Client: GTKPBButtons.

This client for pbbuttonsd displays small pop-up windows each time a
message from the daemon pbbuttonsd appears. The view of each pop-up can
be individually configured. The following windows could pop up:

- brightness level The current display brightness level would be
   displayed.

- keyboard illumination level The current keyboard brightness level
   would be displayed.

- volume level The current volume level would be displayed

- mute The window shows if the speakers were muted.

- battery warning This window shows that battery is running low and
   how long it would last until shutdown. The last warning level
   indicates that the machine will be shut down immediately to save
   data integrity.

- sleep warning This windows shows that the computer is going to
   enter sleep mode.

- trackpad This window shows the current trackpad operating mode.

- ejecting CD-ROM This window signals that a CD-ROM will be ejected
   or why it cannot be.

The window appears after someone has pressed one of the special keys or
an event message has been received. After approximately two seconds
without any changes, the pop-up window vanishes again.

Authors:
--------
    Matthias Grimm <matthiasgrimm@users.sourceforge.net>

%prep
%setup -q
%patch

%build
%configure CFLAGS="$RPM_OPT_FLAGS -lm" --prefix=/usr --mandir=%{_mandir}
make

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %name

%clean
rm -fr $RPM_BUILD_ROOT

%files -f %name.lang
/usr/bin/*
%{_mandir}/man?/*.gz
/usr/share/gtkpbbuttons

%changelog
* Fri Jul 01 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.10
- Rebuild for Fedora
* Mon Oct 20 2008 schwab@suse.de
- Add ExclusiveArch.
* Mon Jul  9 2007 schwab@suse.de
- Update to gtkpbbuttons 0.6.10.
  * no sound if started as daemon - fixed.
  * update source to compile with autotools 1.9.
  * update copyright notice
* Mon Oct  9 2006 schwab@suse.de
- Update to gtkpbbuttons 0.6.9.
  * fix a possible seqfault
  * correct display if no backlight controler is available
  * fix a bug in session handling.
  * LCD and keyboard max values increased to 100 becasue since version
    0.7.9 pbbuttonsd sends values in percent.
* Mon Jun  5 2006 schwab@suse.de
- Don't keep audio device open.
- Don't clobber CFLAGS.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Jul  7 2005 schwab@suse.de
- Update to gtkpbbuttons 0.6.8.
* Tue May  3 2005 schwab@suse.de
- Update to gtkpbbuttons 0.6.7.
* Sun Apr 17 2005 schwab@suse.de
- Add audiofile-devel to nfb.
* Mon Apr 11 2005 schwab@suse.de
- Update to gtkpbbuttons 0.6.6.
* Fri Apr  8 2005 schwab@suse.de
- Fix for new libpbbipc API.
* Thu Jan 27 2005 schwab@suse.de
- Update to gtkpbbuttons 0.6.5.
* Sun Sep 19 2004 schwab@suse.de
- Initial version 0.6.4.
