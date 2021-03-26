%global debug_package %{nil}
%global __python %{__python3}

Name: kitty
Summary: Fast, featureful, GPU based terminal emulator
Version: 0.14.6
Release: 1
Group: System/X11
License: GPLv3
URL: https://github.com/kovidgoyal/kitty
Source0: https://github.com/kovidgoyal/kitty/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: %{name}.1
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  environment-modules
BuildRequires:  ImageMagick-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libpng-devel
BuildRequires:  libwayland-egl-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  pkgconfig(dbus-1)

%description
Kitty supports modern terminal features like: graphics, unicode,
true-color, OpenType ligatures, mouse protocol, focus tracking, and
bracketed paste.

Kitty has a framework for "kittens", small terminal programs that can be used
to extend its functionality.

%prep
%setup -q

%build
#python3 setup.py build

%install
python3 setup.py linux-package
install -d %{buildroot}/usr
cp -a linux-package/* %{buildroot}/usr

%files
%doc LICENSE *.md *.rst *.asciidoc
%{_bindir}/%{name}
/usr/lib/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_mandir}/man1/%{name}.1.*
%{_docdir}/kitty/html
%{_datadir}/terminfo/x/xterm-kitty

%changelog
* Mon Oct 14 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.14.6
- Rebuild for Fedora
