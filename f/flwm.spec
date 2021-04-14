Summary: The fast light window manager
Name: flwm
Version: 1.16
Release: 12.1
License: GPLv2
Group: System/GUI/Other
Source: https://github.com/bbidulock/flwm/releases/download/%{version}/%{name}-%{version}.tgz
Patch0: flwm-1.16.patch
URL: http://flwm.sourceforge.net
BuildRequires: gcc-c++
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: fltk-devel

%description
Flwm is my attempt to combine the best ideas I have seen in several
window managers. The primary influence and code base is from wm2
by Chris Cannam. This is an enhanced version by the Tiny Core team.

%prep
%setup -q
%patch0 -p1

%build
./configure --prefix=/usr --mandir=%{_datadir}/man
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/man/man1/%{name}.1.*

%changelog
* Mon Jul 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.16
- Rebuilt for Fedora
