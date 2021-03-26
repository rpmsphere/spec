Name:         mp3c
Summary:      MP3 Ripping User Interface
URL:          http://mp3c.wspse.de/
Group:        Audio
License:      GPL
Version:      0.31
Release:      7.1
Source0:      ftp://ftp.wspse.de/pub/linux/wspse/mp3c-%{version}.tar.bz2

%description
MP3c is a Curses user interface for ripping audio files from CDROMs
and encoding them as MP3s.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.31
- Rebuild for Fedora
