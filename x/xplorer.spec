%define		libname cxxx

Name:		xplorer
Version:	0.10.0
Release:	19.1
Source:		http://sourceforge.net/projects/cxplorer/files/xplorer/0.10.0/%{name}-%{version}.tar.xz
URL:		http://cxplorer.sourceforge.net
Group:		File tools 
License:	GPL
Vendor:		Gerhard Kräuter <gkraeuter@users.sourceforge.net>
Summary:	A filemanager for X-Windows with fast and accurate file type detection
Requires:	lib%{libname} zlib bzip2-libs
BuildRequires:	gcc-c++ autoconf automake glibc-devel zlib-devel bzip2-devel libstdc++-devel libX11-devel libXext-devel libXrender-devel expat-devel fontconfig-devel freetype-devel giflib-devel libjpeg-devel libpng-devel libtiff-devel

%package	-n %{libname}
Group:		Development/Application
Summary:	C++X, a shared library written from scratch.
Provides:	lib%{libname}

%package	-n %{libname}-devel
Group:		Development/Application
Summary:	C++X development package.
Requires:	lib%{libname}
BuildRequires:	gcc-c++ xorg-x11-proto-devel zlib-devel autoconf automake

%description
Xplorer is a filemanager for POSIX conformant operating systems using the X-Window-System (X11).
You can navigate in your local filesystem and launch applications.
Xplorer figures out filetypes and launches an application appropriate to process these files.
You can get information about files, move, copy or delete them.
Xplorer gets most of its functionality from C++X (libcxxx), a shared library written from scratch.
C++X and Xplorer are developed in parallel at present, but in the future there will be other
applications using C++X. Until then, C++X is only available as part of the Xplorer package.
One goal of C++X is to minimize dependencies on other programs/libraries, Xplorer should run on
every POSIX box with a working X-Window-System.

%description	-n %{libname}
C++X and Xplorer are developed in parallel at present, but in the future there will be other
applications using C++X. Until then, C++X is only available as part of the Xplorer package.
C++X has built-in support for internationalization. English, German and Spanish language is offered
at the moment. The tool intlize needed to create translations is located at http://intlize.sourceforge.net.

%description	-n %{libname}-devel
C++X development package.

%prep
%setup -q
sed -i 's|return mFile|return true|' cxxx/CImage.h
sed -i '73s|static inline const|static const|' intlize/i5e.h

%build
export CXXFLAGS=-std=gnu++98
touch NEWS ChangeLog
autoreconf -ifv
./configure --prefix=/usr --libdir=%{_libdir}
%__make %{?jobs:-j%jobs}

%install
%{__rm} -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%doc AUTHORS COPYING INSTALL README
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/%{libname}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.msg

%files -n %{libname}
%{_libdir}/*.so.*
%{_datadir}/%{libname}/icons/*
%{_datadir}/locale/*/LC_MESSAGES/%{libname}.msg

%files -n %{libname}-devel
%{_includedir}/*/*
%{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10.0
- Rebuilt for Fedora
* Mon Jan 07 2008 TI_Eugene <ti.eugene@gmail.com> 0.8.1
- Initial build for openSUSE Build Service
