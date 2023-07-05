Name:          libgdkxft
Version:       1.5
Release:       8.1
Summary:       Transparently adds anti-aliased font support to gtk+-1.2
Group:         System/Libraries
URL:           https://gdkxft.sourceforge.net/
Source:        https://heanet.dl.sourceforge.net/sourceforge/gdkxft/gdkxft-%{version}.tar.gz
License:       LGPL
BuildRequires: gtk+-devel >= 1.2.10
BuildRequires: glib-devel >= 1.2.10
BuildRequires: libX11-devel >= 1.1.1
BuildRequires: libXft-devel >= 2.1.12
BuildRequires: libXext-devel >= 1.0.2
Patch0:        gdkxft-1.5-lib64.patch

%description
Gdkxft transparently adds anti-aliased font support to gtk+-1.2.
Once you have installed it, you can run any (well, nearly any)
existing gtk+ binary and see anti-aliased fonts in the gtk widgets.
You don't need to recompile gtk+ or your applications.

%package devel
Summary:       Devel package for libgdkxft
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Gdkxft transparently adds anti-aliased font support to gtk+-1.2.
Once you have installed it, you can run any (well, nearly any)
existing gtk+ binary and see anti-aliased fonts in the gtk widgets.
You don't need to recompile gtk+ or your applications.

This is the devel package.

%prep
%setup -q -n gdkxft-%{version}
%patch0 -p1

%build
%configure
C_INCLUDE_PATH=/usr/include/freetype2 make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/gdkxft.conf
%{_libdir}/*.so.*
%{_sbindir}/*
%{_mandir}/man8/*

%files devel
%{_libdir}/*.so
%{_libdir}/*.la

%changelog
* Tue Jun 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuilt for Fedora
* Mon May 28 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5-2mamba
- rebuilt
* Mon Oct 27 2003 Silvan Calarco <silvan.calarco@qilinux.it> 1.5-1qilnx
- first build
