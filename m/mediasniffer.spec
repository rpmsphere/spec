%global debug_package %{nil}

Name: mediasniffer
Summary: Sniff download links of online media
Version: 1.0.0.11
Release: 11.4
Group: Applications/Internet
License: GPL
URL: http://sourceforge.net/projects/mediasniffer/
Source0: %{name}-linux-src-1.0.0.11.tar.bz2
BuildRequires:  libICE-devel
BuildRequires:  ORBit2-devel
BuildRequires:  libSM-devel
#BuildRequires:  art_lgpl_2-devel
BuildRequires:  atk-devel
#BuildRequires:  bonobo-activation-devel
#BuildRequires:  bonobo-devel
#BuildRequires:  bonoboui-devel
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
#BuildRequires:  gconf-devel
BuildRequires:  gdk-pixbuf2-devel
#BuildRequires:  gmodule-devel
#BuildRequires:  gnome-devel
#BuildRequires:  gnomecanvas-devel
BuildRequires:  libgnomeui-devel
#BuildRequires:  gnomevfs-devel
#BuildRequires:  gthread-devel
BuildRequires:  gtk2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpng-devel
BuildRequires:  pango-devel
BuildRequires:  libpcap-devel
BuildRequires:  popt-devel
BuildRequires:  w3m udisks2

%description
Sniff download links of media when you watching online videos, listening to
online musics or downloading from iTunes.

%prep
%setup -q -c

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_datadir}/pixmaps/%{name}/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%{_sysconfdir}/pam.d/%{name}
%{_sysconfdir}/security/console.apps/%{name}
%{_bindir}/%{name}
%{_sbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{name}
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun May 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0.11
- Rebuild for Fedora
* Tue May 17 2011 CTQY <qiyi.caitian@gmail.com>
- Initial package
