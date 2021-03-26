%global debug_package %{nil}

Name:		easypaint
Version: 	0.1.1
Release: 	3.1
License:	MIT
Source:		EasyPaint-%{version}.tar.gz
Group:		Graphics
Summary:	Easy graphic editing program
BuildRequires:	gcc-c++, cmake, pkgconfig(QtGui)

%description
EasyPaint is a simple graphics painting program.

%prep
%setup -q -n EasyPaint-%{version}

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

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_64.png

%changelog
* Tue Jan 09 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuild for Fedora
* Thu Apr 10 2012 Gr1N <grin.minsk@gmail.com>
- 0.1.0, first release
* Fri Apr 15 2011 TI_Eugene <ti.eugene@gmail.com>
- 0.0.1, initial OBS release
