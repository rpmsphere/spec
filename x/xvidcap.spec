Summary: An X-Windows screen capture tool
Name: xvidcap
Version: 1.1.7
Release: 1
License: GPLv2
Source0: https://sourceforge.net/projects/xvidcap/%{name}-%{version}.tar.gz
Group: Applications/Multimedia
URL: https://xvidcap.sourceforge.net
BuildRequires: gettext
BuildRequires: libXmu-devel
BuildRequires: scrollkeeper
BuildRequires: lame-devel, libvorbis-devel
##BuildRequires: ffmpeg-devel >= 0.4.8
BuildRequires: perl(XML::Parser)
BuildRequires: libglade2-devel
BuildRequires: dbus-devel dbus-glib-devel
Requires: mplayer
Obsoletes: gvidcap < %{version}
Provides: gvidcap = %{version}

%description
xvidcap is a screen capture tool for creating videos off
an X-Window desktop for illustration or documentation purposes. 
It is intended to be a standard-based alternative for 
commercial tools, such as Lotus ScreenCam or Camtasia Studio.

%prep
%setup -q 
sed -i 's/shmstr/shmproto/' src/capture.c

%build
export CC=clang CXX=clang++
export LIBS="-lX11 -lXext -lz"
%configure
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -fr %{buildroot}/usr/doc
rm -fr %{buildroot}%{_datadir}/doc/%{name}
ln -s %{name} %{buildroot}%{_bindir}/gvidcap
%find_lang %{name}

echo -e 'Name[zh_TW]=極限螢幕錄影\nComment[zh_TW]=X11 螢幕攝影' >> %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc README INSTALL AUTHORS ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}-dbus-client
%{_bindir}/gvidcap
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/omf/%{name}
%{_datadir}/gnome/help/%{name}
%{_datadir}/dbus-1/services/net.jarre_de_the.Xvidcap.service
%{_mandir}/man1/%{name}*.1*
%{_mandir}/*/man1/%{name}*.1*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.7
- Rebuilt for Fedora
* Fri Aug 01 2008 Paulo Roma <roma@lcg.ufrj.br> - 1.1.7-10
- Updated to 1.1.7
- Removed vversion.
* Sun Feb 03 2008 Paulo Roma <roma@lcg.ufrj.br> - 1.1.7-9_rc1
- Updated to 1.1.7rc1
- Removed shenv patch.
- Included BR dbus-glib-devel.
* Mon Oct 22 2007 Paulo Roma <roma@lcg.ufrj.br> - 1.1.6-9
- Patched for being shell independent.
- Added gettext as a BuilRequirement for find_lang.
* Sat Oct 13 2007 Paulo Roma <roma@lcg.ufrj.br> - 1.1.6-8
- Update to 1.1.6.
- Removed deprecated patches.
- Changed package description.
- Removed unnecessary BuildRequires.
- Using supplied desktop entry and icon.
* Wed Nov 29 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.1.4p1-7
- Update to 1.1.4p1.
* Wed Sep  6 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.1.4-5_rc1
- Update to 1.1.4.
* Wed Jan 04 2006 Paulo Roma <pcavalcanti@devel.atrpms.net>
- Fedora 4 build of gvidcap
- ffmpeg patch to compile it with CC (gcc32).
* Sun May 10 2004 Snorri <snorri_dj@operamail.com>
- First fedora build of gvidcap
