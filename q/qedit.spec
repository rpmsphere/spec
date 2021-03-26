Name:               qedit
Version:            2.8.3
Release:            1
License:            GPL
BuildRequires:      cmake qt4-devel aspell
Group:              Development/Tools/Other 
Summary:            Qt based advanced text editor
URL:                http://hugo.pereira.free.fr/software/index.php?page=package&package_list=software_list_qt&package=qedit
Source:             http://hugo.pereira.free.fr/software/tgz/%{name}-%{version}.tar.gz

%description
Qt based advanced text editor. Supports syntax highlighting, matching-
parenthesis highlighting, auto-indentation, customizable text macro for
many languages, such as C/C++, fortran, Makefile, HTML/XML, etc.
Can be plugged with aspell to provide automatic spell-checking.

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING
%{_bindir}/%{name}

%changelog
* Fri Dec 27 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.8.3
- Rebuild for Fedora
* Thu May 16 2013 giacomosrv@gmail.com
- updated to 2.6.3
* Sat Mar  2 2013 giacomosrv@gmail.com
- updated to 2.6.0
- added support for Qt5.0
- fixed some semi-reproducible crashes when closing some opened files
* Sat Jan 12 2013 giacomosrv@gmail.com
- updated to 2.5.3
* Wed Nov 14 2012 giacomosrv@gmail.com
- updated to 2.5.2
* Sun Oct 21 2012 giacomosrv@gmail.com
- packaged qedit 2.5.1
- first package release
