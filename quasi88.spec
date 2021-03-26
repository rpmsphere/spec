Name:         quasi88
License:      BSD
Group:        System/Emulators/PC
Version:      0.6.3
Release:      20.4
Summary:      NEC PC-8801 Emulator
Source:       %name-%version.tgz
Patch0:       %name-compile.patch
Patch1:       %name-rpmlint.patch
Patch2:       %name-Werror.patch
BuildRequires: gcc-c++ libtool nasm SDL-devel SDL_sound-devel SDL_mixer-devel

%description
Needs ROM images in ~/.quasi88/rom. You can use the corresponding MESS
rom set (pc88srl.zip).

%prep
%setup -q
%patch0
%patch1
%patch2 -p1
sed -i 's|0,  1, -1,  0|0,  1, 255,  0|' src/fmgen/psg.cpp

%build
CFLAGS="$RPM_OPT_FLAGS -Wno-format-security" make LSB_FIRST=1
cd tools
make CFLAGS="$RPM_OPT_FLAGS -Wno-format-security"

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 quasi88.sdl $RPM_BUILD_ROOT%{_bindir}/quasi88
install -m 755 tools/*88 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc document/* *.ini *.rc tools/*.txt
%{_bindir}/*88

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.3
- Rebuild for Fedora
* Thu Nov 27 2008 - uli@suse.de
- fixed bugs found by rpmlint
