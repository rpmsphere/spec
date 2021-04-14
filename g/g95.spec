Summary:	Another Fortran 95 Compiler
Name:		g95
Version:	0.94
Release:	6.1
License:	GPLv2
Group:		Development/Other
URL:		http://www.g95.org
Source0:	http://ftp.g95.org/g95_source.tgz

%description
This package adds support for compiling Fortran 95 programs with g95,
a compiler alternative to the official GNU compiler called gfortran.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure --host=x86_64
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 g95 $RPM_BUILD_ROOT%{_bindir}/g95

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc G95Manual.pdf COPYING AUTHORS BUGS INSTALL README TODO
%{_bindir}/%{name}

%changelog
* Fri Dec 26 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.94
- Rebuilt for Fedora
* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.91-1.404_20070301.1mdv2008.1
+ Revision: 140731
- restore BuildRoot
+ Thierry Vignaud <tvignaud@mandriva.com>
- kill re-definition of %%buildroot on Pixel's request
* Sat Mar 03 2007 Giuseppe GhibĂ˛ <ghibo@mandriva.com> 0.91-1.404_20070301.1mdv2007.0
+ Revision: 131799
- Use gcc 4.0.4.
* Sat Mar 03 2007 Giuseppe GhibĂ˛ <ghibo@mandriva.com> 0.91-1.403_20070301.1mdv2007.1
+ Revision: 131750
- Added libgcc_s.so.1 to list of provides_exceptions (Pixel).
- Updated to release 0.91.
- Import g95
* Tue Mar 28 2006 Giuseppe Ghibň <ghibo@mandriva.com> 0.50-1.403_20060326.1mdk
- Release 20060327.
* Tue Mar 14 2006 Giuseppe Ghibň <ghibo@mandriva.com> 0.50-1.403_20060311.1mdk
- Release 20060311.
- Used internal's 4.0.3 as g95's gcc.
- Fixed description.
* Wed Jan 11 2006 Giuseppe Ghibň <ghibo@mandriva.com> 0.50-1.403_20060111.1mdk
- Release 20060111.
- Added --with systemcompiler to decide whether
- Used internal's 4.0_branch_20060111 as g95's gcc.
* Sat Nov 05 2005 Giuseppe Ghibň <ghibo@mandriva.com> 0.50-1.402_20051105.1mdk
- Added Patch0 to fix buildroot installation.
- Added Patch1 to allow coexisting with gfortran.
- Added Patch2 to fix gcc_libdir patch.
- initial release.
