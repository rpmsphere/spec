Name: libixp
Version: 0.6
Release: 5.1
Summary: Plan9 file protocol library
License: MIT
Group: System/Libraries
URL: https://www.suckless.org/wiki/libs/libixp
Source: https://hg.suckless.org/libixp/archive/339db5c6d2c9.tar.gz

%description
libixp is a stand-alone client/server 9P library.
libixp's server api is heavily based on that of Plan 9's lib9p.

%prep
%setup -qn %{name}-339db5c6d2c9
sed -i 's|-lixp|-lixp -Wl,--allow-multiple-definition|' cmd/Makefile

%build
sed -i \
    -e "/^PREFIX/s|=.*|= /usr|" \
%ifarch x86_64 aarch64
	-e "s|/usr/lib|/usr/lib64|g" \
	-e "/ LIBDIR/s|=.*|= /usr/lib64|" \
%endif
	config.mk
make

%install
#make_install
%makeinstall DESTDIR=%{buildroot}

%package devel
Summary: Plan9 file protocol library
Group: Development/C
Provides: %{name}-devel = %{version}-%{release}

%description devel
libixp is a stand-alone client/server 9P library.
libixp's server api is based heavily on that of Plan 9's lib9p.

%files devel
%{_libdir}/*.a
%{_includedir}/ixp.h
%{_includedir}/ixp_srvutil.h
%{_mandir}/man3/*.3*

%package -n ixpc
Summary: Plan9 file protocol client
Group: Networking/File transfer

%description -n ixpc
ixpc is a client to access a 9P file server from the command line
or from shell scripts.

%files -n ixpc
%{_bindir}/ixpc
%{_mandir}/man1/ixpc.1*

%changelog
* Sat Nov 24 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
* Wed Oct 19 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 0.6-0.20110223.2mdv2012.0
+ Revision: 705337
- removed bogus Requires left after spec cleanup
* Tue Oct 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.6-0.20110223.1
+ Revision: 705289
- new version snapshot 0.6 339db5c6d2c9A
  cleaned up spec and libdir for 64bit
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5-3mdv2011.0
+ Revision: 620144
- the mass rebuild of 2010.0 packages
* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0.5-2mdv2010.0
+ Revision: 438634
- rebuild
* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 0.5-1mdv2009.1
+ Revision: 324859
- New upstream release
* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.4-4mdv2009.0
+ Revision: 248838
- rebuild
- fix no-buildroot-tag
- fix frenglish
* Wed Dec 12 2007 Jérôme Soyer <saispo@mandriva.org> 0.4-2mdv2008.1
+ Revision: 119049
- Fix Requires
* Wed Dec 12 2007 Jérôme Soyer <saispo@mandriva.org> 0.4-1mdv2008.1
+ Revision: 117844
- import libixp
