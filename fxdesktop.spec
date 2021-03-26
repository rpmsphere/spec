%global debug_package %{nil}

Name: fxdesktop
Summary: Lightweight Desktop Environment
Version: 0.1.12r14
Release: 13.1
Group: User Interface/Desktops
License: GPLv3
URL: http://code.google.com/p/fxdesktop/
Source0: %{name}-master.zip
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXft-devel
BuildRequires: libXcursor-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libXfixes-devel
BuildRequires: libXi-devel
BuildRequires: freetype-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: fox-devel
BuildRequires: fox-utils
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel

%description
FOX Desktop is lightweight desktop environment compatible with EWMH capable
window managers.

%prep
%setup -q -n %{name}
sed -i 's|reswrap|fox-reswrap|' configure*

%build
./configure --prefix=/usr
make

%install
install -Dm755 src/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/%{name}

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.12r14
- Rebuild for Fedora
