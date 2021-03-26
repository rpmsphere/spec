%global debug_package %{nil}

Name:            subtle
Version:         0.11.3224
Release:         25.1
Summary:         A grid-based manual tiling window manager
Group:           User Interface/Desktops
License:         GPL
URL:             http://subforge.org/projects/subtle
Requires:        rubypick ruby rxvt-unicode
BuildRequires:   rubypick ruby-devel rubygem-rake rubygem-rdoc libX11-devel libXpm-devel xorg-x11-proto-devel freetype-devel
Source0:         http://subforge.org/attachments/download/81/%{name}-%{version}-xi.tbz2
Source1:         %{name}.desktop

%description
Subtl Window Manager has a strong focus on easy but customizable look and feel.
In comparison to other tiling window managers, subtle has no automatic tiling of
the screen size in any way. Instead, windows are arranged according to positions
inside of a grid. These positions are called gravities. 

Authors:
--------
    --- Christoph Kappel <unexist@dorfelite.net>
        ICQ: 33679091, IRC: #subtle / irc.freenode.org

%prep
%setup -q -n %{name}-%{version}-xi
sed -i -e '260,263d' -e 's|-I\.|-I. -I/usr/include/freetype2 -Wno-incompatible-pointer-types|' Rakefile
sed -i '1i #include <ruby.h>' src/shared/shared.h

%build
rake destdir=$RPM_BUILD_ROOT sysconfdir=$RPM_BUILD_ROOT/etc bindir=$RPM_BUILD_ROOT/usr/bin datadir=$RPM_BUILD_ROOT/usr/share/subtle/ mandir=$RPM_BUILD_ROOT/%_mandir manprefix=$RPM_BUILD_ROOT/%_mandir help

%install
rake install
mv %{buildroot}/usr/local/share/ruby/* %{buildroot}%{_datadir}/ruby
install -d %{buildroot}%{_mandir}/man1
mv %{buildroot}/usr/share/man/*.1 %{buildroot}%{_mandir}/man1
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/%{name}.desktop



%files
%doc ChangeLog AUTHORS INSTALL COPYING NEWS
/etc/xdg/subtle
%{_bindir}/*
%{_datadir}/ruby/%{name}
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*.1.*

%changelog
* Mon Feb 10 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.3224
- Rebuild for Fedora
* Sun Jan  8 2012 seiler@b1-systems.de
- added dependency for rxvt-unicode (main terminal emulator used in subtle)
* Mon Dec 26 2011 seiler@b1-systems.de
- added desktop file to shown in several display managers (gdm, lightdm, kdm)
- fixed some rpmlint warnings
* Mon Nov 21 2011 seiler@b1-systems.de
- enhanced description
* Mon Nov 21 2011 seiler@b1-systems.de
- made spec file more generic
* Mon Nov 21 2011 seiler@b1-systems.de
- removed self provide in spec file
* Mon Nov 21 2011 seiler@b1-systems.de
- added 3 missing directories to 'files' section
* Mon Nov 21 2011 seiler@b1-systems.de
- created files section. including attributes...
* Mon Nov 21 2011 seiler@b1-systems.de
- changed pathes in help / configure section
* Mon Nov 21 2011 seiler@b1-systems.de
- modified rake parameters to install the builded files correctly in an build environment. example: (docdir=$RPM_BUILD_ROOT)
* Mon Nov 21 2011 seiler@b1-systems.de
- added patch to build subtle without '-Werror'
* Mon Nov 21 2011 seiler@b1-systems.de
- another dependency...
* Mon Nov 21 2011 seiler@b1-systems.de
- another dependency 'xorg-x11-libXpm'
* Mon Nov 21 2011 seiler@b1-systems.de
- did a few failbuilds
- added some dependencies to get this thing work
* Thu Nov 17 2011 seiler@b1-systems.de
- added rake to configure and make process
* Thu Nov 17 2011 seiler@b1-systems.de
- a few changes in spec file to the build process work
* Thu Nov 17 2011 seiler@b1-systems.de
- added build dependencies and added ruby1.9 to my home project
* Wed Nov 16 2011 seiler@b1-systems.de
- initial build for openSUSE 12.1
