Name:           faxpp
Version:        0.4
Release:        4.1
License:        Apache-2.0
Summary:        Fast XML Pull Parser
URL:            http://faxpp.sourceforge.net/
Group:          System/Libraries
Source0:        http://downloads.sourceforge.net/faxpp/faxpp-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FAXPP is a small, fast and conformant XML pull parser written in C with
an API that can return strings in any encoding including UTF-8 and
UTF-16.

%package devel
Summary:        FAXPP Development Files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files, documentation and examples for FAXPP.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%makeinstall
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc ChangeLog LICENSE TODO docs examples
%{_includedir}/faxpp
%{_libdir}/*.so

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
* Tue Nov  8 2011 lazy.kent@opensuse.org
- Corrected License tag.
- spec clean up.
* Sat Jun  4 2011 lazy.kent@opensuse.org
- Correct Summary tag
- Use full URL as a source
* Sat Apr  9 2011 lazy.kent@opensuse.org
- Initial package created - 0.4
