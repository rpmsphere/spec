%undefine _debugsource_packages

Summary: Showing Miku Miku Dance 3D models
Name: dunan
Version: 0.6
Release: 10.6
License: GPL
Group: User Interface/Desktops
Source0: http://www.frostworx.de/dunan/%{name}-%{version}.tar.bz2
URL: http://www.frostworx.de/?p=64
BuildRequires: gcc-c++, SDL-devel, SDL_mixer-devel
BuildRequires: libXrender-devel, ftgl-devel, libmmd-devel, bullet-devel
Requires: mmd-data
Patch0: dunan-0.6-makefile.patch

%description
Dunan is a little program which shows (animated) Miku Miku Dance 3D models
(pmd) on the linux desktop. It also supports Miku Miku Dance motion files
(vmd) and has a builtin settings menu and mouse/keyboard control functions.

%prep
%setup -q
%patch0

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README Changelog TODO
%{_bindir}/%{name}

%changelog
* Mon May 23 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
