%undefine _debugsource_packages

Name:           limoo
BuildRequires:  cmake qt4-devel exiv2-devel
URL:            http://getsilicon.org/limoo/
License:        GPLv3
Group:          Productivity/Graphics/Viewers 
Summary:        An QML image viewer
Version:        1.3
Release:        8.1
Source0:        %{name}-src-%{version}.tar.gz

%description
Limoo is an image viewer created using QML, Qt and C++.

%prep
%setup -q -n %{name}-src-%{version}

%build
cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}

%install
%make_install
sed -i 's|/usr/share/pixmaps/%{name}.png|%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc README Authors COPYING
%{_bindir}/limoo
%{_datadir}/applications/limoo.desktop
%{_datadir}/pixmaps/limoo.png

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
* Fri Jul  6 2012 giacomosrv@gmail.com
- packaged limoo version 1.3
* Fri May 18 2012 giacomosrv@gmail.com
- packaged limoo version 1.2
* Sat Apr 28 2012 giacomosrv@gmail.com
- packaged limoo version 1.1.1
* Fri Apr 27 2012 giacomosrv@gmail.com
- packaged limoo version 1.1
* Thu Apr 26 2012 giacomosrv@gmail.com
- packaged limoo version 1.0
* Tue Apr 24 2012 giacomosrv@gmail.com
- packaged limoo version 0.9
* Sat Apr 14 2012 giacomosrv@gmail.com
- packaged limoo version 0.8
* Wed Apr  4 2012 giacomosrv@gmail.com
- packaged limoo version 0.7
* Sat Mar 31 2012 giacomosrv@gmail.com
- packaged limoo version 0.5
* Fri Mar 30 2012 giacomosrv@gmail.com
- packaged limoo version 0.4
