Name:           libexplain
Version:        1.4
Release:        1
Summary:        Library functions to explain system call errors
License:        LGPL-3.0+
Group:          Development/Libraries/C and C++
URL:            https://libexplain.sourceforge.net
Source:         https://downloads.sf.net/libexplain/%{name}-%{version}.tar.gz
Patch0:         libexplain-1.4-largefile.patch
Patch1:         libexplain-1.4-syscall.patch
# PATCH-FIX-UPSTREAM libexplain-1.4-missing-defines.patch mpluskal@suse.com
Patch2:         libexplain-1.4-missing-defines.patch
BuildRequires:  bison
BuildRequires:  ghostscript
BuildRequires:  groff
BuildRequires:  kernel-devel
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  lsof
BuildRequires:  pkg-config

%description
The libexplain project provides a library which may be used to explain
Unix and Linux system call errors. This will make your application's
error messages much more informative to your users.  The library is
not quite a drop-in replacement for strerror, but it comes close. Each
system call has a dedicated libexplain function.

The coverage for system calls is being improved all the time. Coverage
includes 159 system calls and 444 ioctl requests.

%package devel
Summary:        Development files for libexplain
License:        LGPL-3.0+ and GPL-3.0+
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files for the libexplain library.

%prep
%setup -q
%patch0
%patch1
%patch2

%build
%configure
#sed -i 's|bison -y|byacc|' Makefile etc/howto.cook
make

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
# --disable-static for configure has no effect
rm %{buildroot}%{_libdir}/%{name}.{a,la}
%find_lang %{name}

%files -f %{name}.lang
%doc LICENSE README
%{_libdir}/%{name}.so.*
%{_bindir}/explain
%{_mandir}/man1/explain.1%{ext_man}
%{_mandir}/man1/explain_lca2010.1%{ext_man}
%{_mandir}/man1/explain_license.1%{ext_man}

%files devel
%{_datadir}/doc/%{name}
%{_mandir}/man3/*.3%{ext_man}
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Mon Apr 11 2016 mpluskal@suse.com
- Fix building with kernel-4.5 and later
  * libexplain-1.4-missing-defines.patch
- Fix rpm group
* Mon Apr 13 2015 mpluskal@suse.com
- Initial package for version 1.4
- Use patches from fedora
  * libexplain-1.4-largefile.patch
  * libexplain-1.4-syscall.patch
