%global __os_install_post %{nil}

Name: box
Summary: Figure description language
Version: 0.4.0
Release: 5.1
Group: Development/Language
License: LGPLv2
URL: https://boxc.sourceforge.net/
Source0: https://sourceforge.net/projects/boxc/files/Box%20-%20the%20compiler/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires: cairo-devel

%description
Box is a language specifically designed to make vector graphics easy plus
a integrated development environment which facilitates the use of the language
by interactively showing the graphical output. Box combines the convenience of
drawing figures with the mouse with the convenience of describing them with
a language tailored for vector graphics.

%package devel
Summary: Development files for box
Requires: %{name}

%description devel
Header files and libraries for the package box.

%prep
%setup -q

%build
%configure --with-cairo
make

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING COPYING.LESSER README STYLE TODO
%{_bindir}/%{name}*
%{_libdir}/%{name}*
%{_libdir}/libboxcore*.so.*
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/%{name}*
%{_libdir}/libboxcore*.a
%{_libdir}/libboxcore*.la
%{_libdir}/libboxcore*.so

%changelog
* Fri Dec 11 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
