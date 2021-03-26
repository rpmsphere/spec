Summary:	Lightweight and simple frontend for su command
Name:		ktsuss
Version:	2
Release:	3.1
License:	BSD
Group:		System/Base
URL:		http://code.google.com/p/%{name}
Source0:	http://ktsuss.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		ktsuss-2.printf.patch
BuildRequires:	pkgconfig(gtk+-2.0)

%description
ktsuss stands for "keep the su simple, stupid", and as the
name says, is a graphical version of su written in C and
GTK+ 2.The idea of the project is to remain simple and bug
free.

%prep
%setup -q
%patch0 -p1 -b .printf

%build
%configure
make

%install
%makeinstall

%files
%defattr(-,root,root)
%doc README Changelog
%attr(4755,root,root)%{_bindir}/ktsuss
%{_datadir}/pixmaps/ktsuss.png

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2
- Rebuild for Fedora
* Sun Oct 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4-1mdv2009.1
+ Revision: 293009
- update to new version 1.4
  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3-2mdv2008.1
+ Revision: 182165
- rebuild
* Thu Feb 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3-1mdv2008.1
+ Revision: 176288
- add source and complete spec file
- Created package structure for ktsuss.
