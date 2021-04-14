Summary: PowerPC Architecture Emulator
Name: pearpc
Version: 0.5
Release: 31.1
Group: Applications/Emulators
License: GPL
URL: http://pearpc.sourceforge.net/
Source0: http://download.sf.net/pearpc/pearpc-%{version}.tar.gz
Source1: http://pearpc.sourceforge.net/pearpc3.png
Source2: http://download.sf.net/pearpc/pearpc-3gib.img.bz2
Source3: http://download.sf.net/pearpc/pearpc-6gib.img.bz2
BuildRequires: xorg-x11-proto-devel, SDL-devel
BuildRequires: desktop-file-utils, gcc-c++
BuildRequires: nasm
Patch0: pearpc-fix-no-return-in-nonvoid-function.patch
Patch1: pearpc-fix-ambiguates-old-declaration.patch

%description
PearPC is an architecture-independent PowerPC platform emulator capable of
running most PowerPC operating systems.

%prep
%setup -q
### FIXME: Fix /usr/lib(64) for x86_64. (Please fix upstream)
%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure
%patch0
%patch1
sed -i 's|ht_printf(".*"msg)|ht_printf(msg)|' src/debug/tracers.h
sed -i 's|ht_printf(".*"a)|ht_printf(a)|' src/system/ui/sdl/sysdisplay.cc

%build
%configure --enable-ui=sdl --enable-cpu=generic
sed -i 's|-DHAVE_CONFIG_H|-DHAVE_CONFIG_H -fPIC -fno-strict-aliasing -Wno-narrowing|' `find . -name Makefile`
sed -i 's|-Werror=format-security|-Wno-format-security|' `find . -name Makefile`
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall

# Create the system menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=PearPC
Comment=PowerPC Architecture Emulator
Exec=ppc %{_sysconfdir}/ppc.conf
Icon=pearpc.png
Terminal=false
Type=Application
Categories=Application;Utility;
Encoding=UTF-8
EOF

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor "" \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications \
    %{name}.desktop

# Icon for the desktop file
%{__install} -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/pearpc.png

# Example (patched) configuration file
%{__install} -D -m 0644 ppccfg.example $RPM_BUILD_ROOT%{_sysconfdir}/ppc.conf

# Empty compressed disk images + video driver
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/pearpc/emptyimages
%{__install} -m 0644 %{SOURCE2} %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/pearpc/emptyimages/
%{__install} -m 0644 video.x $RPM_BUILD_ROOT%{_datadir}/pearpc/

# Change some paths in the configuration file
%{__perl} -pi -e \
    's|^(prom_driver_graphic =).*|$1 "%{_datadir}/pearpc/video.x"|g;
     s|^(pci_ide0_master_image =).*|$1 "%{_datadir}/pearpc/pearpc-3gib.img"|g' \
    $RPM_BUILD_ROOT%{_sysconfdir}/ppc.conf

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog README TODO ppccfg.example
%config(noreplace) %{_sysconfdir}/ppc.conf
%{_bindir}/ppc
%{_datadir}/pixmaps/pearpc.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pearpc/
%{_mandir}/man1/ppc.1*

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Wed Sep 22 2004 Matthias Saou <http://freshrpms.net/> 0.3.1-1
- Update to 0.3.1.
* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Added fixes for x86_64.
* Wed Aug 25 2004 Matthias Saou <http://freshrpms.net/> 0.3.0-1
- Update to 0.3.0.
* Thu Jul 15 2004 Matthias Saou <http://freshrpms.net/> 0.2.0-1
- Update to 0.2.0 and cleanups.
* Tue May 11 2004 Che
- initial rpm release
- very quickly done but its an experimental release anyways
