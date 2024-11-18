%undefine _debugsource_packages

Name: terminol
Summary: A simple terminal emulator
Version: 0.5
Release: 20.1
Group: Applications/Emulators
License: GPLv3
URL: https://github.com/bagnose/terminol
Source0: %{name}-master.zip
BuildRequires: python
BuildRequires: pango-devel, cairo-devel, fontconfig-devel, libxkbcommon-devel, pcre-devel
BuildRequires: xcb-proto, libxcb-devel, xcb-util-keysyms-devel, xcb-util-wm-devel, xcb-util-devel

%description
terminol is a simple Linux/X11 VT220 terminal emulator featuring reflowed
Unicode text, enormous history support with line deduplication, client-server
mode (optional), user defined key bindings, 24-bit color, minimal dependencies,
and a small resource footprint.

%prep
%setup -q -n %{name}-master
sed -i '/Werror/d' common.mak
sed -i '11i #include <limits>' terminol/common/deduper_interface.hxx
sed -i '13i #include <cstdint>' terminol/support/conv.hxx terminol/support/cache.hxx

%build
./configure build release gnu
make -C build %{?_smp_mflags}

%install
make -C build install INSTALLDIR=%{buildroot}/usr

%files
%doc COPYING README.md
%{_bindir}/*

%changelog
* Thu Dec 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
