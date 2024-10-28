Name:           yabasic
Version:        2.90.2
Release:        1
Summary:        Small basic interpreter with simple graphics and printing
Group:          Development/Languages
License:        GPLv2 or Artistic clarified
URL:            https://www.yabasic.de
Source0:        https://www.yabasic.de/download/%{name}-%{version}.tar.gz
BuildRequires:  kernel-headers
BuildRequires:  ncurses-devel
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%description
Yabasic implements the most common and simple elements of the basic
language. It comes with for-loops and goto with while-loops and
procedures.  Yabasic does monochrome line graphics, printing comes with
no extra effort.

%prep
%setup -q
#Fix rpmlint issues
chmod 0644 *.htm *.yab tests/* *.h *.c ChangeLog
sed -i -e '1d;2i#!/usr/bin/yabasic' tests/*.yab

%build
autoreconf -ifv
#libtoolize --install --copy --force
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%doc LICENSE AUTHORS ChangeLog COPYING NEWS README
%doc *.yab *.htm tests/*.yab
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.90.2
- Rebuilt for Fedora
* Mon Jan 12 2009 Fabian Affolter <fabian@bernewireless.net> - 2.763-1
- Initial package for Fedora
