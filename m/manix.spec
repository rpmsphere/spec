%undefine _debugsource_packages

Name: manix
Version: 0.6
Release: 8.1
Summary: MacOS 8/9 alike UI
License: GPLv2
Group: User Interface/Desktops
URL: https://sourceforge.net/projects/manix/
Source0: https://sourceforge.net/projects/manix/files/%{name}/%{version}/%{name}-%{version}.tgz
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXext-devel
BuildRequires: libXpm-devel
BuildRequires: xorg-x11-xbitmaps

%description
A free implementation of the MacOS 8/9 userinterface and experience,
using X11 as the graphical backend.

%prep
%setup -q

%build
make

%install
install -d %{buildroot}%{_bindir}
install -m755 %{name}-wm/%{name}-wm %{buildroot}%{_bindir}
install -m755 %{name}-keys/%{name}-keys %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install -m644 %{name}-wm/%{name}-wm.conf %{buildroot}%{_datadir}/%{name}/%{name}-wm.conf
install -m644 %{name}-wm/README %{buildroot}%{_datadir}/%{name}/%{name}-wm.README
install -m644 %{name}-keys/keys %{buildroot}%{_datadir}/%{name}/keys
install -m644 %{name}-keys/README %{buildroot}%{_datadir}/%{name}/%{name}-keys.README

%files
%{_bindir}/%{name}-wm
%{_bindir}/%{name}-keys
%{_datadir}/%{name}

%changelog
* Thu Feb 06 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
