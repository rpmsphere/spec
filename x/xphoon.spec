%undefine _debugsource_packages

Summary: Phase of moon for X11
Name: xphoon
Version: 2014.08.14
Release: 3.1
Source: https://acme.com/software/xphoon/xphoon_14Aug2014.tar.gz
URL: https://acme.com/software/xphoon/
License: distributable
Group: X11/Amusements
BuildRequires: imake
BuildRequires: libX11-devel
BuildRequires: libXext-devel

%description
Xphoon sets the X root window to a picture of the moon in its current phase,
including the partial lighting of the dark side by reflected earthlight.
 
%prep
%setup -q -n %{name}

%build
xmkmf
make

%install
make DESTDIR=%{buildroot} install install.man

%files
%doc README
%{_bindir}/xphoon
%{_mandir}/man1/xphoon.1x.*

%changelog
* Tue Dec 26 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2014.08.14
- Rebuilt for Fedora
