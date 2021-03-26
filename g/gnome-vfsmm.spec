%global debug_package %{nil}

Name:           gnome-vfsmm26
Version:        2.26.0
Release:        8.1
Summary:        C++ wrapper for gnome-vfs
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gnome-vfsmm/2.18/gnome-vfsmm-%{version}.tar.bz2
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  glibmm24-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++ udisks2

%description
This package is part of the gnomemm project and provides a C++ interface for
gnome-vfs.

%package devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm24-devel
Requires:       gnome-vfs2-devel

%description devel
This package contains the static libraries and header files needed for
developing applications with %{name}.

%prep
%setup -q -n gnome-vfsmm-%{version}

%build
export CXXFLAGS="-std=gnu++11 -fPIC"
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%{_includedir}/gnome-vfsmm-2.6
%{_libdir}/*.so
%{_libdir}/gnome-vfsmm-2.6
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Nov 13 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.26.0
- Rebuild for Fedora
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sun Aug 16 2009 Denis Leroy <denis@poolshark.org> - 2.26.0-1
- Update to upstream 2.26.0
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Wed Sep 24 2008 Denis Leroy <denis@poolshark.org> - 2.24.0-1
- Update to upstream 2.24.0
* Wed Mar 12 2008 Denis Leroy <denis@poolshark.org> - 2.22.0-1
- Update to upstream 2.22.0
* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.20.0-2
- Autorebuild for GCC 4.3
* Mon Sep 17 2007 Denis Leroy <denis@poolshark.org> - 2.20.0-1
- Update to new stable tree 2.20.0
* Thu Mar 15 2007 Denis Leroy <denis@poolshark.org> - 2.18.0-1
- Update to Gnome 2.18, to follow gnome-vfs2 version
- Added dist tag
* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-2
- FE6 Rebuild
* Mon Aug 21 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-1
- Update to 2.16.0
* Thu Mar 23 2006 Denis Leroy <denis@poolshark.org> - 2.14.0-1
- Update to 2.14.0
* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> - 2.12.0-3
- Rebuild
* Fri Nov 25 2005 Denis Leroy <denis@poolshark.org> - 2.12.0-2
- Disabled static libraries
* Mon Sep 19 2005 Denis Leroy <denis@poolshark.org> - 2.12.0-1
- Update to 2.12.0
* Thu Apr 28 2005 Denis Leroy <denis@poolshark.org> - 2.10.0-1
- Upgrade to 2.10.0. x86_64 patch should no longer be necessary
* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt
* Thu Jan 27 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 0:2.6.1-2
- Add autoreconf patch; fixes build on x86_64
* Sun Jun 27 2004 Denis Leroy <denis@poolshark.org> - 0:2.6.1-0.fdr.1
- Upgrade to 2.6.1
* Tue Jul 22 2003 Gerald Henriksen <ghenriks@rogers.com>
- Initial release
