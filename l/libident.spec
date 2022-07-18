%global __os_install_post %{nil}

Name:           libident
Version:        0.32
Release:        12
Summary:        New LibIdent C library
Group:          System Environment/Libraries
License:        Public Domain
URL:            http://www.remlab.net/libident/
Source0:        http://www.remlab.net/files/libident/libident-%{version}.tar.bz2
Source1:        xinetd.identtest
BuildRequires:  /usr/bin/iconv

%description
LibIdent is a small C library for interfacing with RFC 1413 
Identification protocol servers, which are used for identifying users. 
LibIdent supports both IPv4 and IPv6 addresses transparently.

It is meant to be used by daemons to try to authenticate users using the 
Ident protocol. For this to work, users need to have an Ident server 
running on the system from which they are connected.

%package        tools
Summary:        A small daemon that can be used to test Ident servers
Group:          System Environment/Daemons
Requires:       %{name} = %{version}-%{release}

%description    tools
in.identtestd is a small daemon (to be started from inetd) that does an 
ident lookup on you if you telnet into it. Can be used to verify that 
your Ident server is working correctly.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
LibIdent is a small C library for interfacing with RFC 1413 
Identification protocol servers, which are used for identifying users. 
LibIdent supports both IPv4 and IPv6 addresses transparently.

It is meant to be used by daemons to try to authenticate users using the 
Ident protocol. For this to work, users need to have an Ident server 
running on the system from which they are connected.

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
for f in ident.3 README ChangeLog AUTHORS NEWS COPYING; do
	iconv -f ISO-8859-1 -t UTF-8 $f -o $f.new && mv $f.new $f
done

%build
CFLAGS="-fPIC %{optflags} -D_GNU_SOURCE" %configure \
    --disable-static \
    --enable-testers
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
install -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xinetd.d/identtestd

%clean
rm -rf %{buildroot}

%post tools
/sbin/service xinetd reload > /dev/null 2>&1 || :

%postun tools
if [ $1 = 0 ]; then
    /sbin/service xinetd reload > /dev/null 2>&1 || :
fi

%files
%doc COPYING README AUTHORS ChangeLog NEWS
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/ident.3*

%files tools
%config(noreplace) %{_sysconfdir}/xinetd.d/identtestd
%{_sbindir}/in.identtestd
%{_mandir}/man8/in.identtestd.8*

%changelog
* Sun May 09 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.32
- Rebuilt for Fedora
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Tue Feb 12 2008 Andreas Thienemann <athienem@redhat.com> - 0.32-2
- Rebuild against gcc34 with -D_GNU_SOURCE
* Sat Nov 24 2007 Andreas Thienemann <andreas@bawue.net> - 0.32-1
- Updated to 0.32, making manual .so compile unecessary
* Thu Apr 26 2007 Andreas Thienemann <andreas@bawue.net> - 0.30-4
- Included dependency for -tools subpackage
* Tue Apr 03 2007 Andreas Thienemann <andreas@bawue.net> - 0.30-3
- Build the tools against said shared library as well
* Mon Apr 02 2007 Andreas Thienemann <andreas@bawue.net> - 0.30-2
- Added shared object instead of static lib
* Sat Mar 31 2007 Andreas Thienemann <andreas@bawue.net> - 0.30-1
- Initial FE package
