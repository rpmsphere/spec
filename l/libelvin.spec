%global __os_install_post %{nil}
%define       with_xml      no
%define       with_ssl      no
%define       with_threads  yes

Name:         libelvin
Summary:      Elvin Client Library
URL:          https://www.elvin.org/
Group:        InstantMessaging
License:      Non-Commercial
Version:      4.0.3
Release:      26.1
Source0:      https://elvin.dstc.com/download/files/libelvin-%{version}.tar.gz
Patch0:        libelvin.patch
BuildRequires: libxml2-devel
BuildRequires: openssl-devel

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%description
This is the original C client library for the Elvin event routing
protocol. It supports HTTP/TCP/UDP/Unix as the transport protocol,
optionally SSL as the security layer and XDR/XML as the marshalling.
It also provides an Elvin command-line client.

%prep
%setup -q
%patch 0 -p0

%build
./configure \
    --host=i386-pc-linux-gnu \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --libdir=%{_libdir} \
    --sysconfdir=%{_sysconfdir}/libelvin \
%if "%{with_ssl}" == "yes"
    --with-ssl \
%else
    --without-ssl \
%endif
%if "%{with_xml}" == "yes"
    --with-xml \
%else
    --without-xml \
%endif
%if "%{with_threads}" == "yes"
    --enable-threads \
%else
    --disable-threads \
%endif
    --enable-udp \
    --enable-unix \
    --enable-http \
    --enable-cluster \
    --without-x \
    --without-xt \
    --without-gtk \
    --disable-nls

sed -i 's|-Werror=format-security||' Makefile */Makefile */*/Makefile
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/nls

%files
%{_bindir}/*
#%{_sysconfdir}/%{name}/*
%{_mandir}/man?/*
%{_infodir}/*
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.3
- Rebuilt for Fedora
