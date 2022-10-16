%global debug_package %{nil}

Name:           fakexrandr
Version:        0.20211207
Release:        1
URL:            https://github.com/phillipberndt/fakexrandr
Summary:        Fake XRandR configurations for multi-head setups
License:        GPLv3
Group:          System Environment/Libraries
Source:         https://codeload.github.com/phillipberndt/fakexrandr/zip/master#/%{name}-master.zip
BuildRequires:  python2
BuildRequires:  libXrandr-devel
BuildRequires:  libXinerama-devel
BuildRequires:  xorg-x11-server-devel
Requires:       filesystem-local

%description
This is a tool to cheat an X11 server to believe that there are more monitors
than there actually are. It hooks into libXRandR and libXinerama and replaces
certain, configurable monitor configurations with multiple virtual monitors.
A tool that comes with this package can be used to configure how monitors are
split.

This tool used to only work with XRandR, but I found it useful to add Xinerama
emulation. It can be readily removed if it isn't needed though. Note that this
tool right now only works for legacy Xlib applications. Applications using xcb
will not work.

%prep
%setup -q -n %{name}-master
cat > config.h <<EOF
#define XRANDR_MAJOR 1
#define XRANDR_MINOR 5
#define XRANDR_PATCH 1
#define REAL_XRANDR_LIB "%{_libdir}/libXrandr.so.2"
#define FAKEXRANDR_INSTALL_DIR "/usr/local/%{_lib}"
EOF

%build
make

%install
rm -rf %{buildroot}
install -Dm755 libXrandr.so %{buildroot}/usr/local/%{_lib}/libXrandr.so
#install -Dm755 libXrandr.so %{buildroot}/usr/local/%{_lib}/libXrandr.so.2.2.0
#ln -s libXrandr.so.2.2.0 %{buildroot}/usr/local/%{_lib}/libXrandr.so.2
install -Dm755 fakexrandr-manage.py %{buildroot}%{_bindir}/fakexrandr-manage

sed -i 's|/usr/bin/env python$|/usr/bin/python3|' %{buildroot}%{_bindir}/%{name}*

%clean
rm -rf %{buildroot}

%files
%doc README.md
%{_bindir}/fakexrandr-manage
/usr/local/%{_lib}/libXrandr.so*

%changelog
* Sun Oct 02 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20211207
- Rebuild for Fedora
