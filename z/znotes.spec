%undefine _debugsource_packages

Name:		znotes
Version:	0.4.5
Release:	22.1
License:	GPL
Vendor:		Peter Savichev <psavichev@gmail.com>
Source:		%{name}-%{version}.tar.gz
Summary:	Lightweigh crossplatform application for notes management
Group:		Productivity/Text/Utilities
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++, qt4-devel

%description
Lightweigh crossplatform application for notes management.
Inspired by xfce4-notes-plugin.

%prep
%setup -q
sed -i '1i #include <unistd.h>' single_inst/qtlocalpeer.cpp

%build
lrelease-qt4 %{name}.pro
qmake-qt4
make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall} INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.5
- Rebuilt for Fedora
* Sat Aug 27 2011 Peter Savichev (proton) <psavichev@gmail.com>
- 0.4.5
* Sun Jan 09 2011 Peter Savichev (proton) <psavichev@gmail.com>
- 0.4.4
* Sun Feb 14 2010 TI_Eugene <ti.eugene@gmail.com>
- 0.4.1
* Mon Feb 01 2010 TI_Eugene <ti.eugene@gmail.com>
- 0.4.0
* Sun Oct 25 2009 TI_Eugene <ti.eugene@gmail.com>
- initial package in OBS
