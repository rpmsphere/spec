BuildRequires:  glibc-devel iniparser-devel libxml2-devel pcre-devel libxslt docbook-style-xsl readline-devel
Summary:        TV Personal Video Recorder Daemon
Name:           tvpvrd
Version:        4.5.0
Release:        12.1
License:        GPL-3.0
Group:          Productivity/Multimedia/Other
URL:            http://sourceforge.net/projects/tvpvrd
Source0: https://downloads.sourceforge.net/project/tvpvrd/%{name}-%{version}.tar.xz

%description
TV Personal Video recorder daemon. Schedule and manage video recordings from
one or more TV capture cards, e.g. Hauppauge 150, 250, or 350. The server also
provides automatic transcoding of recordings via ffmpeg, for example, MP4 format.

Authors:
Johan Persson <johan162@gmail.com>

%prep
%setup -q
sed -i 's|rc == rc|rc|' src/shell/tvpshell.c

%build
autoreconf -ifv
sed -i 's|-Werror ||' configure* */Makefile* */*/Makefile*
%configure
make %{?_smp_mflags} CFLAGS+="-Wno-format-truncation"

%install
%makeinstall
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_initrddir}
mv %{buildroot}/etc/init.d/tvpvrd %{buildroot}%{_initrddir}
ln -sf %{_initrddir}/tvpvrd %{buildroot}%{_sbindir}/rctvpvrd
rm -rf %{buildroot}%{_datadir}/doc/packages

%clean
%__rm -rf %{buildroot}

%post  
/usr/sbin/groupadd -r tvpvrd 2> /dev/null || : 
/usr/sbin/useradd -r -g tvpvrd -s /bin/false -c "tvpvrd daemon" tvpvrd 2> /dev/null || : 
/usr/sbin/usermod -g tvpvrd tvpvrd 2>/dev/null || : 
test -e /var/run/tvpvrd.pid  || rm -rf /var/run/tvpvrd.pid && :

%files
%{_bindir}/tvpvrd
%{_bindir}/tvpsh
%{_initrddir}/tvpvrd
%{_sbindir}/rctvpvrd
%config %{_sysconfdir}/tvpvrd
%{_mandir}/man1/*
%doc COPYING AUTHORS README NEWS
%{_sysconfdir}/pm/config.d/ivtv.config
%{_sysconfdir}/pm/sleep.d/10tvpvrd

%changelog
* Tue Feb 11 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 4.5.0
- Rebuild for Fedora
* Wed May 4 2011 Johan Persson <johan162@gmail.com> - 3.1.1-16.1
- Cleanup of RPM spec file 
