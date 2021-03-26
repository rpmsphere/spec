Name:          zimg
Summary:       Visualize Two-Dimensional Data
URL:           http://zimg.sourceforge.net/
Group:         Graphics
License:       GPL
Version:       5.0.0
Release:       9.1
Source0:       http://switch.dl.sourceforge.net/sourceforge/zimg/zimg-%{version}.tar.gz
BuildRequires: gd-devel

%description
Zimg generates PNG or JPEG images from arbitrary formatted 2-D
ASCII or binary data. Zimg is a command line tool and suitable for
rendering large amounts of 2-D data. Zimg is highly configurable via
command line switches and dynamically loadable objects.

%prep
%setup -q

%build
autoreconf -ifv
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir}
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_bindir}/*
%{_includedir}/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0.0
- Rebuild for Fedora
