%undefine _debugsource_packages

Name:		basqet
Version: 0.2.0.rev135
Release: 13.1
License:	GPL
Group:		Productivity/Office/Organizers
Summary:	Notes and Data in Baskets
URL:		https://code.google.com/p/basqet/
Vendor:		Erik Ridderby <erik.ridderby@gmail.com>
Source:		release_0.2.0-%{version}.tar.bz2
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++, pkgconfig, pkgconfig(QtGui)

%description
Keep your notes, pictures, ideas, and information in Baskets.

%prep
%setup -q -n release_0.2.0-%{version}

%build
qmake-qt4 PREFIX=/usr
%{__make}

%install
%{makeinstall} INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0.rev135
- Rebuilt for Fedora
* Tue Nov 10 2009 - TI_Eugene <ti.eugene@gmail.com> 0.2.0
- Initial build for OBS
