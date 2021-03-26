Name:		fuseiso
Summary:	FUSE support for ISO filesystem images
Version:	20070708
Release:	16
License:	GPLv2+
Group:		System Environment/Base
Source0:	http://ubiz.ru/dm/%{name}-%{version}.tar.bz2
# Upstream: https://sourceforge.net/tracker/index.php?func=detail&aid=1933445&group_id=215002&atid=1031924
Patch0:		fuseiso-largeiso.patch
URL:		http://sourceforge.net/projects/fuseiso/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	fuse-devel, glib2-devel, zlib-devel
Requires:	fuse

%description
Mount ISO filesystem images as a non-root user. Currently supports
plain ISO9660 Level 1 and 2, Rock Ridge, Joliet, zisofs. Supported image
types: ISO, BIN (single track only), NRG, MDF, IMG (CCD).

%prep
%setup -q
%patch0 -p0

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/fuseiso

%changelog
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070708-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070708-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070708-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070708-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070708-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070708-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070708-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan  4 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 20070708-9
- rebuilt with fixed url (resolves bz 542998)

* Thu Sep 17 2009 Peter Lemenkov <lemenkov@gmail.com> - 20070708-8
- Rebuilt with new fuse

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070708-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 20070708-6
- add explicit requires on fuse (bz 497681)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20070708-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 20070708-4
- handle larger than 4GB isos (thanks to Thomas Bittermann, resolves 
  bz440436)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20070708-3
- Autorebuild for GCC 4.3

* Wed Nov 14 2007 Tom "spot" Callaway <tcallawa@redhat.com> 20070708-2
- add zlib-devel as BR
- use macros in Source0 url
- add last - in defattr

* Thu Nov 8 2007 Tom "spot" Callaway <tcallawa@redhat.com> 20070708-1
- Initial package for Fedora
