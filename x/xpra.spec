Summary: Persistent remote applications for X
Name: xpra
Version: 0.8.7
Release: 33.1
License: GPL
Requires: pygtk2, xorg-x11-server-utils, xorg-x11-server-Xvfb, python-imaging, dbus-python, python-uuid
Group: Networking
URL: http://xpra.org/
Source: http://xpra.org/src/%{name}-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: pygtk2-devel, setuptool, Cython, pygobject2-devel, gtk2-devel, libXtst-devel, libvpx-devel, libXdamage-devel
#BuildRequires: x264-devel
BuildRequires: ffmpeg-compat-devel

%description
Xpra gives you "persistent remote applications" for X. That is, unlike normal
X applications, applications run with xpra are "persistent" -- you can run
them remotely, and they don't die if your connection does. You can detach them,
and reattach them later -- even from another computer -- with no loss of state.
And unlike VNC or RDP, xpra is for remote applications, not remote desktops --
individual applications show up as individual windows on your screen, managed
by your window manager. They're not trapped in a box. So basically it's screen
for remote X apps.

%prep
%setup -q
sed -i 's|0, 16|0, 15|' setup.py

%build
export PKG_CONFIG_PATH=%{_libdir}/ffmpeg-compat/pkgconfig
export CFLAGS=-I/usr/include/ffmpeg-compat
python setup.py build --without-x264

%install
python setup.py install -O1  --prefix /usr --skip-build --root $RPM_BUILD_ROOT
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{python_sitearch}/*
%{_datadir}/xpra
%{_datadir}/parti
%{_datadir}/wimpiggy
%{_datadir}/icons/*
%{_datadir}/applications/*
%{_datadir}/man/man1/*
/etc/*

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.7
- Rebuilt for Fedora
