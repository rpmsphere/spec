%global debug_package %{nil}

Name:         dwarf
Summary:      Object File Manipulation Tool
URL:          http://code.google.com/p/dwarf-ng/
Group:        Compiler
License:      GPL
Version:      0.3.1
Release:      2.1
Source0:      http://dwarf-ng.googlecode.com/files/dwarf-%{version}.tar.gz
BuildRequires: readline-devel

%description
dwarf is a powerful object file manipulation tools in the spirit
of gdb. With dwarf you can read and edit all the file's
section headers as well as the raw data. With dwarf you can create
and customize new file's header and it can be used as a compiler
back-end to create executables/object files. dwarf also permits to
inject easily new headers and pieces of code/data into the file.
dwarf currently handles ELF, PE (Portable executables) and Mach-O
files format.

%prep
%setup -q
sed -i '/typedef long long            int64_t;/d' src/libdwarf/stdint.h
touch src/libdwarf/dwarfrc

%build
export CFLAGS="-fPIC -std=gnu89 -Wl,--allow-multiple-definition"
export LIBS="`pkg-config readline --libs`"
%configure
make

%install
make install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_bindir}/dwarf
%{_libdir}/libdwarf.a
%{_datadir}/doc/dwarf-ng
%{_mandir}/man1/dwarf.1.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuild for Fedora
