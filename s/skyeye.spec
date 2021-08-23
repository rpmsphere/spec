%undefine _missing_build_ids_terminate_build

Name:		skyeye
Version:	1.3.5
Release:	0.rc1.1
License:	GPLv2
Group:		Emulators
Summary:	ARM, Mips, Coldfire simulator
URL:		http://sourceforge.net/apps/phpwebsite/skyeye
Source0:	%{name}-%{version}_rc1.tar.bz2
Patch0:		skyeye-1.3.0.fix-str-fmt.patch
BuildRequires:  libpng-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	libXpm-devel
BuildRequires:	binutils-devel
BuildRequires:	readline-devel
BuildRequires:	libtool-ltdl-devel
BuildRequires:	gcc-c++, python2-devel
BuildRequires:	SDL-devel
Requires:	libskyeye

%description
The goal of SkyEye is to provide an integrated simulation environment in Linux
and Windows. SkyEye environment simulates/emulates typical Embedded Computer
Systems (Now it supports a series ARM architecture based microprocessors and
Blackfin DSP Processor). You can run some Embedded Operation System such as
ARM Linux, uClinux, uc/OS-II (ucos-ii) etc. in SkyEye, and analysis or debug
them at source level.

%package -n lib%{name}
Summary:	%{name} library
Group:		System/Libraries
	
%description -n lib%{name}
%{name} library.

%package -n lib%{name}-devel
Summary:	%{name} development library
Group:		Development/Other
Requires:	lib%{name} = %{version}
	
%description -n lib%{name}-devel
%{name} development library.  

%prep
%setup -q -n %{name}-%{version}_rc1
%patch0 -p0
sed -i 's/2\.8/2.*/' configure.in
sed -i 's|usr/local|usr|' arch/ppc/Makefile.am
sed -i 's|-MF .deps/armemu32.Tpo||' arch/arm/Makefile.am
sed -i 's|\$(prefix)/bin|$(DESTDIR)%{_bindir}|g' Makefile.am
sed -i 's|\$(prefix)/|$(DESTDIR)%{_libdir}/%{name}/|g' Makefile.am
sed -i 's| -liconv||' android/objs/*/Makefile.*
%ifarch x86_64
sed -i '176,180d' third-party/distrib/sdl-1.2.12/src/video/x11/SDL_x11sym.h
%endif
sed -i -e 's|dumpversion|dumpfullversion|' -e 's|3\.\*)|11.*)|' configure*
sed -i 's|subsubsection|subsection|' third-party/bfd/doc/elf.texi
sed -i 's|#ifdef SEMOPS_DEFINE_INLINE|#ifndef SEMOPS_DEFINE_INLINE|' third-party/opcodes/cgen-ops.h
sed -i 's|llvm/BasicBlock.h|llvm/IR/BasicBlock.h|' common/dyncom/translate_singlestep.cpp
sed -i -e 's|llvm/DerivedTypes.h|llvm/IR/DerivedTypes.h|' -e 's|llvm/LLVMContext.h|llvm/IR/LLVMContext.h|' common/include/dyncom/dyncom_llvm.h

%build
#autoreconf -fiv
%configure --enable-lcd --enable-shared
make lib CFLAGS+="-Wno-format-security -Wno-return-type -Wno-error -Wl,--allow-multiple-definition"
make CFLAGS+="-Wno-format-security -Wno-return-type -Wno-error -Wl,--allow-multiple-definition"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc MAINTAINERS README ChangeLog COPYING LICENSE REPORTING-BUGS TODO
%attr(755,root,root) %{_bindir}/*

%files -n lib%{name}
%{_libdir}/%{name}/*.so.*
%{_libdir}/%{name}/testsuite

%files -n lib%{name}-devel
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/*.so
%{_includedir}/*

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.5.rc1
- Rebuild for Fedora
* Sat Feb 27 2010 Emmanuel Andry <eandry@mandriva.org> 1.3.0-0.rc1.1mdv2010.1
+ Revision: 512492
- BR readline-devel
- add devel subpackage
- BR binutils-devel
- split libs into a subpackage
- BR libxpm-devel
- New version 1.3.0 rc1
- drop p0 (fixed upstream)
- diff patch to fix string format
* Thu May 14 2009 Michael Scherer <misc@mandriva.org> 1.2.8-0.rc1.1mdv2010.0
+ Revision: 375592
- add BuildRequires
- fix rpmlint warning
- fix installation
- add patch to fix problem on file open, detected by fortify option
- import skyeye
