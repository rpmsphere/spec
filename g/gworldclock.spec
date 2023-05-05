Name:	gworldclock
Version: 1.4.4
Release: 1
Summary: Displays time and date in specified time zones
License: GPL
Group: Toys
URL: http://pkgs.org/debian-sid/debian-main-amd64/gworldclock_1.4.4-9_amd64.deb.html
Source:	%{name}-%{version}.tar.xz
Source1: gworldclock.desktop
Source2: gworldclock.png
Patch0:	gworldclock_1.4.4-9.patch
BuildRequires: autoconf
BuildRequires: gettext
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: pango-devel
BuildRequires: libxml2-devel

%description
Displays time and date in specified time zones.

%prep
%setup -q
%patch0 -p 1

%build
#export CFLAGS='-O2 -Wno-format-security -flto=auto -ffat-lto-objects -fexceptions -g -grecord-gcc-switches -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection  -Wl,-z,relro -Wl,--as-needed  -Wl,-z,now -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1'
export CFLAGS='-g -O2 -Wno-format-security -fPIC'
%configure
%make_build

%install
rm -rf %buildroot
%make_install

mkdir -p %buildroot/%{_datadir}/applications
install -m 0644 %SOURCE1 %buildroot/%{_datadir}/applications

mkdir -p %buildroot/%{_datadir}/pixmaps
install -m 0644 %SOURCE2 %buildroot/%{_datadir}/pixmaps

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/gworldclock
%{_bindir}/tzwatch
%{_datadir}/man/man1/gworldclock.1*
%{_datadir}/man/man1/tzwatch.1*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Sun Mar 26 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.4
- Rebuilt for Fedora
* Sun May 17 2015 bb <bb> 0.8.0-2pclos2015
- import
