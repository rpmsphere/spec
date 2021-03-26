%global debug_package %{nil}

Name:		andromeda
Version: 0.2.1.1336157239
Release: 11.1
License:	GPL
Source:		%{name}-%{version}.tar.bz2
Group:		Utility
Summary:	Qt file manager
URL:		https://gitorious.org/andromeda
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++, cmake, pkgconfig(QtGui), pkgconfig(QtWebKit)

%description
Cross-platform file manager, written on Qt.

%prep
%setup -q

%build
mkdir build
pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=release
make
popd

%install
%{__rm} -rf $RPM_BUILD_ROOT
pushd build
make DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc TODO.txt
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1.1336157239
- Rebuild for Fedora
* Thu Aug 16 2011 TI_Eugene <ti.eugene@gmail.com> 0.1
- Initial build on OBS
