%define common_summary A complete user-space boot splash system
%define common_description A boot splash program that doesn't require patching the Linux kernel. It paints\
graphic images directly to framebuffers using libdirectfb.
%define lib_major 1
%define lib_name %{name}-libs
%define develname %{name}-devel

Summary:	%{common_summary}
Name:		splashy
Version:	0.3.10
Release:	1
License:	GPL
Group:		System/Kernel and hardware
URL:		http://alioth.debian.org/download.php/1358/splashy_%{version}.tar.gz
Source:		%{name}-%{version}.tar.gz
# Werror breaks build when used with fortify (we could also empty the _fortify_cflags macro)
Patch0:		splashy-0.3.10-warnings.patch
Patch1:		splashy-0.3.10-checkvideo.patch
Patch2:		splashy-0.3.3-dfblink.patch
BuildRequires:	directfb-devel
BuildRequires:	glib2-devel
#BuildRequires:	libmagic-devel
#BuildRequires:	procps-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	freetype-devel
BuildRequires:	glibc-devel

%description
%{common_description}

%package -n	%{lib_name}
Summary:	A library to %{common_summary}
Group:		System/Libraries

%description -n	%{lib_name}
%{common_description}

This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Development tools for programs using %{name}
Group:		Development/C
Requires:	%{lib_name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%name-libs <= 0.3.4

%description -n	%{develname}
%{common_description}

This package contains the header files and libraries needed for
developing programs using the %{name} library.

%prep
%setup -q
%patch0 -p1 -b .warnings
%patch1 -p1 -b .checkvideo
#%patch2 -p1 -b .dfblink
sed -i 's/1\.10/1.11/' autogen.sh

%build
NOCONFIGURE=1 ./autogen.sh
rm -f src/libglib-2.0.la
##%configure --prefix=/
%__make -j1

%install
rm -rf %{buildroot}

export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"

%makeinstall

install -d %{buildroot}%{_initrddir}
mv %{buildroot}%{_sysconfdir}/init.d/* %{buildroot}%{_initrddir}/
mv %{buildroot}%{_sbindir} %{buildroot}/sbin

rm -f %{buildroot}%{_sysconfdir}/%{name}/themes

# remove Debian-specific files
rm -f %{buildroot}%{_sysconfdir}/lsb-base-logging.sh
rm -rf %{buildroot}%{_datadir}/initramfs-tools

%find_lang %name

%clean
rm -rf %{buildroot}

%post -n %{lib_name}
/sbin/ldconfig
ln -s %{_datadir}/%{name}/themes %{_sysconfdir}/%{name}/themes

%postun -n %{lib_name}
/sbin/ldconfig
rm -f %{_sysconfdir}/%{name}/themes

%files -f %name.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%attr(0755,root,root) %{_initrddir}/*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/default/*
%dir %{_sysconfdir}/splashy
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/splashy/*.xml
#%{_sysconfdir}/%name/themes
/sbin/*
%{_sysconfdir}/console-tools/config.d/splashy
%dir %{_datadir}/splashy
%{_datadir}/splashy/*
%{_mandir}/man?/*

%files -n %{lib_name}
%{_libdir}/lib%{name}*.so.%{lib_major}*

%files -n %{develname}
%{_includedir}/%{name}*.h
%{_libdir}/lib%{name}*.la
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%name.pc


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Jul 9 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.3.10-1.ossii
- Rebuild for M6(CentOS5)

* Thu May 29 2008 Funda Wang <fundawang@mandriva.org> 0.3.10-1mdv2009.0
+ Revision: 213009
- rediff checkvideo patch
- New version 0.3.10

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 09 2007 Olivier Blin <oblin@mandriva.com> 0.3.5-2mdv2008.0
+ Revision: 60801
- remove bundled libglib-2.0.la
- 0.3.5

* Thu Jul 26 2007 Olivier Blin <oblin@mandriva.com> 0.3.4-3mdv2008.0
+ Revision: 55899
- new devel library policy
- fix warnings instead of removing Werror option

* Wed Jul 25 2007 Olivier Blin <oblin@mandriva.com> 0.3.4-2mdv2008.0
+ Revision: 55507
- buildrequires glibc and png static devel packages to get a full static build

* Sat Jul 21 2007 Olivier Blin <oblin@mandriva.com> 0.3.4-1mdv2008.0
+ Revision: 54319
- fix group
- 0.3.4
- specify fbdev as default directfb system and force linking with directfb system/wm/input libraries (making splashy work again!)
- fix segfault when video init fails

* Wed Jun 13 2007 Olivier Blin <oblin@mandriva.com> 0.3.3-1mdv2008.0
+ Revision: 38543
- drop post script (mxterm theme is not in the package anymore, and it should not be hardcoded anyway)
- 0.3.3
- build with static files from new directfb-devel
- add lib packages
- package console-tools hook and remove debian-specific files
- enable static linking
- do no build with Werror (breaks build with fortify)
- use the configure macro
- buildrequire freetype2-static-devel


* Sun Feb 25 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.8-2mdv2007.0
+ Revision: 125545
- fix build
- fix deps
- fix build and deps
- lib64 fixes
- Import splashy

* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1.8-1mdk
- initial Mandriva package (mille-xterm import)
