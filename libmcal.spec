Name:          libmcal
Version:       0.7
Release:       19.1
Summary:       A C library for accessing calendars
Group:         System/Libraries
URL:           http://libmcal.sourceforge.net/
Source:        http://easynews.dl.sourceforge.net/sourceforge/libmcal/libmcal-%{version}.tar.gz
Patch0:        libmcal-%{version}-flexfix.patch
License:       GPL

%description
mcal stands for Modular Calendar Access Library. libmcal is a C library
for accessing calendars, written to be very modular, with pluggable drivers.
One of the main drivers it handles is ICAP, an internet protocol that has
very close ties with the IMAP protocol. Using ICAP, you can access a calendar
in very much the same way as you use IMAP to access a remote mailbox.

%package devel
Summary:       A C library for accessing calendars
Group:         Development/Libraries

%description devel
mcal stands for Modular Calendar Access Library. libmcal is a C library
for accessing calendars, written to be very modular, with pluggable drivers.
One of the main drivers it handles is ICAP, an internet protocol that has
very close ties with the IMAP protocol. Using ICAP, you can access a calendar
in very much the same way as you use IMAP to access a remote mailbox.

This package contains the mcal headers and static library.

%prep
%setup -q -n libmcal
%patch0 -p1
sed -i '/extern int/d' icalroutines.h
sed -i '1i extern int ical_yyleng;' icalroutines.c

%build
%configure
sed -i 's/-Wall/-Wall -fPIC/' Makefile
make

%install
sed -i "s|/usr/local/mcal|$RPM_BUILD_ROOT/usr/lib/mcal|" Makefile
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_includedir}
mv $RPM_BUILD_ROOT/usr/lib/mcal/include $RPM_BUILD_ROOT%{_includedir}/mcal
cp cal_misc.h icalroutines.h $RPM_BUILD_ROOT%{_includedir}/mcal
%ifarch x86_64 aarch64
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%{_includedir}/mcal
%{_libdir}/mcal

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7
- Rebuild for Fedora
* Tue Jul 03 2007 Tiziana Ferro <tiziana.ferro@email.it> 0.7-1mamba
- update to 0.7
* Wed Sep 10 2003 Silvan Calarco <silvan.calarco@qilinux.it> 0.6-1qilnx
- first build
