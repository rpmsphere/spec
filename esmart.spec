Name:		esmart
Version:	0.9.0.050
Release:	1
Summary:	Esmart is Evas "smart objects"
Group:		User Interface/X
License:	BSD
URL:		http://www.enlightenment.org/pages/efl.html
Source:		%{name}-%{version}.tar.gz
BuildRequires:	libtool-ltdl-devel, evas-devel, ecore-devel
BuildRequires:	imlib2-devel, edje-devel, embryo-devel
BuildRequires:	libpng-devel, SDL-devel, libXcursor-devel
BuildRequires:	libXdamage-devel, libXcomposite-devel, libXinerama-devel
BuildRequires:	libXp-devel, libXScrnSaver-devel, fontconfig-devel
BuildRequires:	eet-devel, libjpeg-devel, openssl-devel, curl-devel
BuildRequires:	libeina-devel, libXtst-devel, gnutls-devel

%description
Esmart contains "smart" pre-built evas objects. It currently includes
a thumbnail generator and a horizontal/vertical container.

%package devel
Summary: 	Evas "smart objects" headers and development libraries.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Evas "smart objects" development headers and libraries.

%prep
%setup -q
sed -i 's/eina-0/eina/' configure*
##sed -i 's/2\.2\.6b/2.2.6/' aclocal.m4 configure
##sed -i '11i #define TRUE 1' src/lib/esmart_container/esmart_container_smart.c

%build
./autogen.sh --disable-static --prefix=/usr --libdir=%{_libdir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
find $RPM_BUILD_ROOT -name '*.la' -delete

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING INSTALL NEWS README ChangeLog
%{_datadir}/esmart*
%{_libdir}/*.so.*
%{_libdir}/esmart

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0.050
- Rebuild for Fedora
* Tue Oct 06 2009 Chelban Vasile <vchelban@fedoramd.org> 0.9.0.050-10
- BR exclude: epsilon
* Thu Jul 16 2009 Vasile Chelban <vchelban@fedoramd.org> 0.9.0.050-9
- bump release
* Sat Mar 14 2009 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.050-20090314
- SVN Update
* Sun Mar 1 2009 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.050-20090301
- Fixed BuildRequires based upon mock for F10
- CVS Update
* Thu Jul 17 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.042-20080717
- CVS Update
* Wed May 28 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.042-20080528
- CVS Update
* Sat Apr 5 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.042-20080405
- CVS Update
* Sun Mar 30 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.042-20080330
- CVS Update
* Mon Feb 25 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.042-2008.02.25
- CVS Update
* Wed Feb 20 2008 Chelban Vasile <vchelban@fedoramd.org> 0.9.0.042-2.2008.02.12.cvs.prof_k
- BuildRequires: eet-devel, libjpeg-devel, openssl-devel, curl-devel
* Mon Feb 11 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.042-2008.02.11
- CVS Update
* Mon Feb 11 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.042-2008.02.11
- CVS Update
* Mon Feb 4 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.042-2008.02.04
- CVS Update
* Sun Jan 20 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.011-2008.01.20
- CVS Update
* Tue Jan 8 2008 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.011-2008.01.08
- Fixed spec file (BuildRequires) based upon mock
- CVS Update
* Fri Dec 28 2007 Dr. Gregory R. Kriehn (Professor Kriehn) <gkriehn@csufresno.edu> - 0.9.0.011-2007.12.28
- CVS Update
