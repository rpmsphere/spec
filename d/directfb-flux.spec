%global debug_package %{nil}
Summary:	Interface description language used by DirectFB
Summary(pl.UTF-8):	język opisu interfejsów używany przez DirectFB
Name:		directfb-flux
Version:	1.4.4
Release:	3.1
License:	MIT
Group:		Development/Tools
Source0:	http://www.directfb.org/downloads/Core/flux/flux-%{version}.tar.gz
URL:		http://www.directfb.org/
#BuildRequires:	directfb-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
Requires:	directfb

%description
flux is an interface description language used by DirectFB.

fluxcomp compiles .flux files to .cpp or .c files.

%description -l pl.UTF-8
flux to język opisu interfejsów używany przez DirectFB.

fluxcomp kompiluje pliki .flux do plików .cpp lub .c.

%prep
%setup -q -n flux-%{version}

%build
%configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/fluxcomp

%changelog
* Thu Jan 02 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.4
- Rebuild for Fedora
* Tue Jun 19 2012 PLD Team <feedback@pld-linux.org>
- Revision 1.5 2012/06/19 19:02:23 qboosh - updated to 1.4.1
- Revision 1.4 2012/05/25 15:22:52 qboosh - updated to 1.3.0 (for DirectFB 1.4.17/1.6)
- Revision 1.3 2012/04/08 07:58:31 qboosh - updated to 1.2.0
- Revision 1.2 2012/01/01 09:49:35 qboosh - require DirectFB 1.4.15 as 1.4.14 had fluxcomp included
- Revision 1.1 2012/01/01 09:48:07 qboosh - new

