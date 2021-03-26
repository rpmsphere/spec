Name:		gnunet
Version:	0.13.3
Release:	1
License:	GPLv2+
Summary:	Secure and anonymous peer-to-peer file sharing
URL:		http://gnunet.org/
Source0:	ftp://ftp.gnu.org/gnu/gnunet/%{name}-%{version}.tar.gz
Source1:	gnunetd.conf
Source2:	init_gnunetd
Group:		Networking/File transfer
BuildRequires:  libpng-devel
BuildRequires:	libextractor-devel
BuildRequires:	libxml2-devel
BuildRequires:	curl-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	gawk
BuildRequires:	gmp-devel
BuildRequires:	gettext-devel
BuildRequires:	sqlite-devel
BuildRequires:	mysql-devel
BuildRequires:	zlib-devel
BuildRequires:	openssl-devel
BuildRequires:	libmicrohttpd-devel
BuildRequires:	ncurses-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	libunistring-devel
BuildRequires:	libidn-devel
BuildRequires:	glpk-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	opus-devel
BuildRequires:	gstreamer1-devel
BuildRequires:	atlas
Requires:		redhat-lsb-core

%description
GNUnet is a framework for secure peer-to-peer networking that does not
use any centralized or otherwise trusted services. A first service
implemented on top of the networking layer allows anonymous censorship-
resistant file-sharing. GNUnet uses a simple, excess-based economic
model to allocate resources. Peers in GNUnet monitor each others behavior
with respect to resource usage; peers that contribute to the network
are rewarded with better service.

%package devel
Summary:	Development files for lib%{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q
mv AUTHORS AUTHORS.old
iconv -f ISO_8859-1 -t UTF-8 AUTHORS.old -o AUTHORS

%build
%configure
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall
%{__mkdir_p} $RPM_BUILD_ROOT/var/lib/gnunet
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_initrddir}
%{__install} -m0755 %{SOURCE2} $RPM_BUILD_ROOT%{_initrddir}/%{name}d
%{__ln_s} %{_datadir}/%{name}/config.d $RPM_BUILD_ROOT%{_sysconfdir}/gnunet.d
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%find_lang %{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%pre
useradd -r gnunetd -d /var/lib/gnunet -s /bin/false ||:

%post
systemctl restart %{name}d ||:

%preun
systemctl stop %{name}d ||:

%postun
userdel gnunetd ||:

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README COPYING
%attr(0700, gnunetd, gnunetd) %dir /var/lib/gnunet
%config %{_sysconfdir}/gnunet.d
%{_initrddir}/%{name}d
%{_bindir}/*
%{_libdir}/%{name}
%{_libexecdir}/*
%{_datadir}/%{name}
%{_mandir}/man?/%{name}*
%{_libdir}/lib%{name}*.so.*
%exclude %{_datadir}/info/dir
%{_datadir}/info/%{name}.*
%{_datadir}/info/images/*

%files devel
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

%changelog
* Mon Sep 07 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.13.3
- Rebuild for Fedora
* Mon Jan 16 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.1-2mdv2012.0
+ Revision: 761718
- spec cleanup
- unused pathes removed
  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - get rid of %%pre variable that's not really in use and that breaks %%pre script
* Mon Jan 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.1-1
+ Revision: 759222
- new version 0.9.1
* Thu Aug 11 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.0-0.pre2.1
+ Revision: 693952
- Update patch1
- imported package gnunet
* Thu Aug 11 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.9.0-0.pre2.1mdv2011.0
- Port to 2011
- New version
- Major spec rewrite
* Wed Apr 02 2008 Anssi Hannula <anssi@zarb.org> 0.7.3-1plf2008.1
- add to PLF
- ensure major correctness
- do not package COPYING, it is GPLv2+
- provide gnunet-devel
- fix library groups
- split library package due to different majors
- fix plugin loading on lib64 systems
- do not use daemonize
* Fri Mar 21 2008 Nicolas Vigier <boklm@mars-attacks.org> 0.7.3-1mdv2008.1
- first version
