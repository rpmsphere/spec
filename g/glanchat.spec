Name: glanchat
Summary: Chat in local network
Version: 0.0.8
Release: 8.1
Group: Applications/Communications
License: GPLv2
URL: https://glanchat.sourceforge.net/
Source0: https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  libXau-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXrender-devel
BuildRequires:  atk-devel
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libX11-devel
BuildRequires:  libpng-devel
BuildRequires:  pango-devel
BuildRequires:  libxml2-devel
BuildRequires:  zlib-devel

%description
Ethernet chat compatible with popular Lanchat Pro (UDP chat in local network).
Uses gtk+ and gettext.

%prep
%setup -q

%build
export LDFLAGS="-Wl,--allow-multiple-definition -lX11"
%configure
make %{?_smp_mflags} CFLAGS+=-Wno-format-security

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}/usr/doc %{buildroot}%{_datadir}/doc

%files
%{_bindir}/%{name}
%{_datadir}/doc/%{name}
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%changelog
* Sun Jun 02 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.8
- Rebuilt for Fedora
* Mon Feb 12 2007 qla<qla0@vp.pl> 0.0.8.2-2qla
- porawione dodawanie do menu
* Wed Feb 07 2007 qla<qla0@vp.pl> 0.0.8.6qla
- wydanie dla Pclos2007
* Sat Apr 08 2006 <qla0@vp.pl> 0.0.8.5qla
- poprawki w spec-u
* Thu Mar 02 2006 <qla0@vp.pl> 0.0.8.4qla
- good old style recieving ip
- fixed problems with saving config files
- you can open links in private chat
- German translation (by John Gibbon <john@punksyndikat.de>)
- new icons and logo (by John Gibbon <john@punksyndikat.de>)
- if pictures on picture arrow insted --->
- fixed not checking links only
- you can add options to browsers
- improved trayicon
- ignore case for links
