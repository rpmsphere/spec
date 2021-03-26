%global debug_package %{nil}

Name:         ctalk
Summary:      Object-Orientation Extensions for ISO-C
URL:          https://sourceforge.net/projects/ctalk/
Group:        Language
License:      GPL
Version:      0.0.65
Release:      1
Source0:      ctalk-0.0.65-2019-09-24.tar.xz
Source1:      ctpp-1.0.89.tar.xz
#BuildRequires: ctalk

%description
Ctalk adds object oriented programming features, including an object
class hierarchy, methods, and operator overloading, to ANSI and ISO
C source code. It also contains the C99 compliant C preprocessor
ctpp(1) which can be used stand-alone, too.

%prep
%setup -q -c -a 1

%build
export LDFLAGS=-Wl,--allow-multiple-definition
cd ctalk-*
CPPFLAGS="-DWITHOUT_X11" \
./configure \
      --prefix=%{_prefix} \
      --mandir=%{_mandir} \
      --libdir=%{_libdir} \
      --infodir=%{_datadir}/info \
      --without-x \
      --disable-shared
%{__make} %{_smp_mflags}

cd ../ctpp-*
./configure \
      --prefix=%{_prefix} \
      --mandir=%{_mandir} \
      --libdir=%{_libdir} \
      --infodir=%{_datadir}/info \
      --disable-shared
%{__make} %{_smp_mflags}

%install
export PATH=$PATH:%{buildroot}%{_bindir}
cd ctalk-*
%make_install
#{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
cd ../ctpp-*
%make_install
#{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%{_bindir}/*
%{_includedir}/%{name}
%{_mandir}/man*/*
%{_datadir}/info/*
%{_datadir}/%{name}
%{_libdir}/lib*

%changelog
* Wed Oct 02 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.65
- Rebuild for Fedora
