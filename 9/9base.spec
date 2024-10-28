%undefine _debugsource_packages

Summary: Plan 9 userland tools to Unix
Name: 9base
Version: 6
License: MIT
Release: 11.1
Group: System/Base
URL: https://tools.suckless.org/9base
Source: https://dl.suckless.org/tools/%{name}-%{version}.tar.gz
BuildRequires: glibc-static

%description
9base is a port of various original Plan 9 tools for Unix, based on plan9port.

%prep
%setup -q -n 9base-%version

%build
export LDFLAGS=-Wl,--allow-multiple-definition
make 

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} PREFIX=%{_prefix}/ MANPREFIX=%{_mandir} install

cd %{buildroot}%{_bindir}
for file in * ; do
mv $file 9$file
done
cd %{buildroot}%{_mandir}/man1
for man in * ; do
mv $man 9$man
done

%files
%{_bindir}/*
/usr/etc/rcmain
/usr/lib/troff
%{_mandir}/man1/*

%changelog
* Sat Nov 24 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 6
- Rebuilt for Fedora
* Thu May 31 2007 Antoine Ginies <aginies@mandriva.com> 20051114-4mdv2008.0
+ Revision: 33084
- adjust buildrequires
- add glibc-devel buildrequires
- fix bug #23957 (description and path)
* Sat Dec 10 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 20051114-3mdk
- fix build on x86_64
- fix debug files in main package
* Mon Dec 05 2005 Antoine Ginies <aginies@mandriva.com> 20051114-2mdk
- fix pb of man conflict
* Sat Dec 03 2005 Antoine Ginies <aginies@mandriva.com> 20051114-1mdk
- first release, need to create a subdir /usr/bin/9 to avoid conflict
