%undefine _debugsource_packages

Summary:        Full Qt4 based implementation of XML-RPC protocol
Name:           qxmlrpc
Version:        1
Release:        8.1
License:        GPL-3
Group:          System/Libraries
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++, qt4-devel

%description
It provides an easy way to construct, send and receive XML-RPC messages
on the client side, and process XML-RPC messages on the server side.

%package devel
Summary: Full Qt4 based implementation of XML-RPC protocol
Group:   Development/Libraries
Requires: %{name}

%description devel
Development files for qxmlrpc.

%prep
%setup -q
sed -i 's|staticlib|sharedlib|' xmlrpc.pro

%build
qmake-qt4
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}
install *.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install -m755 lib%{name}.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}
ln -s lib%{name}.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.1.0
ln -s lib%{name}.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so.1
ln -s lib%{name}.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so

%files
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}.so

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
* Tue Jun 28 2011 Alex Burmashev <burmashev@mandriva.org> 1-2
+ Revision: 687644
- spec fix
- small spec fix
- import qxmlrpc
