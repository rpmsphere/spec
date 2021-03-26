%global debug_package %{nil}

Name:           libgnomemm26
Version:        2.30.0
Release:        9.4
Summary:        C++ interface for Gnome libs (a GUI library for X)
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libgnomemm/2.30/libgnomemm-%{version}.tar.gz
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  libpng-devel
BuildRequires:  gtkmm24-devel
BuildRequires:  libgnome-devel
BuildRequires:  sane-backends-devel
BuildRequires:  gcc-c++ udisks2

%description
This package provides a C++ interface for GnomeUI. It is a subpackage
of the Gtk-- project. The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.

%package devel
Summary:        Headers for developing programs that will use Gnome--.
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       gtkmm24-devel
Requires:       libgnome-devel

%description devel
This package contains the headers that programmers will need to develop
applications which will use Gnome--, part of Gtk-- the C++ interface to
the GTK+ (the Gimp ToolKit) GUI library.

%prep
%setup -q -n libgnomemm-%{version}

%build
export CXXFLAGS="-std=gnu++11"
%configure --disable-static --enable-docs
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_libdir}/*.so.*

%files devel
%doc %{_datadir}/doc/*
%{_includedir}/libgnomemm-2.6
%{_libdir}/*.so
%{_libdir}/libgnomemm-2.6
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Nov 13 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.30.0
- Rebuild for Fedora
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Fri Sep 25 2009 Denis Leroy <denis@poolshark.org> - 2.28.0-1
- Update to upstream 2.28.0
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Apr  7 2009 Denis Leroy <denis@poolshark.org> - 2.26.0-1
- Update to upstream 2.26.0
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Wed Sep 24 2008 Denis Leroy <denis@poolshark.org> - 2.24.0-1
- Update to upstream 2.24.0
* Wed Mar 12 2008 Denis Leroy <denis@dedibox.albator.org> - 2.22.0-1
- Update to upstream 2.22.0
* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.20.0-2
- Autorebuild for GCC 4.3
* Thu Sep 20 2007 Denis Leroy <denis@poolshark.org> - 2.20.0-1
- Update to new stable branch 2.20
* Thu Mar 15 2007 Denis Leroy <denis@poolshark.org> - 2.18.0-1
- Update to Gnome 2.18, to follow libgnome2 version
* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-3
- FE6 Rebuild
* Mon Aug 21 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-2
- Uploaded source file
* Mon Aug 21 2006 Denis Leroy <denis@poolshark.org> - 2.16.0-1
- Update to 2.16.0
* Thu Mar 23 2006 Denis Leroy <denis@poolshark.org> - 2.14.0-1
- Update to 2.14.0
* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> - 2.12.2-1
- Update to 2.12.2
* Fri Nov 25 2005 Denis Leroy <denis@poolshark.org> - 2.12.1-1
- Update to 2.12.1
- Disabled static libraries
* Mon Sep 19 2005 Denis Leroy <denis@poolshark.org> - 2.12.0-1
- Update to 2.12.0
* Thu Apr 28 2005 Denis Leroy <denis@poolshark.org> - 2.10.0-1
- Upgrade to 2.10.0; x86_64 patch should no longer be necessary
* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt
* Thu Jan 27 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> - 2.6.0-2
- Add autoreconf patch; fixes build on x86_64
* Mon Jun 27 2004 Denis Leroy <denis@poolshark.org> - 0:2.6.0-0.fdr.1
- Upgrade to 2.6.0
* Wed Oct 22 2003 Michael A. Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.5
- Fix requirements on -devel
- Fix -devel description
* Tue Oct 16 2003 Michael A. Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.4
- Remove Prefix, the package isn't relocatable due to paths in gtkmmproc et.al.
* Mon Oct 15 2003 Michael A. Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.3
- Ignore Doxygen documentation, it doesn't build correctly.
- Fix up prefix
* Sun Oct 14 2003 Michael A. Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.2
- Fix BuildRequires and requires.  --enable-docs
* Sat Oct 13 2003 Michael A. Koziarski <michael@koziarski.org> - 2.0.1-0.fdr.1
- Import of Dag's package to fedora
* Sat Mar 29 2003 Dag Wieers <dag@wieers.com> - 1.3.10-0
- Initial package. (using dar)
